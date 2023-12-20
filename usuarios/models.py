from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from categorias.models import Categoria


class Usuario(AbstractUser):
    nome = models.CharField(max_length=250)
    first_name = None
    last_name = None


class Administrador(Usuario):

    def save(self, *args, **kwargs):
        super(Administrador, self).save(*args, **kwargs)
        grupo, _ = Group.objects.get_or_create(name='Administradores')
        self.groups.add(grupo)


class Professor(Usuario):
    bio = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Professor, self).save(*args, **kwargs)
        grupo, _ = Group.objects.get_or_create(name='Professores')
        self.groups.add(grupo)
