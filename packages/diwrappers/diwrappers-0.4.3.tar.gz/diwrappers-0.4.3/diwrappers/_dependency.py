import contextlib
import enum
import functools
import random
import typing as t
import uuid
from collections import abc
from dataclasses import dataclass
from functools import cache

import diwrappers._commons._data as d


@dataclass
class Injector[Data]:
    """A dependency injection container.

    This class provides a flexible way to manage dependencies in your
    application, supporting both regular dependency injection and
    testing scenarios through context managers that allow temporary
    dependency replacement.

    Type Parameters:
        Data: The type of the dependency being managed by this injector.

    """

    _constructor: t.Callable[[], Data]
    """Function that creates new instances of the dependency."""

    @contextlib.contextmanager
    def fake_value(self, val: Data) -> abc.Generator[Data, None, None]:
        """Temporarily replace the dependency with a specific value.

        Args:
            val: The value to use instead of the normal dependency.

        Yields:
            The provided fake value.

        """
        tmp_constructor = self._constructor
        self._constructor = lambda: val
        try:
            yield val
        finally:
            self._constructor = tmp_constructor

    def faker(self, fake_constructor: t.Callable[[], Data]):
        """Create a context manager to replace the dependency constructor.

        Args:
            fake_constructor:
                A callable that will temporarily replace the normal
                dependency constructor.

        Returns:
            A context manager that can be used to temporarily
            replace the dependency constructor.

        """

        @contextlib.contextmanager
        def wrapper():
            tmp_constructor = self._constructor
            self._constructor = fake_constructor
            try:
                yield
            finally:
                self._constructor = tmp_constructor

        return wrapper

    def inject[**TaskParams, TaskReturn](
        self,
        task: t.Callable[t.Concatenate[Data, TaskParams], TaskReturn],
    ) -> t.Callable[TaskParams, TaskReturn]:
        """Decorate a function to inject the dependency as its first argument.

        Type Parameters:
            TaskParams: Type parameters for the decorated function's arguments
            TaskReturn: Return type of the decorated function

        Args:
            task:
                The function to be decorated.
                Its first parameter must be of type Data.

        Returns:
            A wrapped function that will automatically
            receive the dependency as its first argument.

        """

        @functools.wraps(task)
        def _wrapper(*args: TaskParams.args, **kwargs: TaskParams.kwargs):
            """Create and inject the dependency."""
            data = self._constructor()
            return task(data, *args, **kwargs)

        return _wrapper


def dependency[Data](func: t.Callable[[], Data]) -> Injector[Data]:
    """Create a dependency injector from a constructor function.

    Type Parameters:
        Data: The type of the dependency being created

    Args:
        func: A constructor function that creates the dependency

    """
    return Injector(func)


if d.is_test_env():
    import pytest
    # SECTION tests

    # fake data
    NAME = "user_name"
    PROD_TOKEN = uuid.uuid4().hex
    FAKE_TOKEN = uuid.uuid4().hex
    PROD_URL = "http://prod-api.com"
    FAKE_URL = "http://fake-api.com"
    FAKE_INT = 1234

    def test_token_injection() -> None:
        @dependency
        def token() -> str:
            return "test_token"

        @token.inject
        def build_http_headers(token: str):
            return {"Authorization": f"Bearer {token}"}

        for i in range(3):
            headers = build_http_headers()
            assert headers["Authorization"] == "Bearer test_token", (
                f"Attempt {i}"
            )

    def test_singleton_dependency() -> None:
        counter = 0

        @dependency
        @cache
        def get_counter():
            nonlocal counter
            counter += 1
            return counter

        @get_counter.inject
        def read_counter(counter: int):
            return counter

        assert read_counter() == 1, "must always return the same value"
        assert read_counter() == 1, "must always return the same value"
        assert read_counter() == 1, "must always return the same value"
        assert read_counter() == 1, "must always return the same value"

        assert counter == 1, (
            "constructor can only be called once"
        )  # Constructor called only once

    # types and data for using random during tests

    class _NormalRange(enum.IntEnum):
        """Ground truth range for random number generation."""

        START = 1
        END = 10

    class _TestRAnge(enum.IntEnum):
        """Modified range for testing purposes."""

        START = 11
        END = 15

    N_TRIALS = 100
    """ Number of times the distribution will be sampled """

    SEED = 42
    """ Seed for the pRNG """

    @pytest.fixture(autouse=True)
    def set_random_seed() -> None:
        random.seed(SEED)

    def test_faker_decorator() -> None:
        @dependency
        def random_int() -> int:
            return random.randint(_NormalRange.START, _NormalRange.END)  # nosec - for testing purposes, not used in package

        @random_int.faker
        def fake_random_int() -> int:
            return random.randint(_TestRAnge.START, _TestRAnge.END)  # nosec - for testing purposes, not used in package

        @random_int.inject
        def get_number(random_int: int) -> int:
            return random_int

        # Test normal behavior
        assert all(
            _NormalRange.START <= get_number() <= _NormalRange.END
            for _ in range(N_TRIALS)
        )

        # Test with faker
        with fake_random_int():
            assert all(
                _TestRAnge.START <= get_number() <= _TestRAnge.END
                for _ in range(N_TRIALS)
            )

        # Test restoration after context
        assert all(
            _NormalRange.START <= get_number() <= _NormalRange.END
            for _ in range(N_TRIALS)
        )

    def test_fake_value_context() -> None:
        @dependency
        def random_int():
            return random.randint(_NormalRange.START, _NormalRange.END)  # nosec - for testing purposes, not used in package

        @random_int.inject
        def get_number(random_int: int):
            return random_int

        # Test normal behavior
        assert all(
            _NormalRange.START <= get_number() <= _NormalRange.END
            for _ in range(N_TRIALS)
        )

        # Test with fake value
        with random_int.fake_value(FAKE_INT) as fake_int:
            assert get_number() == FAKE_INT
            assert fake_int == FAKE_INT

        # Test restoration after context
        assert all(
            _NormalRange.START <= get_number() <= _NormalRange.END
            for _ in range(N_TRIALS)
        )

    def test_multiple_fake_contexts() -> None:
        @dependency
        def random_int():
            return random.randint(_NormalRange.START, _NormalRange.END)

        @dependency
        def token():
            return PROD_TOKEN

        @dependency
        def api_base_url():
            return PROD_URL

        @random_int.inject
        @token.inject
        @api_base_url.inject
        def get_random_user(
            base_url: str, token: str, random_int: int, name: str,
        ):
            return base_url, token, random_int, name

        with (
            random_int.fake_value(FAKE_INT) as fake_int,
            token.fake_value(FAKE_TOKEN) as fake_token,
            api_base_url.fake_value(FAKE_URL) as fake_api_base_url,
        ):
            assert fake_int == FAKE_INT
            assert fake_token == FAKE_TOKEN
            assert fake_api_base_url == FAKE_URL

            _base_url, _token, _random_int, _name = get_random_user(name=NAME)

            assert _base_url == fake_api_base_url
            assert _token == fake_token
            assert _random_int == fake_int
            assert _name == NAME

    def test_chained_dependencies() -> None:
        @dependency
        def token() -> str:
            return "test_token"

        values: list[str] = []

        @dependency
        @token.inject
        def client(token: str) -> str:
            values.append(token)
            return "test_client"

        @client.inject
        def use_client(client: str):
            values.append(client)
            return client

        result = use_client()
        assert result == "test_client"
        assert values == ["test_token", "test_client"]

    def test_multiple_dependencies() -> None:
        @dependency
        def logger() -> str:
            return "logger_instance"

        @dependency
        def db_connection() -> str:
            return "db_connection_instance"

        @logger.inject
        @db_connection.inject
        def use_services(db_connection: str, logger: str) -> str:
            return f"Using {db_connection} with {logger}"

        assert (
            use_services()
            == "Using db_connection_instance with logger_instance"
        )

    def test_dependency_replacement() -> None:
        @dependency
        def config() -> dict[str, str]:
            return {"env": "production"}

        @config.inject
        def get_env(config: dict[str, str]) -> str:
            return config["env"]

        assert get_env() == "production"

        with config.fake_value({"env": "test"}):
            assert get_env() == "test"

        assert get_env() == "production"

    def test_injected_function_exception() -> None:
        @dependency
        def db_connection() -> str:
            return "db"

        @db_connection.inject
        def failing_function(_db_connection: str) -> t.NoReturn:
            msg = "Simulated error"
            raise ValueError(msg)

        with pytest.raises(ValueError, match="Simulated error"):
            failing_function()

    def test_thread_safety() -> None:
        import threading

        range_start = 1
        range_end = 100

        @dependency
        def random_number() -> int:
            return random.randint(range_start, range_end)

        @random_number.inject
        def get_number(random_number: int) -> int:
            return random_number

        results: list[int] = []

        def worker() -> None:
            results.append(get_number())

        number_of_threads = 10
        threads = [
            threading.Thread(target=worker) for _ in range(number_of_threads)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        assert len(results) == number_of_threads
        assert all(
            isinstance(num, int) and range_start <= num <= range_end
            for num in results
        )

    GT_TOKEN = uuid.uuid4().hex
    FAKE_1 = uuid.uuid4().hex
    FAKE_2 = uuid.uuid4().hex

    def test_nested_fakers() -> None:
        @dependency
        def token() -> str:
            return GT_TOKEN

        @token.faker
        def fake_token_1():
            return FAKE_1

        @token.faker
        def fake_token_2():
            return FAKE_2

        @token.inject
        def assert_gt(token: str) -> None:
            assert token == GT_TOKEN

        @token.inject
        def assert_fake_1(token: str) -> None:
            assert token == FAKE_1

        @token.inject
        def assert_fake_2(token: str) -> None:
            assert token == FAKE_2

        assert_gt()

        with fake_token_1():
            assert_fake_1()
            with fake_token_2():
                assert_fake_2()
                with fake_token_1():
                    assert_fake_1()
                assert_fake_2()

                assert_fake_2()
                with fake_token_1():
                    assert_fake_1()
                assert_fake_2()

            assert_fake_1()

        assert_gt()
