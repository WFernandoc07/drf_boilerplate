from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Sobre escribir campos ya existentes
    email = models.EmailField(unique=True)

    # Crear nuevos campos
    # auto_now_add -> inserta la fecha y hora actual, solo en la creación
    # auto_now -> Inserta la fecha y hora actual en cada actualización
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Modificar el nombre de la tabla 'auth_users
        db_table = 'users'
    
    # Métodos únicos en la clase heredada

    # Menciona los campos a validar(requeridos) para la creación
    # desde el UserManager (SuperUser)
    REQUIRED_FIELDS = ['email', 'password']

    # Método instancia (heredado)
    def create_user(self, **kwargs):
        # {'username':'username'}
        # username=kgargs['username]
        record = self.model(**kwargs)
        record.set_password(kwargs['password'])
        record.save()
        return record
