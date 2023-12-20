from django.views.generic import TemplateView
from postagens.models import Postagem


class Inicio(TemplateView):
    template_name = 'core/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postagens'] = Postagem.objects.all()
        return context
