from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'fecha_publicacion')
    list_filter = ('autor', 'fecha_publicacion')
    search_fields = ('titulo', 'isbn')

