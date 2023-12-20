from django.views import generic
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy


class UsuarioCriar(generic.CreateView):
    form_class = UsuarioForm
    model = Usuario
    success_url = reverse_lazy('usuarios:usuario_listar')


class UsuarioListar(generic.ListView):
    model = Usuario


class UsuarioEditar(generic.UpdateView):
    form_class = UsuarioForm
    model = Usuario
    success_url = reverse_lazy('usuarios:usuario_listar')


class UsuarioExcluir(generic.DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:usuario_listar')
