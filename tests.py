import unittest
from unittest.mock import patch, Mock
import todo
from datetime import datetime, timedelta


class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Esta función se ejecuta antes de cada prueba
        self.initial_tasks = todo.load_tasks()

    def tearDown(self):
        # Esta función se ejecuta después de cada prueba
        # Restaurar las tareas originales después de cada prueba
        todo.save_tasks(self.initial_tasks)

    def test_load_tasks(self):
        tasks = todo.load_tasks()
        self.assertIsInstance(tasks, list, "La carga de tareas no devolvió una lista")

    def test_add_task(self):
        initial_tasks = todo.load_tasks()
        todo.add_task("Nueva tarea")
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), len(initial_tasks) + 1, "La tarea no fue añadida correctamente")
        self.assertEqual(tasks[-1]["task"], "Nueva tarea", "El título de la tarea añadida no coincide")
        self.assertFalse(tasks[-1]["completed"], "La nueva tarea debería estar incompleta")

    def test_mark_task_completed(self):
        todo.add_task("Tarea por marcar")
        tasks = todo.load_tasks()
        index = len(tasks) - 1
        todo.mark_task_completed(index)
        updated_tasks = todo.load_tasks()
        self.assertTrue(updated_tasks[index]["completed"], "La tarea no fue marcada como completada")

    def test_delete_task(self):
        todo.add_task("Tarea a eliminar")
        initial_tasks = todo.load_tasks()
        index = len(initial_tasks) - 1
        todo.delete_task(index)
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), len(initial_tasks) - 1, "La tarea no fue eliminada correctamente")

    def test_add_task_with_past_due_date(self):
        # Prueba para agregar una tarea con fecha de vencimiento pasada
        past_date = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError) as context:
            todo.add_task("Tarea con fecha pasada", due_date=past_date)
        self.assertEqual(str(context.exception), "La fecha de vencimiento no puede ser en el pasado.")

    def test_edit_task_title_only(self):
        # Prueba para editar solo el título de una tarea existente
        todo.add_task("Tarea original")
        tasks = todo.load_tasks()
        index = len(tasks) - 1
        todo.edit_task(index, title="Nuevo título")
        updated_tasks = todo.load_tasks()
        self.assertEqual(updated_tasks[index]["task"], "Nuevo título", "El título de la tarea no se actualizó correctamente")
        self.assertEqual(updated_tasks[index]["due_date"], tasks[index]["due_date"], "La fecha de vencimiento debería permanecer sin cambios")
        self.assertEqual(updated_tasks[index]["completed"], tasks[index]["completed"], "El estado de completado debería permanecer sin cambios")

    def test_edit_task_title_only_equivalence_partitioning(self):
        # Prueba adicional para editar solo el título de una tarea existente (Particionamiento de Equivalencia)
        todo.add_task("Otra tarea original")
        tasks = todo.load_tasks()
        index = len(tasks) - 1
        todo.edit_task(index, title="Título modificado")
        updated_tasks = todo.load_tasks()
        self.assertEqual(updated_tasks[index]["task"], "Título modificado", "El título de la tarea no se actualizó correctamente")
        self.assertEqual(updated_tasks[index]["due_date"], tasks[index]["due_date"], "La fecha de vencimiento debería permanecer sin cambios")
        self.assertEqual(updated_tasks[index]["completed"], tasks[index]["completed"], "El estado de completado debería permanecer sin cambios")


if __name__ == "__main__":
    unittest.main()
