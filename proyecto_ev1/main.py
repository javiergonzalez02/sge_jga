from init_fichero import iniciar_archivo  # Importa la función para inicializar el archivo
from manipular_fichero import add_tarea, listar_tareas, marcar_completada, eliminar_tarea  # Importa las funciones de manejo de tareas


def main():
    """
    Función principal que controla el flujo de la aplicación de Gestión de Tareas.
    """
    # Inicializa el archivo de tareas (crea el archivo si no existe)
    iniciar_archivo()

    # Bucle que mantiene en ejecución el programa hasta que el usuario decida salir
    while True:
        # Muestra el menú de opciones al usuario
        print("\nGestión de Tareas")
        print("1. Añadir Tarea")
        print("2. Listar Tareas")
        print("3. Marcar Tarea como Completada")
        print("4. Eliminar Tarea")
        print("5. Salir")

        # Solicita al usuario que seleccione una opción del menú
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Llama a la función para añadir una tarea
            add_tarea()

        elif opcion == '2':
            # Llama a la función para listar las tareas existentes
            listar_tareas()

        elif opcion == '3':
            # Solicita al usuario el ID de la tarea a marcar como completada
            try:
                tarea_id = int(input("ID de la tarea a marcar como completada: "))
                marcar_completada(tarea_id)
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == '4':
            # Solicita al usuario el ID de la tarea a eliminar
            try:
                tarea_id = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(tarea_id)
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")


if __name__ == "__main__":
    main()
