from django.urls import path, include
from .views import UsuarioListar


app_name = 'usuarios'
urlpatterns = [
    path('listar/', UsuarioListar.as_view(), name='usuario_listar'),
    path('accounts/', include('django.contrib.auth.urls'))

]
