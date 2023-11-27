# API RENTAL CAR

El proyecto permite gestionar las rentas de vehículos en una compañia de renta de vehículos.

## Requerimientos del Proyecto

1. Login
   - [x] Creación del token de acceso (JWT | access_token - refresh_token)
2. Registro
   - [x] Encriptación de contraseña (pkdpf2)
3. Recuperar Contraseña
   - [x] Generar una nueva contraseña encriptada
   - [x] Enviar un correo con un template (html)
4. CRUD por cada Modelo
   - [x] Listado con paginación
   - [x] Obtener un registro mediante el id
   - [x] Creación de un registro
   - [x] Actualización de un registro
   - [x] Eliminar un registro (SoftDelete)
5. Decoradores
   - [x] Proteger las rutas mediante autenticación
6. Documentación y validaciones
   - [x] Swagger OpenAPI
7. Despliegue
   - [x] Render

## Modelos:

- Users (Extender del modelo de Django)

  | campo      | tipo         | constraint |
  | ---------- | ------------ | ---------- |
  | email      | VARCHAR(160) | UNIQUE     |
  | first_name | VARCHAR(150) |            |
  | last_name  | VARCHAR(150) |            |
  | password   | VARCHAR(150) |            |
  | created_at | DATETIME     |            |
  | updated_at | DATETIME     |            |

- Vehicles
  | campo      | tipo         |  constraint |
  | ---------- | ------------ | ----------- |
  | car_make   | VARCHAR(100) |             |
  | model      | VARCHAR(100) |             |
  | plate_num  | VARCHAR(150) |             |
  | password   | VARCHAR(12)  | UNIQUE      |
  | price_day  | FLOAT        |             |
  | condition  | VARCHAR(8)   |             |

- Rents
  | campo      | tipo         |  constraint |
  | ---------- | ------------ | ----------- |
  | date_start | DATETIME     |             |
  | date_end   | DATETIME     |             |
  | total_pay  | FLOAT        |             |
  | userId     | INTEGER      |             |
  | vehicleId  | FLOAT        |             |

## Arquitectura
Modelo Vista Template

## Tecnologías a utilizar
* **Database:** PostgreSQL
* **Backend:** Django Rest Framework
* **Frontend:** React
* **Documentation:** Swagger
* **Despliegue:** Para el backend se utilizará Render, y para el Frontend se utilizará Vercel.

# Comensando
Para que la api funcione correctamente se deve tener en cuenta las variable del archivo .env, y cambiarlas según sus necesidades.

```py
DEBUG=...

# Considerar para un funcionamiento a nivel local
DB_NAME='...'
DB_USER='....'
DB_PASSWORD='...'
DB_HOST='....'
DB_PORT=...

ALLOWED_HOSTS = '.....'

#Considerar para un funcionamiento online
DATABASE_URL = '......'


MAIL_SERVER = '.......'
MAIL_PORT = '......'
MAIL_USE_TLS = '....'
MAIL_USERNAME = '.....'
MAIL_PASSWORD = '....'
```

### Prerequisitos

Es necesario instalar todas las dependencia del archivo requirements.txt

#### PIP

```sh
pip install Django psycopg2-binary python-decouple djangorestframework drf-yasg djangorestframework-simplejwt

```

```zsh
pip install dj-database-url

pip install whitenoise

python manage.py collectstatic
```

- **Configura CORS en el Servidor Django**

```zsh
pip install django-cors-headers
```

#### Django

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

---

### Django

1º Crear un proyecto de Django

```sh
django-admin startproject <nombre_proyecto> .
```

2º Iniciar un proyecto de Django

```sh
python manage.py runserver
```

- Rents

## Documentación

- Django Users Model
  - [Extender el modelo de Usuarios](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)
- ORM
  - [Tipos de datos](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)
- Relaciones entre serializadores
  - [Documentación de relación entre serialziadores](https://www.django-rest-framework.org/api-guide/relations/)
- Vistas genéricas -[GenericApiView](https://www.django-rest-framework.org/api-guide/generic-views/)

### Notas

- PWA aplicaciones híbridas
- Session Storage, Local Storage, Private State Tokens,
- 