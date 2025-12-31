import unittest
from typer.testing import CliRunner
from src.todo.cli import app

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_add_task_command(self):
        # Test with description
        result_desc = self.runner.invoke(app, ["add", "Read a book", "--description", "Sci-fi novel"])
        self.assertEqual(result_desc.exit_code, 0)
        self.assertIn("Task 'Read a book' added with ID", result_desc.stdout)
        self.assertIn("Description: Sci-fi novel", result_desc.stdout)
        
        # Test with minimum required fields
        result = self.runner.invoke(app, ["add", "Buy groceries"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Task 'Buy groceries' added with ID", result.stdout)
        
        # Test with empty title (should fail)
        result_empty = self.runner.invoke(app, ["add", ""])
        self.assertNotEqual(result_empty.exit_code, 0)
        self.assertIn("Error: Title cannot be empty.", result_empty.stderr)

        # Test with missing title (should fail)
        result_missing = self.runner.invoke(app, ["add"])
        self.assertNotEqual(result_missing.exit_code, 0)
        self.assertIn("Error: Missing argument 'TITLE'", result_missing.stderr)
        self.assertIn("Usage:", result_missing.stderr)

    def test_list_tasks_command(self):
        # Add some tasks first
        self.runner.invoke(app, ["add", "Task 1"])
        self.runner.invoke(app, ["add", "Task 2", "-d", "Description 2"])

        result = self.runner.invoke(app, ["list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("[ ] 1: Task 1", result.stdout)
        self.assertIn("[ ] 2: Task 2 (Description 2)", result.stdout)

        # Test empty list (after clearing for example, which is not implemented yet)

    def test_update_task_command(self):
        self.runner.invoke(app, ["add", "Original Task"])
        task_id = 1 # Assuming first task gets ID 1

        result = self.runner.invoke(app, ["update", str(task_id), "-t", "Updated Task", "-d", "New Description"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"Task {task_id} updated.", result.stdout)

        # Verify change through list command
        list_result = self.runner.invoke(app, ["list"])
        self.assertIn(f"{task_id}: Updated Task (New Description)", list_result.stdout)

        # Test non-existent ID
        result_fail = self.runner.invoke(app, ["update", "999", "-t", "Non Existent"])
        self.assertNotEqual(result_fail.exit_code, 0)
        self.assertIn("Error: Task with ID 999 not found.", result_fail.stderr)

    def test_delete_task_command(self):
        self.runner.invoke(app, ["add", "Task to delete"])
        task_id = 1 # Assuming first task gets ID 1

        result = self.runner.invoke(app, ["delete", str(task_id)])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f"Task {task_id} deleted.", result.stdout)

        # Verify deletion
        list_result = self.runner.invoke(app, ["list"])
        self.assertNotIn(f"{task_id}: Task to delete", list_result.stdout)

        # Test non-existent ID
        result_fail = self.runner.invoke(app, ["delete", "999"])
        self.assertNotEqual(result_fail.exit_code, 0)
        self.assertIn("Error: Task with ID 999 not found.", result_fail.stderr)

    def test_toggle_task_status_command(self):
        self.runner.invoke(app, ["add", "Toggle Me"])
        task_id = 1

        # Check initial state
        list_initial = self.runner.invoke(app, ["list"])
        self.assertIn(f"[ ] {task_id}: Toggle Me", list_initial.stdout)

        # Toggle to complete
        result_toggle = self.runner.invoke(app, ["toggle", str(task_id)])
        self.assertEqual(result_toggle.exit_code, 0)
        self.assertIn(f"Task {task_id} status toggled.", result_toggle.stdout)

        list_completed = self.runner.invoke(app, ["list"])
        self.assertIn(f"[x] {task_id}: Toggle Me", list_completed.stdout)

        # Toggle back to incomplete
        result_toggle_back = self.runner.invoke(app, ["toggle", str(task_id)])
        self.assertEqual(result_toggle_back.exit_code, 0)
        self.assertIn(f"Task {task_id} status toggled.", result_toggle_back.stdout)

        list_incomplete = self.runner.invoke(app, ["list"])
        self.assertIn(f"[ ] {task_id}: Toggle Me", list_incomplete.stdout)

        # Test non-existent ID
        result_fail = self.runner.invoke(app, ["toggle", "999"])
        self.assertNotEqual(result_fail.exit_code, 0)
        self.assertIn("Error: Task with ID 999 not found.", result_fail.stderr)
