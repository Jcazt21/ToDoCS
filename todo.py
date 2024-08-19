import json

# Nombre del archivo donde se almacenan las tareas
TODO_FILE = "todo.json"
 #CommentForCommit Admin. Configuracion

# Carga las tareas desde el archivo JSON
def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, retorna una lista vacía
        return []


# Guarda las tareas en el archivo JSON
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)


# Añade una nueva tarea a la lista de tareas
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)


# Marca una tarea como completada dado su índice
def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
    else:
        print("El número de tarea ingresado no es válido.")


# Elimina una tarea de la lista dado su índice
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    else:
        print("El número de tarea ingresado no es válido.")


# Imprime todas las tareas pendientes
def print_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for index, task in enumerate(tasks):
            # Aquí se imprimiría cada tarea con su índice y estado
            status = "✓" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")


# Función principal que muestra el menú y procesa las opciones
def main():
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")
        print("6. Creditos")

        # Solicitar al usuario que ingrese una opción
        choice = input("Ingrese el número de la opción: ")
        if choice == "1":
            task = input("Ingrese la nueva tarea: ")
            add_task(task)
        elif choice == "2":
            print_tasks()
            index = int(input("Ingrese el # de la completada: ")) - 1
            mark_task_completed(index)
        elif choice == "3":
            print_tasks()
            index = int(input("Indique la que desea eliminar: ")) - 1
            delete_task(index)
        elif choice == "4":
            print_tasks()
        elif choice == "5":
            break
        elif choice == "6":
            print("Grupo A1 - Administración de la Configuración")
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    main()
