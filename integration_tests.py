import unittest
from todo import load_tasks, add_task, mark_task_completed, delete_task


class IntegrationTests(unittest.TestCase):
    def test_add_task(self):
        # Prueba de integración para agregar una tarea
        add_task("Completar informe")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Completar informe")
        self.assertFalse(tasks[0]["completed"])

    def test_mark_task_completed(self):
        # Prueba de integración para marcar una tarea como completada
        add_task("Completar informe")
        tasks = load_tasks()
        mark_task_completed(0)
        tasks = load_tasks()
        self.assertTrue(tasks[0]["completed"])

    def test_delete_task(self):
        # Prueba de integración para eliminar una tarea
        add_task("Completar informe")
        tasks = load_tasks()
        delete_task(0)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
