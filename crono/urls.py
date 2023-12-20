from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('postagens/', include('postagens.urls', namespace='postagens')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('admin/', admin.site.urls)
]
