from dataclasses import dataclass, field
from datetime import datetime


class ValidationError(ValueError):
    pass


@dataclass
class Todo:
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


class TodoRepository:
    # Repositorio simple en memoria (para practicar MVC sin BD).
    def __init__(self):
        self._items: list[Todo] = []

    def list_all(self) -> list[Todo]:
        return list(self._items)

    def add(self, todo: Todo) -> None:
        todo.validate()
        for item in self._items:
            if item.title.lower() == todo.title.lower():
                raise ValidationError("Tarea duplicada.")
        self._items.append(todo)

    def toggle(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise ValidationError("Índice fuera de rango.")
        self._items[index].done = not self._items[index].done

    def delete(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise ValidationError("Índice fuera de rango.")
        self._items.pop(index)
