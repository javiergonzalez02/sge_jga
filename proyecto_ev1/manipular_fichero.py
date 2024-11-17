from datetime import datetime  # Importa la clase datetime para manejar fechas y horas
from pathlib import Path      # Importa Path para manejar rutas de archivos
import pandas as pd           # Importa pandas para manipulación del csv
from config import FILE_PATH  # Importa FILE_PATH para obtener la ruta del archivo CSV

def add_tarea():
    """
    Agrega una nueva tarea al archivo CSV de tareas.
    """
    # Carga el archivo CSV existente
    df = pd.read_csv(FILE_PATH)

    while True:
        # Recoge el nombre de la tarea
        nombre = input("Nombre de la tarea: ")

        while True:
            try:
                # Solicita la prioridad de la tarea y la convierte a entero
                prioridad = int(input("Prioridad (0-10): "))
                if 0 <= prioridad <= 10:
                    break  # Sale del bucle si la prioridad es válida
                else:
                    print("La prioridad debe estar entre 0 y 10.")
            except ValueError:
                # Maneja el error si la entrada no es un entero válido
                print("La prioridad debe ser un número entero entre 0 y 10.")

        while True:
            # Solicita la fecha límite de la tarea en formato YYYY-MM-DD
            fecha_limite = input("Fecha límite (YYYY-MM-DD): ").strip()
            if validar_fecha(fecha_limite):
                break
            else:
                print("Por favor, ingresa una fecha válida dentro del rango permitido.\n")

        # Pide al usuario que compruebe si los datos introducidos son correctos, sino los vuelve a pedir
        print("\nVerifica los datos ingresados:")
        print(f"Nombre: {nombre}")
        print(f"Prioridad: {prioridad}")
        print(f"Fecha límite: {fecha_limite}")
        confirmar = input("¿Son correctos? (s/n): ")
        if confirmar.lower() == 's':
            break
        else:
            print("Ingresa los datos nuevamente.\n")

    # Establece el nuevo ID de la tarea, 1 si no existe ninguna tarea, o el último ID + 1 si ya hay tareas
    if df.empty:
        nuevo_id = 1
    else:
        nuevo_id = df['id'].max() + 1

    # Crea un diccionario con los detalles de la nueva tarea
    nueva_tarea = {
        'id': nuevo_id,
        'nombre': nombre,
        'prioridad': prioridad,
        'fecha_limite': fecha_limite,
        'completada': False  # La tarea no está completada al añadirla
    }

    # Añade la nueva tarea al final del DataFrame
    df.loc[len(df)] = nueva_tarea

    # Muestra el DataFrame actualizado
    print(df)

    # Guarda el DataFrame actualizado en el archivo CSV sin incluir el índice
    df.to_csv(FILE_PATH, index=False)
    print(f"\nTarea '{nombre}' añadida correctamente con ID {nuevo_id}.")


def validar_fecha(fecha):
    """
    Valida que la fecha esté en el formato correcto y dentro del rango permitido por pandas. (Mayor que 1677-09-21 y menor que 2262-04-11)
    """
    try:
        fecha_dt = pd.to_datetime(fecha, format='%Y-%m-%d', errors='raise')
        # Verifica el rango de años
        if fecha_dt.year < 1677 or fecha_dt.year > 2262:
            print("La fecha debe estar entre 1677-09-21 y 2262-04-11.")
            return False
        return True
    except ValueError:
        print("La fecha límite debe tener el formato YYYY-MM-DD y ser una fecha válida.")
        return False

def listar_tareas():
    """
    Lista todas las tareas almacenadas, indicando si han vencido y si han sido completadas.
    """
    file_path = Path(FILE_PATH)  # Crea un objeto Path con la ruta del archivo de tareas
    df = pd.read_csv(file_path)  # Carga el archivo en un DataFrame

    if df.empty:
        print("No hay tareas para mostrar.")
        return

    # Convierte la columna 'fecha_limite' a formato datetime, manejando errores con 'coerce'
    df['fecha_limite'] = pd.to_datetime(df['fecha_limite'], format="%Y-%m-%d", errors='coerce')

    # Obtiene la fecha actual sin la hora
    hoy = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))

    # Determina si la tarea está vencida comparando la fecha límite con la fecha actual
    df['vencida'] = df['fecha_limite'] < hoy
    # Actualiza la columna 'vencida' a 'Sí' si está vencida y no está completada, de lo contrario 'No'
    df['vencida'] = df.apply(lambda row: 'Sí' if row['vencida'] and not row['completada'] else 'No', axis=1)

    # Muestra las columnas relevantes de las tareas
    print(df[['id', 'nombre', 'prioridad', 'fecha_limite', 'completada', 'vencida']])

def marcar_completada(tarea_id):
    """
    Marca una tarea específica como completada según su ID.

    Parámetros:
    tarea_id (int): El ID de la tarea a marcar como completada.
    """
    file_path = Path(FILE_PATH)  # Crea un objeto Path para el archivo de tareas
    df = pd.read_csv(file_path)  # Carga el archivo CSV en un DataFrame

    if tarea_id not in df['id'].values:
        # Informa al usuario si el ID no existe en el DataFrame
        print(f"No se encontró una tarea con ID {tarea_id}.")
        return

    # Actualiza la columna 'completada' a True para la tarea con el ID especificado
    df.loc[df['id'] == tarea_id, 'completada'] = True
    # Guarda el DataFrame actualizado en el archivo CSV
    df.to_csv(file_path, index=False)
    print(f"Tarea con ID {tarea_id} marcada como completada.")

def eliminar_tarea(tarea_id):
    """
    Elimina una tarea específica del sistema según su ID.

    Parámetros:
    tarea_id (int): El ID de la tarea a eliminar.
    """
    file_path = Path(FILE_PATH)  # Crea un objeto Path para el archivo de tareas
    df = pd.read_csv(file_path)  # Carga el archivo CSV en un DataFrame

    if tarea_id not in df['id'].values:
        # Informa al usuario si el ID no existe en el DataFrame
        print(f"No se encontró una tarea con ID {tarea_id}.")
        return

    # Filtra el DataFrame para excluir la tarea con el ID especificado
    df = df[df['id'] != tarea_id]
    # Guarda el DataFrame actualizado en el archivo CSV
    df.to_csv(file_path, index=False)
    print(f"Tarea con ID {tarea_id} eliminada correctamente.")

def guardar_tareas(df):
    """
    Guarda el DataFrame de tareas actual en el archivo CSV.

    Parámetros:
    df (DataFrame): El DataFrame que contiene las tareas a guardar.
    """
    file_path = Path(FILE_PATH)  # Crea un objeto Path para el archivo de tareas
    df.to_csv(file_path, index=False)  # Guarda el DataFrame en el archivo CSV sin el índice
    print("Tareas guardadas correctamente.")
