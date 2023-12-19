from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class CategoriaCriar(generic.CreateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')


class CategoriaListar(generic.ListView):
    model = Categoria


class CategoriaEditar(generic.UpdateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('core:categoria_listar')


class CategoriaExcluir(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
