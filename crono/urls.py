from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('categorias', include('categorias.urls', namespace='categorias')),
    path('postagens', include('postagens.urls', namespace='postagens')),
    path('admin/', admin.site.urls)
]
