from typing import List, Optional
from src.todo.models import Task
import copy # Added this import

class TodoService:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        task_id = self._next_id
        self._next_id += 1

        new_task = Task(id=task_id, title=title, description=description)
        self._tasks.append(new_task)
        return new_task

    def list_tasks(self) -> List[Task]:
        # Return deep copies to prevent external modification of internal Task objects
        return [copy.deepcopy(task) for task in self._tasks]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                if title is not None:
                    self._tasks[i].title = title
                if description is not None:
                    self._tasks[i].description = description
                return copy.deepcopy(self._tasks[i])
        return None

    def delete_task(self, task_id: int) -> bool:
        initial_len = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) < initial_len

    def toggle_task_status(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = not task.is_completed
                return True
        return False

