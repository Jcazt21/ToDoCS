import json

TODO_FILE = "todo.json"


def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Tarea '{task}' agregada con éxito.")


def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Tarea '{tasks[index]['task']}' marcada como completada.")
    else:
        print("El número de tarea ingresado no es válido.")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tarea '{deleted_task['task']}' eliminada con éxito.")
    else:
        print("El número de tarea ingresado no es válido.")


def print_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for index, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")


def edit_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        old_task = tasks[index]["task"]
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print(f"Tarea '{old_task}' actualizada a '{new_task}'.")
    else:
        print("El número de tarea ingresado no es válido.")


def handle_user_choice(choice):
    if choice == "1":
        task = input("Ingrese la nueva tarea: ")
        add_task(task)
    elif choice == "2":
        print_tasks()
        try:
            index = int(input("Ingrese el número de la tarea completada: ")) - 1
            mark_task_completed(index)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif choice == "3":
        print_tasks()
        try:
            index = int(input("Indique el número de la tarea a eliminar: ")) - 1
            delete_task(index)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif choice == "4":
        print_tasks()
    elif choice == "5":
        print_tasks()
        try:
            index = int(input("Ingrese el número de la tarea a editar: ")) - 1
            new_task = input("Ingrese la nueva descripción de la tarea: ")
            edit_task(index, new_task)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif choice == "6":
        print("Grupo 3 - Construcción de Software")
    elif choice == "7":
        print("Hasta luego.")
        return False
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 7.")
    return True


def main():
    options = {
        "1": "Agregar tarea",
        "2": "Marcar tarea como completada",
        "3": "Eliminar tarea",
        "4": "Mostrar tareas",
        "5": "Editar tarea",
        "6": "Créditos",
        "7": "Salir"
    }
    
    while True:
        print("\n¿Qué desea hacer?")
        for key, value in options.items():
            print(f"{key}. {value}")

        choice = input("Ingrese el número de la opción: ")
        if not handle_user_choice(choice):
            break


if __name__ == "__main__":
    main()
