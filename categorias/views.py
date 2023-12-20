from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.permissions import AdministradorPermission
from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class CategoriaCriar(LoginRequiredMixin, AdministradorPermission, generic.CreateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')


class CategoriaListar(LoginRequiredMixin, AdministradorPermission, generic.ListView):
    model = Categoria


class CategoriaEditar(LoginRequiredMixin, AdministradorPermission, generic.UpdateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')


class CategoriaExcluir(LoginRequiredMixin, AdministradorPermission, generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
