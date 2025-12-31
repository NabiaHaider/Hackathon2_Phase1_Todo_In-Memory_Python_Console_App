import unittest
from src.todo.service import TodoService
from src.todo.models import Task

class TestTodoService(unittest.TestCase):
    def setUp(self):
        self.service = TodoService()

    def test_add_task(self):
        initial_task_count = len(self.service.list_tasks())

        task1 = self.service.add_task("Buy groceries")
        self.assertEqual(len(self.service.list_tasks()), initial_task_count + 1)
        self.assertEqual(task1.title, "Buy groceries")
        self.assertEqual(task1.description, "")
        self.assertFalse(task1.is_completed)
        self.assertIsInstance(task1.id, int) # Check if id is an integer

        task2 = self.service.add_task("Read a book", "Chapter 1-5")
        self.assertEqual(len(self.service.list_tasks()), initial_task_count + 2)
        self.assertEqual(task2.title, "Read a book")
        self.assertEqual(task2.description, "Chapter 1-5")
        self.assertFalse(task2.is_completed)
        self.assertIsInstance(task2.id, int)
        self.assertNotEqual(task1.id, task2.id) # Ensure IDs are unique

    def test_list_tasks(self):
        self.assertEqual(self.service.list_tasks(), [])

        task1_original = self.service.add_task("Task 1")
        tasks = self.service.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertIsNot(tasks[0], task1_original) # Ensure it's a copy of the object

        self.service.add_task("Task 2")
        tasks = self.service.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].title, "Task 2")

        # Modify the returned task's title and ensure the service's internal state is unchanged
        tasks[0].title = "Modified"
        self.assertNotEqual(self.service.list_tasks()[0].title, "Modified")
        self.assertEqual(self.service.list_tasks()[0].title, task1_original.title) # Original should be unchanged

    def test_update_task(self):
        # Add a task to update
        initial_task = self.service.add_task("Old Title", "Old Description")
        task_id = initial_task.id

        # Test updating title and description
        updated_task = self.service.update_task(task_id, title="New Title", description="New Description")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.id, task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
        self.assertFalse(updated_task.is_completed) # Status should not change

        # Verify internal state is updated
        retrieved_task = next((t for t in self.service._tasks if t.id == task_id), None)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.title, "New Title")
        self.assertEqual(retrieved_task.description, "New Description")

        # Test updating only title
        updated_task_title_only = self.service.update_task(task_id, title="New Title Only")
        self.assertEqual(updated_task_title_only.title, "New Title Only")
        self.assertEqual(updated_task_title_only.description, "New Description") # Description should remain same

        # Test updating only description
        updated_task_desc_only = self.service.update_task(task_id, description="New Description Only")
        self.assertEqual(updated_task_desc_only.title, "New Title Only") # Title should remain same
        self.assertEqual(updated_task_desc_only.description, "New Description Only")

        # Test with non-existent ID
        non_existent_id = task_id + 99
        result = self.service.update_task(non_existent_id, title="Should not update")
        self.assertIsNone(result)

        # Test that passing None for title/description doesn't change them
        updated_task_none_args = self.service.update_task(task_id, title=None, description=None)
        self.assertEqual(updated_task_none_args.title, "New Title Only")
        self.assertEqual(updated_task_none_args.description, "New Description Only")

    def test_delete_task(self):
        task1 = self.service.add_task("Task to delete 1")
        task2 = self.service.add_task("Task to keep")
        self.assertEqual(len(self.service.list_tasks()), 2)

        # Test deleting an existing task
        deleted = self.service.delete_task(task1.id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].title, "Task to keep")

        # Test deleting a non-existent task
        not_deleted = self.service.delete_task(999) # Non-existent ID
        self.assertFalse(not_deleted)
        self.assertEqual(len(self.service.list_tasks()), 1) # Count should remain 1

        # Test deleting the last remaining task
        deleted_last = self.service.delete_task(task2.id)
        self.assertTrue(deleted_last)
        self.assertEqual(len(self.service.list_tasks()), 0)

    def test_toggle_task_status(self):
        task = self.service.add_task("Task to toggle")
        self.assertFalse(task.is_completed)

        # Toggle to complete
        toggled_completed = self.service.toggle_task_status(task.id)
        self.assertTrue(toggled_completed)
        self.assertTrue(self.service.list_tasks()[0].is_completed)

        # Toggle back to incomplete
        toggled_incomplete = self.service.toggle_task_status(task.id)
        self.assertTrue(toggled_incomplete)
        self.assertFalse(self.service.list_tasks()[0].is_completed)

        # Test with non-existent ID
        result = self.service.toggle_task_status(999)
        self.assertFalse(result)





if __name__ == '__main__':
    unittest.main()