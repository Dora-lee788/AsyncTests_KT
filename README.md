# КТ «Асинхронные тесты»

Проект содержит 5 асинхронных тестов по заданию.

## Установка

В терминале VS Code из папки проекта выполните:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Если PowerShell не разрешает активацию виртуального окружения, можно не активировать его и выполнить установку через:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Запуск тестов

```powershell
python -m pytest -v
```

Или без активации окружения:

```powershell
.venv\Scripts\python.exe -m pytest -v
```

## Что проверяется

1. Future возвращает ожидаемое значение.
2. Future завершается ожидаемым исключением.
3. HTTP-запрос через `aiohttp` возвращает статус 200.
4. Новая запись добавляется в SQLite через `aiosqlite`.
5. Асинхронный вызов функции в отдельном потоке возвращает результат.

Для третьего теста необходимо подключение к интернету.
