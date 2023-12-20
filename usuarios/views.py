from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdministradorPermission
from django.views import generic
from .models import Usuario, Administrador, Professor
from .forms import AdministradorRegistrationForm, ProfessorRegistrationForm
from django.urls import reverse_lazy


class UsuarioListar(LoginRequiredMixin, AdministradorPermission, generic.ListView):
    model = Usuario


class AdministradorCriar(LoginRequiredMixin, AdministradorPermission, generic.CreateView):
    form_class = AdministradorRegistrationForm
    model = Administrador
    success_url = reverse_lazy('core:inicio')


class ProfessorCriar(generic.CreateView):
    form_class = ProfessorRegistrationForm
    model = Professor
    success_url = reverse_lazy('core:inicio')
