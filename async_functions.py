import asyncio
import aiohttp
import aiosqlite


async def future_result():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    future.set_result("Готово")
    return await future


async def future_error():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    future.set_exception(ValueError("Ожидаемая ошибка"))
    return await future


async def fetch_api_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return response.status


async def add_user(database_path, name):
    async with aiosqlite.connect(database_path) as database:
        await database.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)"
        )
        await database.execute("INSERT INTO users (name) VALUES (?)", (name,))
        await database.commit()

        async with database.execute(
            "SELECT name FROM users WHERE id = last_insert_rowid()"
        ) as cursor:
            row = await cursor.fetchone()

        return row[0]


async def run_in_thread():
    return await asyncio.to_thread(run_async_function_in_thread)


def run_async_function_in_thread():
    return asyncio.run(async_calculate_value())


async def async_calculate_value():
    await asyncio.sleep(0)
    return 2 + 3
