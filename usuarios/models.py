from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Perfil(AbstractUser):

    website = models.URLField(max_length=200, blank=True)

    foto = models.ImageField(
        upload_to=('usuarios/img'),
        blank=True,
        null=True,
    )

    fecha_modificacion = models.DateTimeField(auto_now=True)
