from django.urls import path, include
from .views import UsuarioCriar, UsuarioListar, UsuarioEditar, UsuarioExcluir


app_name = 'usuarios'
urlpatterns = [
    path('criar/', UsuarioCriar.as_view(), name='usuario_criar'),
    path('listar/', UsuarioListar.as_view(), name='usuario_listar'),
    path('editar/<int:pk>/', UsuarioEditar.as_view(), name='usuario_editar'),
    path('excluir/<int:pk>/', UsuarioExcluir.as_view(), name='usuario_excluir'),
    path('accounts/', include('django.contrib.auth.urls'))

]
