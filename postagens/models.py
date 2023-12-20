from django.db import models
from usuarios.models import Usuario
from categorias.models import Categoria


class Postagem(models.Model):
    titulo = models.CharField(max_length=250)
    desc = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
