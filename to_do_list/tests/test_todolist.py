import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.todolist import ToDoList


def test_add_task_direct():
    todo = ToDoList()
    todo.tasks.append("task1")
    assert "task1" in todo.tasks


def test_remove_task_direct():
    todo = ToDoList()
    todo.tasks = ["task1", "task2"]
    todo.tasks.pop(0)
    assert todo.tasks == ["task2"]
