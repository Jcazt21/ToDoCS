import unittest
from datetime import datetime, timedelta
import todo

class TestTodoAppTC01(unittest.TestCase):
    def setUp(self):
        self.initial_tasks = todo.load_tasks()

    def tearDown(self):
        todo.save_tasks(self.initial_tasks)

    def test_add_task_with_past_due_date(self):
        # Prueba para agregar una tarea con fecha de vencimiento pasada
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError) as context:
            todo.add_task("Tarea con fecha pasada", due_date=past_date)
        self.assertEqual(str(context.exception), "La fecha de vencimiento no puede ser en el pasado.")

if __name__ == "__main__":
    unittest.main()
