from django.contrib import admin
from .models import Usuario, Administrador, Professor


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'nome')


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'nome')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'nome', 'bio', 'categoria')
