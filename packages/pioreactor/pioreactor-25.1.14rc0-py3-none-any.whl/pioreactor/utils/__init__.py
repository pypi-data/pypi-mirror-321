# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import signal
import sqlite3
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from functools import wraps
from os import getpid
from threading import Event
from typing import Any
from typing import Callable
from typing import cast
from typing import Generator
from typing import overload
from typing import Sequence
from typing import TYPE_CHECKING

from msgspec import DecodeError
from msgspec import Struct
from msgspec.json import decode as loads
from msgspec.json import encode as dumps

from pioreactor import structs
from pioreactor import types as pt
from pioreactor import whoami
from pioreactor.config import config
from pioreactor.exc import JobRequiredError
from pioreactor.exc import NotActiveWorkerError
from pioreactor.exc import RoleError
from pioreactor.pubsub import create_client
from pioreactor.pubsub import patch_into
from pioreactor.pubsub import subscribe_and_callback
from pioreactor.utils.networking import resolve_to_address
from pioreactor.utils.timing import catchtime
from pioreactor.utils.timing import current_utc_timestamp

if TYPE_CHECKING:
    from pioreactor.pubsub import Client

JobMetadataKey = int


class callable_stack:
    """
    A class for managing a stack of callable objects in Python.

    Example:
    >>> def greet(name):
    ... print(f"Hello, {name}!")
    ...
    >>> def goodbye(name):
    ... print(f"Goodbye, {name}!")
    ...
    >>> my_stack = callable_stack()
    >>> my_stack.append(greet)
    >>> my_stack.append(goodbye)
    >>> my_stack('Alice')
    Goodbye, Alice!
    Hello, Alice!
    """

    def __init__(self, default_function_if_empty: Callable = lambda *args: None) -> None:
        self._callables: list[Callable] = []
        self.default = default_function_if_empty

    def append(self, function: Callable) -> None:
        self._callables.append(function)

    def __call__(self, *args) -> None:
        if not self._callables:
            self.default(*args)

        while self._callables:
            function = self._callables.pop()
            function(*args)


def append_signal_handler(signal_value: signal.Signals, new_callback: Callable) -> None:
    """
    The current api of signal.signal is a global stack of size 1, so if
    we have multiple jobs started in the same python process, we
    need them all to respect each others signal.
    """
    current_callback = signal.getsignal(signal_value)

    if callable(current_callback):
        if isinstance(current_callback, callable_stack):
            # we've previously added something to the handler..
            current_callback.append(new_callback)
            signal.signal(signal_value, current_callback)
        else:
            # no stack yet, default callable was present. Don't forget to add new callback, too
            stack = callable_stack(signal.default_int_handler)
            stack.append(current_callback)
            stack.append(new_callback)
            signal.signal(signal_value, stack)
    elif (current_callback is signal.SIG_DFL) or (current_callback is signal.SIG_IGN):
        # no stack yet.
        stack = callable_stack(signal.default_int_handler)
        stack.append(new_callback)
        signal.signal(signal_value, stack)
    elif current_callback is None:
        signal.signal(signal_value, callable_stack(signal.default_int_handler))
    else:
        raise RuntimeError(f"Something is wrong. Observed {current_callback}.")


def append_signal_handlers(signal_value: signal.Signals, new_callbacks: list[Callable]) -> None:
    for callback in new_callbacks:
        append_signal_handler(signal_value, callback)


class managed_lifecycle:
    """
    Wrap a block of code to have "state" in MQTT. See od_normalization, self_test, pump

    You can use send a "disconnected" to "pioreactor/<unit>/<exp>/<name>/$state/set" to stop/disconnect it.

    Example
    ----------

    > with managed_lifecycle(unit, experiment, "self_test") as state: # publishes "ready" to mqtt
    >    value = do_work()
    >    state.publish_setting("work", value) # looks like a entry from a published_setting
    >
    > # on close of block, a "disconnected" is fired to MQTT, regardless of how that end is achieved (error, return statement, etc.)


    If the program is required to know if it's killed, managed_lifecycle contains an event (see pump.py code)

    > with managed_lifecycle(unit, experiment, "self_test") as state:
    >    do_work()
    >
    >    state.block_until_disconnected()
    >    # or state.exit_event.is_set() or state.exit_event.wait(...) are other options.
    >

    For now, it's possible to run multiple jobs with the same name using this tool.

    """

    def __init__(
        self,
        unit: str,
        experiment: str,
        name: str,
        mqtt_client: Client | None = None,
        exit_on_mqtt_disconnect: bool = False,
        mqtt_client_kwargs: dict | None = None,
        ignore_is_active_state=False,  # hack and kinda gross
        is_long_running_job=False,
        source: str = "app",
        job_source: str | None = None,
    ) -> None:
        if not ignore_is_active_state and not whoami.is_active(unit):
            raise NotActiveWorkerError(f"{unit} is not active.")

        self.unit = unit
        self.experiment = experiment
        self.name = name
        self.state = "init"
        self.exit_event = Event()
        self._source = source
        self.is_long_running_job = is_long_running_job
        self._job_source = job_source or os.environ.get("JOB_SOURCE") or "user"

        last_will = {
            "topic": f"pioreactor/{self.unit}/{self.experiment}/{self.name}/$state",
            "payload": b"lost",
            "qos": 2,
            "retain": True,
        }

        default_mqtt_client_kwargs = {
            "keepalive": 5 * 60,
            "client_id": f"{self.name}-{self.unit}-{self.experiment}",
        }

        if mqtt_client:
            self._externally_provided_client = True
            self.mqtt_client = mqtt_client
        else:
            self._externally_provided_client = False
            self.mqtt_client = create_client(
                last_will=last_will,
                on_disconnect=self._on_disconnect if exit_on_mqtt_disconnect else None,
                **(default_mqtt_client_kwargs | (mqtt_client_kwargs or dict())),  # type: ignore
            )

        self.start_passive_listeners()

    def _exit(self, *args) -> None:
        # recall: we can't publish in a callback!
        self.exit_event.set()

    def _on_disconnect(self, *args):
        self._exit()

    def __enter__(self) -> managed_lifecycle:
        try:
            # this only works on the main thread.
            append_signal_handlers(signal.SIGTERM, [self._exit])
            append_signal_handlers(
                signal.SIGINT, [self._exit, lambda *args: signal.signal(signal.SIGINT, signal.SIG_IGN)]
            )  # ignore future sigints so we clean up properly.
        except ValueError:
            pass

        with JobManager() as jm:
            self._job_id = jm.register_and_set_running(
                self.unit,
                self.experiment,
                self.name,
                self._job_source,
                getpid(),
                "",  # TODO: why is leader string empty? perf?
                self.is_long_running_job,
            )

        self.state = "ready"
        self.publish_setting("$state", self.state)

        return self

    def __exit__(self, *args) -> None:
        self.state = "disconnected"
        self.publish_setting("$state", self.state)
        if not self._externally_provided_client:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()

        with JobManager() as jm:
            jm.set_not_running(self._job_id)

        return

    def exit_from_mqtt(self, message: pt.MQTTMessage) -> None:
        if message.payload == b"disconnected":
            self._exit()

    def start_passive_listeners(self) -> None:
        subscribe_and_callback(
            self.exit_from_mqtt,
            [
                f"pioreactor/{self.unit}/{self.experiment}/{self.name}/$state/set",
                f"pioreactor/{whoami.UNIVERSAL_IDENTIFIER}/{self.experiment}/{self.name}/$state/set",
                f"pioreactor/{whoami.UNIVERSAL_IDENTIFIER}/{whoami.UNIVERSAL_EXPERIMENT}/{self.name}/$state/set",
                f"pioreactor/{self.unit}/{whoami.UNIVERSAL_EXPERIMENT}/{self.name}/$state/set",
            ],
            client=self.mqtt_client,
        )
        return

    def block_until_disconnected(self) -> None:
        self.exit_event.wait()

    def publish_setting(self, setting: str, value: Any) -> None:
        self.mqtt_client.publish(
            f"pioreactor/{self.unit}/{self.experiment}/{self.name}/{setting}", value, retain=True
        )
        with JobManager() as jm:
            jm.upsert_setting(self._job_id, setting, value)


class cache:
    @staticmethod
    def adapt_key(key):
        # keys can be tuples!
        return dumps(key)

    @staticmethod
    def convert_key(s):
        if isinstance(s, bytes):
            try:
                return loads(s)
            except DecodeError:
                return s.decode()
        else:
            return s

    def __init__(self, table_name, db_path):
        self.table_name = f"cache_{table_name}"
        self.db_path = db_path

    def __enter__(self):
        sqlite3.register_adapter(tuple, self.adapt_key)
        # sqlite3.register_converter("_key_BLOB", self.convert_key)

        self.conn = sqlite3.connect(self.db_path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA journal_mode=WAL;")
        self._initialize_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def _initialize_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                key _key_BLOB PRIMARY KEY,
                value BLOB
            )
        """
        )

    def __setitem__(self, key, value):
        self.cursor.execute(
            f"""
            INSERT INTO {self.table_name} (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value
        """,
            (key, value),
        )

    def set(self, key, value):
        return self.__setitem__(key, value)

    def get(self, key, default=None):
        self.cursor.execute(f"SELECT value FROM {self.table_name} WHERE key = ?", (key,))
        result = self.cursor.fetchone()
        return result[0] if result else default

    def iterkeys(self):
        self.cursor.execute(f"SELECT key FROM {self.table_name}")
        return (self.convert_key(row[0]) for row in self.cursor.fetchall())

    def pop(self, key, default=None):
        self.cursor.execute(f"SELECT value FROM {self.table_name} WHERE key = ?", (key,))
        result = self.cursor.fetchone()
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE key = ?", (key,))

        if result is None:
            return default
        else:
            return result[0]

    def __contains__(self, key):
        self.cursor.execute(f"SELECT 1 FROM {self.table_name} WHERE key = ?", (key,))
        return self.cursor.fetchone() is not None

    def __iter__(self):
        return self.iterkeys()

    def __delitem__(self, key):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE key = ?", (key,))

    def __getitem__(self, key):
        self.cursor.execute(f"SELECT value FROM {self.table_name} WHERE key = ?", (key,))
        result = self.cursor.fetchone()
        if result is None:
            raise KeyError(f"Key '{key}' not found in cache.")
        return result[0]


@contextmanager
def local_intermittent_storage(
    cache_name: str,
) -> Generator[cache, None, None]:
    """

    The cache is deleted upon a Raspberry Pi restart!

    Examples
    ---------
    > with local_intermittent_storage('pwm') as cache:
    >     assert '1' in cache
    >     cache['1'] = 0.5


    Notes
    -------
    Opening the same cache in a context manager is tricky, and should be avoided.

    """
    with cache(cache_name, db_path=config.get("storage", "temporary_cache")) as c:
        yield c


@contextmanager
def local_persistent_storage(
    cache_name: str,
) -> Generator[cache, None, None]:
    """
    Values stored in this storage will stay around between RPi restarts, and until overwritten
    or deleted.

    Examples
    ---------
    > with local_persistent_storage('od_blank') as cache:
    >     assert '1' in cache
    >     cache['1'] = 0.5

    """

    with cache(cache_name, db_path=config.get("storage", "persistent_cache")) as c:
        yield c


def clamp(minimum: float | int, x: float | int, maximum: float | int) -> float:
    return max(minimum, min(x, maximum))


@overload
def is_pio_job_running(target_jobs: list[str]) -> list[bool]:
    ...


@overload
def is_pio_job_running(target_jobs: str) -> bool:
    ...


def is_pio_job_running(target_jobs):
    """
    pass in jobs to check if they are running
    ex:

    > result = is_pio_job_running("od_reading")
    > # True

    > result = is_pio_job_running(["od_reading", "stirring"])
    > # [True, False]
    """
    if isinstance(target_jobs, str):
        target_jobs = (target_jobs,)

    results = []

    with JobManager() as jm:
        for job in target_jobs:
            results.append(jm.is_job_running(job))

    if len(target_jobs) == 1:
        return results[0]
    else:
        return results


def get_cpu_temperature() -> float:
    if whoami.is_testing_env():
        return 22.0

    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temperature_celcius = int(f.read().strip()) / 1000.0
    except FileNotFoundError:
        return -999
    return cpu_temperature_celcius


def argextrema(x: Sequence) -> tuple[int, int]:
    min_, max_ = float("inf"), float("-inf")
    argmin_, argmax_ = 0, 0
    for i, value in enumerate(x):
        if value < min_:
            min_ = value
            argmin_ = i
        if value > max_:
            max_ = value
            argmax_ = i
    return argmin_, argmax_


class SummableDict(dict):
    """
    SummableDict is a subclass of dict that allows for easy addition of two dictionaries by key.
    If a key exists in both dictionaries, the values are added together.
    If a key only exists in one dictionary, it is included in the result with its original value.

    Example
    ---------
    # create two SummableDicts
    d1 = SummableDict({'a': 1, 'b': 2})
    d2 = SummableDict({'b': 3, 'c': 4})

    # add them together
    result = d1 + d2

    # result should be {'a': 1, 'b': 5, 'c': 4}

    # also has a default value:
    print(result['missing_key']) # 0.0


    """

    def __init__(self, *arg, **kwargs) -> None:
        dict.__init__(self, *arg, **kwargs)

    def __add__(self, other: SummableDict) -> SummableDict:
        s = SummableDict()
        for key in self:
            s[key] += self[key]
        for key in other:
            s[key] += other[key]

        return s

    def __iadd__(self, other: SummableDict) -> SummableDict:
        return self + other

    def __getitem__(self, key: str) -> float:
        if key not in self:
            return 0.0  # TODO: later could be generalized for the init to accept a zero element.
        else:
            return dict.__getitem__(self, key)


def boolean_retry(
    func: Callable[..., bool],
    retries: int = 3,
    sleep_for: float = 0.25,
    args: tuple = (),
    kwargs: dict = {},
) -> bool:
    """
    Retries a function upon encountering an False return until it succeeds or the maximum number of retries is exhausted.

    """
    for _ in range(retries):
        res = func(*args, **kwargs)
        if res:
            return res
        time.sleep(sleep_for)
    return False


def exception_retry(func: Callable, retries: int = 3, sleep_for: float = 0.5, args=(), kwargs={}) -> Any:
    """
    Retries a function upon encountering an exception until it succeeds or the maximum number of retries is exhausted.

    Parameters
    -----------
    func (callable): The function to be retried.
    retries (int, optional): The maximum number of times to retry the function. Defaults to 3.
    delay (float, optional): The number of seconds to wait between retries. Defaults to 0.5.
    args (tuple, optional): The positional arguments to pass to the function. Defaults to an empty tuple.
    kwargs (dict, optional): The keyword arguments to pass to the function. Defaults to an empty dictionary.

    Returns
    --------
    The return value of the function call, if the function call is successful.

    Raises
    --------
    Exception: The exception raised by the function call if the function call is unsuccessful after the specified number of retries.

    Example
    --------

    > def risky_function(x, y):
    >     return x / y
    >
    > # Call the function with retry
    > result = exception_retry(risky_function, retries=5, sleep_for=1, args=(10, 0))
    """
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if i == retries - 1:  # If this was the last attempt
                raise e
            time.sleep(sleep_for)


def safe_kill(*args: str) -> None:
    from subprocess import run

    try:
        run(("kill", "-2") + args)
    except Exception:
        pass


class ShellKill:
    def __init__(self) -> None:
        self.list_of_pids: list[int] = []

    def append(self, pid: int) -> None:
        self.list_of_pids.append(pid)

    def kill_jobs(self) -> int:
        if len(self.list_of_pids) == 0:
            return 0

        safe_kill(*(str(pid) for pid in self.list_of_pids))

        return len(self.list_of_pids)


class JobManager:
    def __init__(self) -> None:
        db_path = config.get("storage", "temporary_cache")
        self.conn = sqlite3.connect(db_path, isolation_level=None)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA journal_mode=WAL;")
        self._create_tables()

    def _create_tables(self) -> None:
        # TODO: add a created_at, updated_at to pio_job_published_settings
        create_table_query = """
        CREATE TABLE IF NOT EXISTS pio_job_metadata (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            unit         TEXT NOT NULL,
            experiment   TEXT NOT NULL,
            job_name     TEXT NOT NULL,
            job_source   TEXT NOT NULL,
            started_at   TEXT NOT NULL,
            is_running   INTEGER NOT NULL,
            leader       TEXT NOT NULL,
            pid          INTEGER NOT NULL,
            is_long_running_job INTEGER NOT NULL,
            ended_at     TEXT
        );

        CREATE TABLE IF NOT EXISTS pio_job_published_settings (
            setting        TEXT NOT NULL,
            value          BLOB,
            proposed_value BLOB,
            job_id         INTEGER NOT NULL,
            FOREIGN KEY(job_id) REFERENCES pio_job_metadata(id),
            UNIQUE(setting, job_id)
        );

        CREATE INDEX IF NOT EXISTS idx_pio_job_metadata_is_running ON pio_job_metadata(is_running);
        CREATE INDEX IF NOT EXISTS idx_pio_job_metadata_is_running_experiment ON pio_job_metadata(is_running, experiment);
        CREATE INDEX IF NOT EXISTS idx_pio_job_metadata_job_name ON pio_job_metadata(job_name);

        CREATE INDEX IF NOT EXISTS idx_pio_job_published_settings_job_id ON pio_job_published_settings(job_id);
        CREATE UNIQUE INDEX IF NOT EXISTS  idx_pio_job_published_settings_setting_job_id ON pio_job_published_settings(setting, job_id);
        """
        self.cursor.executescript(create_table_query)

    def register_and_set_running(
        self,
        unit: str,
        experiment: str,
        job_name: str,
        job_source: str | None,
        pid: int,
        leader: str,
        is_long_running_job: bool,
    ) -> JobMetadataKey:
        insert_query = "INSERT INTO pio_job_metadata (started_at, is_running, job_source, experiment, unit, job_name, leader, pid, is_long_running_job, ended_at) VALUES (STRFTIME('%Y-%m-%dT%H:%M:%f000Z', 'NOW'), 1, :job_source, :experiment, :unit, :job_name, :leader, :pid, :is_long_running_job, NULL);"

        self.cursor.execute(
            insert_query,
            {
                "unit": unit,
                "experiment": experiment,
                "job_source": job_source,
                "pid": pid,
                "leader": leader,
                "job_name": job_name,
                "is_long_running_job": is_long_running_job,
            },
        )
        assert isinstance(self.cursor.lastrowid, int)
        return self.cursor.lastrowid

    def upsert_setting(self, job_id: JobMetadataKey, setting: str, value: Any) -> None:
        if value is None:
            # delete
            delete_query = """
            DELETE FROM pio_job_published_settings WHERE setting = :setting and job_id = :job_id
            """
            self.cursor.execute(delete_query, {"setting": setting, "job_id": job_id})
        else:
            # upsert
            update_query = """
            INSERT INTO pio_job_published_settings (setting, value, job_id)
            VALUES (:setting, :value, :job_id)
                ON CONFLICT (setting, job_id) DO
                UPDATE SET value = :value;
            """
            if isinstance(value, dict):
                value = dumps(value).decode()  # back to string, not bytes
            elif isinstance(value, Struct):
                value = str(value)  # complex type

            self.cursor.execute(update_query, {"setting": setting, "value": value, "job_id": job_id})

        return

    def get_setting_from_running_job(self, job_name: str, setting: str, timeout=None) -> Any:
        if timeout is not None and not self.is_job_running(job_name):
            raise JobRequiredError(f"Job {job_name} is not running.")

        with catchtime() as timer:
            while True:
                select_query = """
                    SELECT value
                        FROM pio_job_published_settings s
                        JOIN pio_job_metadata m ON s.job_id = m.id
                    WHERE job_name=(?) and setting=(?) and is_running=1"""
                self.cursor.execute(select_query, (job_name, setting))
                result = self.cursor.fetchone()  # returns None if not found

                if result:
                    return result[0]

                if (timeout and timer() > timeout) or (timeout is None):
                    raise NameError(f"Setting {setting} was not found.")

    def set_not_running(self, job_id: JobMetadataKey) -> None:
        update_query = "UPDATE pio_job_metadata SET is_running=0, ended_at=STRFTIME('%Y-%m-%dT%H:%M:%f000Z', 'NOW') WHERE id=(?)"
        self.cursor.execute(update_query, (job_id,))
        return

    def is_job_running(self, job_name: str) -> bool:
        select_query = """SELECT pid FROM pio_job_metadata WHERE job_name=(?) and is_running=1"""
        self.cursor.execute(select_query, (job_name,))
        return len(self.cursor.fetchall()) > 0

    def _get_jobs(self, all_jobs: bool = False, **query) -> list[tuple[str, int]]:
        if not all_jobs:
            # Construct the WHERE clause based on the query parameters
            where_clause = " AND ".join([f"{key} = :{key}" for key in query.keys() if query[key] is not None])

            # Construct the SELECT query
            select_query = f"""
                SELECT
                    job_name, pid
                FROM pio_job_metadata
                WHERE is_running=1
                AND {where_clause};
            """

            # Execute the query and fetch the results
            self.cursor.execute(select_query, query)

        else:
            # Construct the SELECT query
            select_query = (
                "SELECT job_name, pid FROM pio_job_metadata WHERE is_running=1 AND is_long_running_job=0"
            )

            # Execute the query and fetch the results
            self.cursor.execute(select_query)

        return self.cursor.fetchall()

    def kill_jobs(self, all_jobs: bool = False, **query) -> int:
        # ex: kill_jobs(experiment="testing_exp") should end all jobs with experiment='testing_exp'

        shell_kill = ShellKill()
        count = 0

        for job, pid in self._get_jobs(all_jobs, **query):
            if job == "led_intensity":
                # led_intensity doesn't register with the JobManager, probably should somehow. #502
                continue
            else:
                shell_kill.append(pid)

        count += shell_kill.kill_jobs()

        return count

    def close(self):
        self.conn.close()

    def __enter__(self) -> JobManager:
        return self

    def __exit__(self, *args) -> None:
        self.close()
        return


class ClusterJobManager:
    # this is a context manager to mimic the kill API for JobManager.
    def __init__(self) -> None:
        if not whoami.am_I_leader():
            raise RoleError("Must be leader to use this. Maybe you want JobManager?")

    @staticmethod
    def kill_jobs(
        units: tuple[str, ...],
        all_jobs: bool = False,
        experiment: str | None = None,
        job_name: str | None = None,
        job_source: str | None = None,
    ) -> list[tuple[bool, dict]]:
        if len(units) == 0:
            return []

        if experiment:
            endpoint = f"/unit_api/jobs/stop/experiment/{experiment}"
        if job_name:
            endpoint = f"/unit_api/jobs/stop/job_name/{job_name}"
        if job_source:
            endpoint = f"/unit_api/jobs/stop/job_source/{job_source}"
        if all_jobs:
            endpoint = "/unit_api/jobs/stop/all"

        def _thread_function(unit: str) -> tuple[bool, dict]:
            try:
                r = patch_into(resolve_to_address(unit), endpoint)
                r.raise_for_status()
                return True, r.json()
            except Exception as e:
                print(f"Failed to send kill command to {unit}: {e}")
                return False, {"unit": unit}

        with ThreadPoolExecutor(max_workers=len(units)) as executor:
            results = executor.map(_thread_function, units)

        return list(results)

    def __enter__(self) -> ClusterJobManager:
        return self

    def __exit__(self, *args) -> None:
        return
