from django.urls import path
from .views import PostagemCriar, PostagemListar, PostagemEditar, PostagemExcluir

app_name = 'postagens'
urlpatterns = [
    path('criar/', PostagemCriar.as_view(), name='postagem_criar'),
    path('listar/', PostagemListar.as_view(), name='postagem_listar'),
    path('<int:pk>/editar/', PostagemEditar.as_view(), name='postagem_editar'),
    path('<int:pk>/excluir/', PostagemExcluir.as_view(), name='postagem_excluir')
]
