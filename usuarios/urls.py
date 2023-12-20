from django.urls import path, include
from .views import UsuarioListar, AdministradorCriar, ProfessorCriar


app_name = 'usuarios'
urlpatterns = [
    path('listar/', UsuarioListar.as_view(), name='usuario_listar'),
    path('administrador/criar', AdministradorCriar.as_view(), name='admiministrador_criar'),
    path('professor/criar', ProfessorCriar.as_view(), name='professor_criar')
]
