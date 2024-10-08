# PR0201: Preparación del entorno con Docker

## Pasos a seguir

### 1. Levantar el contenedor de la base de datos

Para ello, tendremos que ejecutar el siguiente comando:

``` (bash)
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=postgres --name db -v ./dataPG:/var/lib/postgresql/data postgres:14
```

Este comando creará el contenedor de la base de datos con los siguientes parámetros:

1. Usuario
2. Contraseña
3. Nombre de la base de datos
4. Nombre del contenedor
5. Volumen donde se guardará la información
6. Imagen de docker que utilizará y su versión, en nuestro caso usaremos la 14.

En caso de que no tengas la imagen de postgres, el comando la obtendrá por ti. En caso de que quieras descargarla tu primero ejecuta el siguiente comando:

``` (bash)
docker pull postgres:14
```

### 2. Levantar el contenedor de Odoo

Para ello, tendremos que ejecutar el siguiente comando:

``` (bash)
docker run -d -p 8069:8069 --name odooprod --user="root" --link db:db -v .\volumesOdoo\addons:/mnt/extra/addons -v ".\volumesOdoo\firestore:/var/lib/firestore" -v .\volumesOdoo\sessions:/var/lib/sessions -t odoo:16
```

Este comando creará el contenedor de Odoo con los siguientes parámetros:

1. Puerto en el que se escucharán las conexiones
2. Nombre del contenedor
3. Nombre del usuario, en este caso será el usuario root
4. Db que utilizará, que será el contendor que hemos creado antes
5. Volúmenes donde se guardará la información
6. Imagen de docker que utilizará y su versión, en nuestro caso usaremos la 16.

En caso de que no tengas la imagen de odoo, el comando la obtendrá por ti. En caso de que quieras descargarla tu primero ejecuta el siguiente comando:

``` (bash)
docker pull odoo:16
``` 

### 3. Levantar el contenedor de pgadmin

El comando para levantar el contenedor es el siguiente:

``` (bash)
docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=user@domain.com -e PGADMIN_DEFAULT_PASSWORD=1234 -d dpage/pgadmin4
``` 

Este comando creará el contenedor de Odoo con los siguientes parámetros:

Al ejecutarlo se creará el contenedor con los siguientes parámetros:

1. Nombre del contendor
2. Mapeará los puertos del contenedor con el host para las conexiones
3. Email predeterminado
4. Contraseña
5. Contenedor de pgadmin.

En caso de que no tengas la imagen de odoo, el comando la obtendrá por ti. En caso de que quieras descargarla tu primero ejecuta el siguiente comando:

``` (bash)
docker pull dpage/pgadmin4
``` 