# Boilerplate DRF

---

## Modelos:

- Usuarios (Extender del modelo de Django)

  | campo      | tipo         | constraint |
  | ---------- | ------------ | ---------- |
  | email      | VARCHAR(160) | UNIQUE     |
  | created_at | DATETIME     |            |
  | updated_at | DATETIME     |            |

## Caracteristicas:

1. Login
   - [] Creación del token de acceso (JWT | access_token - refresh_token)
2. Registro
   - [] Encriptación de contraseña (pkdpf2)
3. Recuperar Contraseña
   - [] Generar una nueva contraseña encriptada
   - [] Enviar un correo con un template (html)
4. CRUD por cada Modelo
   - [] Listado con paginación
   - [] Obtener un registro mediante el id
   - [] Creación de un registro
   - [] Actualización de un registro
   - [] Eliminar un registro (SoftDelete)
5. Decoradores
   - [] Proteger las rutas mediante autenticación
   - [] Proteger las rutas por rol
6. Documentación y validaciones
   - [] Swagger OpenAPI
7. Despliegue
   - [] Render

## PIP

```ssh
pip install Django psycopg2-binary python-decouple djangorestframework drf-yasg djangorestframework-simplejwt 

```

```zsh
pip install dj-database-url

pip install whitenoise

python manage.py collectstatic
```


## Enviroments

```py
DEBUG=True

DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```

## Documentación

- Django Users Model
  - [Extender el modelo de Usuarios](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)
- ORM
  - [Tipos de datos](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)

## Comandos

### Django

1º Crear un proyecto de Django

```sh
django-admin startproject <nombre_proyecto> .
```

2º Iniciar un proyecto de Django

```sh
python manage.py runserver
```

3º Crear super usuario

```sh
python manage.py createsuperuser
```

4º Crear una app

```sh
python manage.py startapp <nombre_app>
```

5º Crear las migraciones

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

6º Sincronizar migraciones

```sh
python manage.py migrate
```