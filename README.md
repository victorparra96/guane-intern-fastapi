### Desarrollo de una api rest hecha con fastapi, postgres, celery

## Introduccion
Esta api nos permite hacer un crud de users, dogs, hacer llamadas a otra api para recuperar informacion, realizar tareas en segundo plano para responder al cliente de manera rapida

## Documentacion

- [FastApi](https://fastapi.tiangolo.com/ "FastApi")
- [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/ "Tortoise ORM")
- [Aerich](https://github.com/tortoise/aerich "Aerich") para el manejo de las migraciones de la base de datos

## Instalacion
- Crear el contenedor
`docker-compose build`
- Correr el contenedor
`docker-compose up`

## Rutas
Users
- http://localhost:8002/api/users -> post - crear un user
- http://localhost:8002/api/users -> get - obtener todos los users
- http://localhost:8002/api/user/{id} -> get - obtener un user por id
- http://localhost:8002/api/user/{id} -> put - actualizar un user por id
- http://localhost:8002/api/user/{id} -> delete - eliminar un user por id

Dogs
- http://localhost:8002/api/dogs -> post - crear un dog (se necesita un token)
- http://localhost:8002/api/dogs -> get - obtener todos los dogs
- http://localhost:8002/api/dogs/is_adopted -> get - obtener todos los dogs que sean adoptados
- http://localhost:8002/api/dogs/{name} -> get - obtener un dog por nombre
- http://localhost:8002/api/dogs/{name} -> put - actualizar un dog por nombre
- http://localhost:8002/api/dogs/{name} -> delete - eliminar un dog por nombre

Token
- http://localhost:8002/api/login/token -> post - enviamos el username y la contraseña del user y nos devuelve un token

Tasks
- http://localhost:8002/api/tasks/test_celery/{word} -> post - enviamos cualquier string y activamos una tarea
- http://localhost:8002/api/tasks/send_photo -> post - activamos el envio de una foto a otra api en segundo plano

## Manejo de la api
Podemos interactuar con la api desde los docs http://localhost:8002/docs o por medio de postman
Tenemos dos tablas, users y dogs. Lo primero que debemos hacer es crear un nuevo user y luego si podemos crear un nuevo dog, anexando a que user pertenece ese dog

## Migraciones

Iniciar aerich:

`docker-compose exec web aerich init -t db.TORTOISE_ORM`

Crear la primera migracion y aplicarla a la base de datos

`docker-compose exec web aerich init-db`


Crear migraciones

`docker-compose exec web aerich migrate`

`docker-compose exec web aerich upgrade`


## Verificar buenas practicas con pep8

`docker-compose exec web flake8`
