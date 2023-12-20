from django.contrib import admin
from .models import Usuario, Administrador, Professor


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'nome')


@admin.register(Administrador)
class AdministradorAdmin(UsuarioAdmin):
    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('bio', 'categoria')
