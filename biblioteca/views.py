from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


def index(request):
    """Página de inicio"""
    return render(request, 'biblioteca/index.html')


def listar_autores(request):
    """Vista para listar todos los autores"""
    autores = Autor.objects.all()
    return render(request, 'biblioteca/listar_autores.html', {'autores': autores})


def crear_autor(request):
    """Vista para crear un nuevo autor"""
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/crear_autor.html', {'form': form})


def listar_libros(request):
    """Vista para listar todos los libros"""
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'biblioteca/listar_libros.html', {'libros': libros})


def crear_libro(request):
    """Vista para crear un nuevo libro"""
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear_libro.html', {'form': form})
