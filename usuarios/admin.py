from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Perfil

# Register your models here.
admin.site.register(Perfil, UserAdmin)