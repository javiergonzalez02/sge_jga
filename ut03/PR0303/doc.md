docker-compose exec -ti db bash

service postgresql stop

pg_dump -U user postgres > backup.sql

postgresql start

docker cp db:/root/backup.sql D:\Users\Alumno\ODOO