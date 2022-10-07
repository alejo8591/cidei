 ## Ejemplo shapes en PostgreSQL, postGIS y QGIS
### PostgreSQL y PostGIS
```
docker run --name=postgis -d -e POSTGRES_USER=fullstacksedic -e POSTGRES_PASS=fullstacksedic -e POSTGRES_DBNAME=lab3 -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v pg_data:/lab3 --restart=always kartoza/postgis 
```
#### Que información tiene este comando:

* `docker run --name=postgis` le dice a Docker que nuestro nuevo contenedor se llamará `postgis`
* `-d` ejecuta el contenedor en segundo plano (modo separado)
* `-e POSTGRES_USER=fullstacksedic` el flag `-e` establece una variable de entorno dentro del contenedor. Este se usa para configurar el nombre de un rol de inicio de sesión en PostgreSQL que tendrá privilegios de superusuario (admin) en la base de datos.
* `-e POSTGRES_PASS=fullstacksedic` establece una variable de entorno que establecerá la contraseña de la función de inicio de sesión en ese caso `fullstacksedic`.
* `-e POSTGRES_DBNAME=lab1` variable de entorno que le dice al contenedor que cree una nueva base de datos en el servidor con el nombre `lab1`. Después de crear la base de datos, se habilitará la extensión PostGIS.
* `-e ALLOW_IP_RANGE=0.0.0.0/0` le dice al contenedor que configure PostgreSQL para aceptar conexiones de cualquier persona. Si no configuró esto, la base de datos solo aceptará conexiones de direcciones que utilizan la subred de red de Docker.
* `-p 5432:5432` asigna el puerto `5432` en la máquina virtual host al puerto `5432` en el contenedor. Esto es necesario porque el servidor de bases de datos escucha las conexiones en el puerto `5432` de manera predeterminada.
* `-v pg_data:/Users/alejandroromero/Documents/fullstacksedic/lab1 o pg_data:/lab1` le dice al sistema de archivos contenedor que monte el volumen `pg_data` que acabamos de crear en la ruta `/lab1`. Esto significa que cualquier dato que el contenedor guarde o cree en ese directorio se guardará en el volumen `pg_data`.
* `--restart=always` crea una política de reinicio para su contenedor. Ahora su contenedor se iniciará cada vez que se inicie la máquina virtual Docker. Si no se configuró, tendría que iniciar manualmente el contenedor cada vez que la VM se iniciara con `docker start postgis`
* `kartoza/postgis` le dice a Docker que extraiga el repositorio `kartoza/postgis` de Docker Hub, usando PostgreSQL y PostGIS.

#### Verificar que esta arriba el contenedor:
```
docker container ls
```
Debe mostar es algo así:
```
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                    NAMES
4fcf7beb60e4   kartoza/postgis   "/bin/sh -c /scripts…"   2 minutes ago   Up 2 minutes   0.0.0.0:5432->5432/tcp   postgis
```
#### Verificar que esta arriba el volumen
```
docker volume ls
```
Debe mostar es algo así:
```
DRIVER              VOLUME NAME
local               pg_data
```

### Conectar y configurar `lab1` con PgAdmin

#### Opción config server con pgAdmin
![acceder pgAdmin](./img/captura_1.png)

#### config name para la identificación de la conexión 
![acceder pgAdmin](./img/captura_2.png)

#### config host y datos de conexión indicados en los primeros pasos 
![acceder pgAdmin](./img/captura_3.png)

#### lista de DBs en `lab1`
![acceder pgAdmin](./img/captura_4.png)

#### lista de schemas en `lab1`
![acceder pgAdmin](./img/captura_5.png)

#### verificando `PostGIS` en `lab1`
![acceder pgAdmin](./img/captura_6.png)
