import unittest
from unittest.mock import patch
import todo


class TestTodoApp(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "Tarea de prueba", "4", "5"])
    def test_todo_app(self, mock_input):
        todo.main()

    def test_load_tasks(self):
        tasks = todo.load_tasks()
        self.assertIsInstance(tasks, list)

    def test_add_task(self):
        initial_tasks = todo.load_tasks()
        todo.add_task("Nueva tarea")
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), len(initial_tasks) + 1)
        self.assertEqual(tasks[-1]["task"], "Nueva tarea")
        self.assertFalse(tasks[-1]["completed"])

    def test_mark_task_completed(self):
        todo.add_task("Tarea por marcar")
        tasks = todo.load_tasks()
        index = len(tasks) - 1
        todo.mark_task_completed(index)
        updated_tasks = todo.load_tasks()
        self.assertTrue(updated_tasks[index]["completed"])

    def test_delete_task(self):
        todo.add_task("Tarea a eliminar")
        initial_tasks = todo.load_tasks()
        index = len(initial_tasks) - 1
        todo.delete_task(index)
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), len(initial_tasks) - 1)


if __name__ == "__main__":
    unittest.main()
