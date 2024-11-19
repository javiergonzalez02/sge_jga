from pathlib import Path  # Importa Path para manejar rutas de archivos
import pandas as pd  # Importa pandas para manipulación del csv
from config import FILE_PATH  # Importa FILE_PATH para obtener la ruta del archivo CSV


def check_if_exists(file_to_check):
    """
    Verifica si un archivo existe y si es un archivo.
    """
    if file_to_check.exists():
        if file_to_check.is_file():
            print(f"El archivo {file_to_check} existe")
            return True
        else:
            print(f"{file_to_check} no es un archivo")
            return False
    else:
        print(f"El archivo {file_to_check} no existe")
        return False


def crear_file(file_to_create):
    """
    Crea un archivo CSV con las columnas necesarias para almacenar tareas.
    """
    try:
        # Crea un DataFrame vacío con las columnas especificadas
        df = pd.DataFrame(columns=['id', 'nombre', 'prioridad', 'fecha_limite', 'completada'])
        # Guarda el DataFrame en un archivo CSV sin incluir el índice
        df.to_csv(file_to_create, index=False)
        print(f"El archivo {file_to_create} se ha creado con las columnas necesarias")
    except FileNotFoundError:
        print(f"No se ha podido crear el archivo {file_to_create}")
    except IOError:
        print("Unn error ocurrió mientras se leía/escribía el archivo")


def iniciar_archivo():
    """
    Inicializa el archivo de tareas verificando su existencia, creando columnas si es necesario
    y ordenando las columnas en el orden correcto.
    """
    # Crea un objeto Path con la ruta del archivo
    file_to_create = Path(FILE_PATH)
    if not check_if_exists(file_to_create):
        # Crea el archivo si no existe
        crear_file(file_to_create)
    if not comprobar_columnas(file_to_create):
        # Añade columnas que falten
        crear_columnas(file_to_create)
    # Ordena las columnas correctamente
    ordenar_columnas(file_to_create)


def comprobar_columnas(file_path):
    """
    Comprueba si el csv contiene las columnas necesarias.
    """
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        print(f"El archivo {file_path} está vacío.")
        return False
    exists = all(col in df.columns for col in ['id', 'nombre', 'prioridad', 'fecha_limite', 'completada'])
    return exists


def crear_columnas(file_path):
    """
    Añade columnas que falten al csv.
    """
    try:
        df = pd.read_csv(file_path)
        updated = False
        if 'id' not in df.columns:
            df['id'] = pd.Series(dtype='int')
            updated = True
        if 'nombre' not in df:
            df['nombre'] = ''
            updated = True
        if 'prioridad' not in df:
            df['prioridad'] = ''
            updated = True
        if 'fecha_limite' not in df:
            df['fecha_limite'] = ''
            updated = True
        if 'completada' not in df:
            df['completada'] = False
            updated = True
        if updated:
            df.to_csv(file_path, index=False)
    except pd.errors.EmptyDataError:
        print(f"El archivo {file_path} está vacío. Añadiendo columnas...")
        # En caso de que el archivo esté vacío, se crean las columnas necesarias
        df = pd.DataFrame(columns=['id', 'nombre', 'prioridad', 'fecha_limite', 'completada'])
        df.to_csv(file_path, index=False)


def ordenar_columnas(file_path):
    """
    Ordena las columnas del csv en el orden correcto.
    """
    df = pd.read_csv(file_path)
    df.reindex(['id', 'nombre', 'prioridad', 'fecha_limite', 'completada'])
    df.to_csv(file_path, index=False)
