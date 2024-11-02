## Integración de Servicios Externos

## Ejercicio 1

### Pasos a seguir

(Se dará por hecho que el nombre del contenedor de la base de datos es `db`, sino se debe seguir el siguiente tutorial cambiando el nombre del contenedor por el que corresponda)

1. **Crear la copia de seguridad con `pg_dump`:**
    - Conéctate al contenedor de la base de datos:
      ```bash
      docker compose exec db bash
      ```
    - Parar el servicio de postgres:
      ```bash
      service postgresql stop
      ```
    - Dentro del contenedor crea la copia de seguridad:
      ```bash
      pg_dump -U odoo odoo > backup.sql
      ```
    - Volver a iniciar el servicio de postgres:
      ```bash
        service postgresql start
        ```
    - Sal del contenedor:
      ```bash
      exit
      ```
    - Apaga el contenedor
   
2. **Copiar el archivo de copia de seguridad a la máquina anfitriona:**
    - Usa el siguiente comando cambiando ruta por la ruta donde quieras guardar el archivo:
    ```bash
    docker compose cp db:./backup.sql ./ruta/backup.sql
    ```
    - 

3. **Eliminar los contenedores y limpiar los directorios mapeados:**
    ```bash
    docker compose down
    sudo rm -rf dataPG/* sessions/* filestore/* addons/*
    ```

4. **Recrear los contenedores:**
    ```bash
    docker compose up -d
    ```
    - Verifica que el servidor no tiene datos accediendo a `http://localhost:8069`.

5. **Restaurar la base de datos desde la copia de seguridad:**
    - Entra al contenedor de la base de datos:
      ```bash
      docker compose exec db bash
      ```
    - Crea una nueva base de datos vacía:
      ```bash
      createdb -U odoo -O odoo odoo
      ```
    - Sal del contenedor y copia el archivo de respaldo de vuelta al contenedor:
      ```bash
      docker cp ./backup.sql <ID_CONTENEDOR>:/
      ```
    - Vuelve a entrar y restaura la copia de seguridad:
      ```bash
      psql -U odoo -d odoo < ./backup.sql
      ```
    - Sal del contenedor:
      ```bash
      exit
      ```

6. **Verificar la restauración:**
    - Accede a Odoo en tu navegador en `http://localhost:8069` y verifica que los datos han sido restaurados correctamente.

---

## Ejercicio 2

### Pasos a seguir

1. **Lo primero es ir a esta [pagina](http://localhost:8069/web/database/manager)**
2. **Una vez dentro, debemos introducir el nombre de la base de datos que queremos guardar y pulsar el botón backup:**
    - Introduciremos la contraseña maestra de Odoo.
    - Y el tipo de copia de seguridad que queremos hacer. En nuestro caso .zip incluyendo el filestore.
    - Pulsamos el botón backup y esperamos a que termine.
3. **Una vez terminado, nos descargará un archivo .zip que contendrá la copia de seguridad de la base de datos.**
4. **De nuevo, eliminamos los contenedores y limpiamos los directorios mapeados:**
    ```bash
    docker compose down
    sudo rm -rf dataPG/* sessions/* filestore/* addons/*
    ```
5. **Recreamos los contenedores:**
    ```bash
    docker compose up -d
    ```
6. **Volvemos a la [pagina de gestión de bases de datos](http://localhost:8069/web/database/manager) y pulsamos el botón 'Restore Database'**
7. **Se nos abrirá un menú y seleccionamos el archivo .zip que hemos descargado anteriormente, introducimos el nombre de la db y la contraseña.**
8. **Pulsamos el botón 'Continue' y esperamos a que termine.**
9. **Una vez terminado, accedemos a la base de datos y comprobamos que los datos han sido restaurados correctamente.**