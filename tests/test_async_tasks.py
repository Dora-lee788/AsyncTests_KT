import pytest
import aiohttp
import aiosqlite

from async_functions import (
    future_result,
    future_error,
    fetch_api_status,
    add_user,
    run_in_thread,
)


@pytest.mark.asyncio
async def test_future_returns_expected_value(event_loop):
    result = await future_result()
    assert result == "Готово"


@pytest.mark.asyncio
async def test_future_raises_expected_exception(event_loop):
    with pytest.raises(ValueError, match="Ожидаемая ошибка"):
        await future_error()


@pytest.mark.asyncio
async def test_http_request_returns_success_status(event_loop):
    status = await fetch_api_status("https://httpbin.org/status/200")
    assert status == 200


@pytest.mark.asyncio
async def test_database_adds_new_record(event_loop, tmp_path):
    database_path = str(tmp_path / "test.db")
    result = await add_user(database_path, "Дарья")
    assert result == "Дарья"

    async with aiosqlite.connect(database_path) as database:
        async with database.execute("SELECT COUNT(*) FROM users WHERE name = ?", ("Дарья",)) as cursor:
            row = await cursor.fetchone()

    assert row[0] == 1


@pytest.mark.asyncio
async def test_async_function_in_separate_thread_returns_result(event_loop):
    result = await run_in_thread()
    assert result == 5
