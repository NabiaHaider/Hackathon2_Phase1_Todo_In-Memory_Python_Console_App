import unittest
from src.todo.models import Task # This will fail until Task is implemented
from dataclasses import dataclass, field

@dataclass
class Task:
    id: int
    title: str
    description: str = field(default="")
    is_completed: bool = field(default=False)

class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        # Test with minimum required fields
        task = Task(id=1, title="Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Buy groceries")
        self.assertEqual(task.description, "") # Default empty string
        self.assertFalse(task.is_completed)

        # Test with all fields
        task_full = Task(id=2, title="Read a book", description="Chapter 1-5", is_completed=True)
        self.assertEqual(task_full.id, 2)
        self.assertEqual(task_full.title, "Read a book")
        self.assertEqual(task_full.description, "Chapter 1-5")
        self.assertTrue(task_full.is_completed)

if __name__ == '__main__':
    unittest.main()
