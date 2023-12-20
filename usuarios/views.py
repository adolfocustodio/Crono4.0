from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdministradorPermission
from django.views import generic
from .models import Usuario


class UsuarioListar(LoginRequiredMixin, AdministradorPermission, generic.ListView):
    model = Usuario
