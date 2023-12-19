from django.urls import path
from .views import Inicio


app_name = 'core'
urlpatterns = [
    path('inicio', Inicio.as_view(), name='inicio')
]
