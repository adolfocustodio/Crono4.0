from django.views import generic
from .models import Postagem
from .forms import PostagemForm
from django.urls import reverse_lazy


class PostagemCriar(generic.CreateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')


class PostagemListar(generic.ListView):
    model = Postagem


class PostagemEditar(generic.UpdateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')


class PostagemExcluir(generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')
