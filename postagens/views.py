from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.permissions import AdministradorPermission, ProfessorPermission
from django.views import generic
from .models import Postagem
from .forms import PostagemForm
from django.urls import reverse_lazy


class PostagemCriar(LoginRequiredMixin, AdministradorPermission, ProfessorPermission, generic.CreateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('core:inicio')


class PostagemListar(LoginRequiredMixin, AdministradorPermission, generic.ListView):
    model = Postagem


class PostagemEditar(LoginRequiredMixin, AdministradorPermission, generic.UpdateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')


class PostagemExcluir(LoginRequiredMixin, AdministradorPermission, generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')
