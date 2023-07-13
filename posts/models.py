from django.db import models
from django.utils.text import slugify
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class Post(BaseModel):
    perfil = models.ForeignKey('usuarios.Perfil', on_delete=models.PROTECT)

    titulo = models.CharField(max_length=255)
    head_image = models.ImageField(upload_to='fotos')
    post = RichTextField()

    crear = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    
    class Meta():
        ordering = ('titulo',)

    def __str__(self) -> str:
        return f'{self.titulo}'
    