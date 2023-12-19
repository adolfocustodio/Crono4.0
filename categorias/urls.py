from django.urls import path
from .views import CategoriaCriar, CategoriaListar, CategoriaEditar, CategoriaExcluir


app_name = 'categorias'
urlpatterns = [
    path('criar/', CategoriaCriar.as_view(), name='categoria_criar'),
    path('listar/', CategoriaListar.as_view(), name='categoria_listar'),
    path('<int:pk>/editar/', CategoriaEditar.as_view(), name='categoria_editar'),
    path('<int:pk>/excluir/', CategoriaExcluir.as_view(), name='categoria_excluir')
]