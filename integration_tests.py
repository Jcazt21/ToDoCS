import unittest
import os
import todo

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        # Limpiar el archivo todo.json antes de cada prueba
        with open(todo.TODO_FILE, "w") as file:
            file.write("[]")

    def tearDown(self):
        # Limpiar el archivo todo.json después de cada prueba
        os.remove(todo.TODO_FILE)

    def test_add_task(self):
        todo.add_task("Tarea de prueba")
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), 1)

    def test_mark_task_completed(self):
        todo.add_task("Tarea de prueba")
        todo.mark_task_completed(0)
        tasks = todo.load_tasks()
        self.assertTrue(tasks[0]["completed"])

    def test_delete_task(self):
        todo.add_task("Tarea de prueba")
        todo.delete_task(0)
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
