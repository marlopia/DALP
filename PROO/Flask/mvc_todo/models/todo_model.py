from dataclasses import asdict, dataclass, field
from datetime import datetime
import os
from typing import List

from flask import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")


class ValidationError(ValueError):
    pass


@dataclass
class Todo:
    id: int
    title: str
    priority: str
    done: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)

    def validate(self) -> None:
        # Regla de negocio: título obligatorio y con longitud mínima
        if not isinstance(self.title, str):
            raise ValidationError("El título debe ser texto.")
        clean = self.title.strip()
        if len(clean) < 3:
            raise ValidationError("El título debe tener al menos 3 caracteres.")
        if self.priority not in ("low", "medium", "high"):
            raise ValidationError(
                "El valor de prioridad no coincide con los aceptados."
            )
        self.title = clean

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
        }


class TodoRepository:
    def __init__(self):

        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        self._items: List[Todo] = []

        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                created_at = item.get("created_at")
                if created_at:
                    created_at = datetime.fromisoformat(created_at)
                todo = Todo(
                    id=int(item["id"]),
                    title=item["title"],
                    priority=item["priority"],
                    done=item.get("done", False),
                    created_at=created_at,
                )
                self._items.append(todo)
        else:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)

    def list_all(self) -> list[Todo]:
        return list(self._items)

    def save_tasks(self) -> None:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(
                [t.to_dict() for t in self._items], f, indent=2, ensure_ascii=False
            )

    def add(self, todo: Todo) -> None:
        todo.validate()
        for item in self._items:
            if item.title.lower() == todo.title.lower():
                raise ValidationError("Tarea duplicada.")
        self._items.append(todo)
        self.save_tasks()

    def toggle(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise ValidationError("Índice fuera de rango.")
        self._items[index].done = not self._items[index].done
        self.save_tasks()

    def delete(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise ValidationError("Índice fuera de rango.")
        self._items.pop(index)
        self.save_tasks()

    def next_id(self) -> int:
        return len(self._items)
