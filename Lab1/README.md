# Team Board

Небольшая веб-доска задач команды. Данные хранятся в SQLite в памяти процесса.

## Запуск

```bash
python -m pip install -e '.[dev]' -r requirements.txt
uvicorn team_board.main:app --reload
```

Откройте `http://127.0.0.1:8000`.

## Проверка

```bash
pytest
```

Показатель выполнения задач на главной странице рассчитывается функцией
`calculate_completion_rate`. Её поведение проверяется тестами.
