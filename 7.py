tareas = []

def agregar_tarea():
    tarea = {"Descripcion": input("Descripcion: "),
             "Fecha limite": input("Fecha limite (dd/mm/aaaa): "),
             "Prioridad": input("Prioridad: ")}
    tareas.append(tarea)
    print("Tarea agregada.")

def mostrar_tareas():
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"Tarea {i}: {tarea}")

while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Mostrar lista de tareas")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        print("chau")
        break
    else:
        print("Opcion invalida.")
