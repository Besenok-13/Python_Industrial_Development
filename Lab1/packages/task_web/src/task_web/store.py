from dataclasses import dataclass
from datetime import date
import sqlite3


@dataclass(frozen=True)
class Task:
    title: str
    status: str
    due_date: date


class TaskStore:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS tasks (title TEXT, status TEXT, due_date TEXT)"
        )

    def seed(self) -> None:
        if self.connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]:
            return
        self.connection.executemany(
            "INSERT INTO tasks VALUES (?, ?, ?)",
            [
                ("Подготовить макет", "done", "2026-09-12"),
                ("Проверить данные", "in progress", "2026-09-15"),
                ("Провести демо", "todo", "2026-09-18"),
            ],
        )
        self.connection.commit()

    def list_tasks(self) -> list[Task]:
        return [Task(title, status, date.fromisoformat(due_date)) for title, status, due_date in self.connection.execute("SELECT * FROM tasks")]
