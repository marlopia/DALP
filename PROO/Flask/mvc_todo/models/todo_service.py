from .todo_model import Todo, TodoRepository, ValidationError


class TodoService:

    def __init__(self) -> None:
        self.repo = TodoRepository()

    def create_todo(self, title: str, priority: str) -> None:
        id = self.repo.next_id()
        self.repo.add(Todo(id=id, title=title, priority=priority))

    def toggle_todo(self, index: int) -> None:
        self.repo.toggle(index)

    def delete_todo(self, index: int) -> None:
        self.repo.delete(index)

    def total_complete(self) -> int:
        counter = 0
        for item in self.repo.list_all():
            if item.done:
                counter += 1

        return counter

    def validate_name(self, name: str) -> str:
        if not name.isalpha():
            raise ValidationError("Formato de nombre incorrecto")
        else:
            return name.lower().capitalize()
