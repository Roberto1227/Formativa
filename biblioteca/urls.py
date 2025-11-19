from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
]

