def agregar_tarea(tareas, tarea, fecha_limite, completada):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Completada": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        tareaElejida = int(input('Selecione una tarea:'))
        index = tareaElejida - 1
        if index < len(lista_tareas):
            tareas.pop(index)
            print(f'La tarea a sido completada {tareaElejida}')
        else:
            print(f'No existe la tarea {tareaElejida}')

def mostrar_tarea(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")

def completar_tarea(tareas):
    if not tareas:
        print("No hay tareas")
    else:
        tareaElejida = int(input('Selecione una tarea:'))
        index = tareaElejida - 1
        if index < len(lista_tareas):
            tareas[index]["Comletada"] = True
            print(f'La tarea a sido completada {tareaElejida}')
        else:
            print(f'No existe la tarea {tareaElejida}')


if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tareas")
        print('4. Eliminar tarea')
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha limite (formato: dd/mm/yyyy): ")
            completada = False
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, completada)
        
        elif opcion == "2":
            mostrar_tarea(lista_tareas)
        
        elif opcion == "3":
            completar_tarea(lista_tareas)
        
        elif opcion == '4':
            eliminar_tarea(lista_tareas)

        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")