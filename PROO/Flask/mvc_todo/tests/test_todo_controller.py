from unittest.mock import mock_open, patch
import pytest

from PROO.Flask.mvc_todo.models.todo_model import Todo, TodoRepository, ValidationError

# Todo


def test_todo_validate_ok():
    t = Todo(id=1, title="Comprar leche", priority="low")
    t.validate()
    assert t.title == "Comprar leche"


def test_todo_validate_title_too_short():
    t = Todo(id=2, title="ab", priority="low")
    with pytest.raises(ValidationError) as exc:
        t.validate()
    assert "al menos 3 caracteres" in str(exc.value)


def test_todo_validate_invalid_priority():
    t = Todo(id=3, title="Tarea válida", priority="urgent")
    with pytest.raises(ValidationError) as exc:
        t.validate()
    assert "prioridad no coincide" in str(exc.value)


def test_todo_validate_title_not_string():
    t = Todo(id=4, title=123, priority="low")  # type: ignore
    with pytest.raises(ValidationError) as exc:
        t.validate()
    assert "debe ser texto" in str(exc.value)


# TodoRepository


@pytest.fixture
def repo_no_disk():
    # Parcheamos os.makedirs y open para que no toquen disco
    with patch("os.makedirs"), patch("builtins.open", mock_open(read_data="[]")), patch(
        "json.dump"
    ):
        yield TodoRepository()


def test_todorepository_toggle_out_of_index(repo_no_disk):
    repo = repo_no_disk
    repo._items = [Todo(id=0, title="Tarea", priority="low")]

    with pytest.raises(ValidationError) as exc:
        repo.toggle(-1)
    assert "Índice fuera de rango" in str(exc.value)

    with pytest.raises(ValidationError) as exc:
        repo.toggle(10)
    assert "Índice fuera de rango" in str(exc.value)


def test_todorepository_delete_out_of_index(repo_no_disk):
    repo = repo_no_disk
    repo._items = [Todo(id=0, title="Tarea", priority="low")]

    with pytest.raises(ValidationError) as exc:
        repo.delete(-1)
    assert "Índice fuera de rango" in str(exc.value)

    with pytest.raises(ValidationError) as exc:
        repo.delete(10)
    assert "Índice fuera de rango" in str(exc.value)
