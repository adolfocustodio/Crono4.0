from django.db import models
from usuarios.models import Usuario
from categorias.models import Categoria


class Postagem(models.Model):
    titulo = models.CharField(max_length=250)
    desc = models.TextField()
    arquivo = models.FileField(upload_to='arquivos', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
