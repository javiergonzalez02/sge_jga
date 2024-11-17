# PROYECTO PRIMERA EVALUACIÓN - SISTEMA DE GESTIÓN DE TAREAS PENDIENTES

## ÍNDICE

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Archivo `main.py`](#archivo-mainpy)
3. [Archivo `init_fichero.py`](#archivo-init_ficheropy)
4. [Archivo `manipular_fichero.py`](#archivo-manipular_ficheropy)
5. [Archivo `config.py`](#archivo-configpy)

---

## Estructura del Proyecto

El proyecto permite al usuario crear tareas, verlas, eliminarlas y marcarlas como completadas:

- **`main.py`**: Es la parte principal del programa, donde se encuentra el menú de opciones.
- **`init_fichero.py`**: Crea y configura el archivo CSV que almacena las tareas.
- **`manipular_fichero.py`**: Contiene funciones para manipular las tareas: añadir, listar, marcar como completada y eliminar.
- **`config.py`**: Contiene la constante de la localización del archivo, por lo que solo hace falta cambiar la localización en un solo lugar.

---

## Archivo `main.py`

Es el archivo con el que el usuario interactúa. Contiene el menú de usuario y llama a las funciones correspondientes dependiendo de la opción seleccionada.

### Función `main()`

```python
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
```
---

## Archivo `init_fichero.py`

Este archivo se encarga de la configuración inicial del archivo CSV donde se guardan las tareas. Asegura que el archivo existe y tiene las columnas correctas.

``` python
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


def cargar_tareas():
    """
    Carga las tareas desde el archivo CSV.
    """
    file_path = Path("archivo.csv")
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Archivo no encontrado. Creando un nuevo archivo.")
        crear_file(file_path)
        return pd.DataFrame(columns=['id', 'nombre', 'prioridad', 'fecha_limite', 'completada'])
```
---

## Archivo `manipular_fichero.py`

```python
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

```
---

## Archivo `config.py`

Contiene la constante de la localización del CSV. Ahorra tiempo en caso de que se quiera cambiar la ubicación y evita posibles errores de inconsistencia.

```python
FILE_PATH = './archivo.csv'
```
