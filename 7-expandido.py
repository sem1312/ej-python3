tareas = []

def agregar_tarea():
    tarea = {"Descripcion": input("Descripcion: "),
             "Fecha limite": input("Fecha limite (dd/mm/aaaa): "),
             "Prioridad": input("Prioridad: "), "Completada": False}
    tareas.append(tarea)
    print("Tarea agregada.")

def mostrar_tareas(completadas):
  if(completadas == True): 
    print("\nLista de tareas completadas:")
    for i, tarea in enumerate(tareas, start=1):
      if(tarea["Completada"] == True):  
        print(f"Tarea {i}: {tarea}")
  elif(completadas == False):
    print("\nLista de tareas no completadas:")
    for i, tarea in enumerate(tareas, start=1):
      if(tarea["Completada"] == False):  
        print(f"Tarea {i}: {tarea}")
  else:
    print("\nLista total de taras:")
    for i, tarea in enumerate(tareas, start=1):
      print(f"Tarea {i}: {tarea}")

def marca_completada(tareas):
  i = int(input("Que indice de tarea queres marcar como completada? "))
  if(i < len(tareas)):
    tareas[i]["Completada"] = True
    print("Tarea marcada como completada")
  else:
    print("No se pudo marcar la tarea")

while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Mostrar lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas(True)
    elif opcion == "3":
        marca_completada(tareas)
    elif opcion == "4":
        print("chau")
        break
    else:
        print("Opcion invalida.")
