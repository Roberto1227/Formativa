# Proyecto Formativa - Django

Proyecto Django con dos modelos relacionados: **Autor** y **Libro**.

## Estructura del Proyecto

- **Proyecto**: `formativa`
- **Aplicación**: `biblioteca`

## Modelos

### Autor
- nombre
- apellido
- fecha_nacimiento
- nacionalidad

### Libro
- titulo
- autor (ForeignKey a Autor)
- isbn
- fecha_publicacion
- paginas

**Relación**: Un Autor puede tener muchos Libros (relación uno a muchos).

## Vistas

### Autores
- `/autores/` - Lista todos los autores
- `/autores/crear/` - Formulario para crear un nuevo autor

### Libros
- `/libros/` - Lista todos los libros
- `/libros/crear/` - Formulario para crear un nuevo libro

## Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Crear las migraciones:
```bash
python manage.py makemigrations
```

3. Aplicar las migraciones:
```bash
python manage.py migrate
```

4. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

5. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

6. Acceder a la aplicación:
- http://127.0.0.1:8000/autores/
- http://127.0.0.1:8000/libros/
- http://127.0.0.1:8000/admin/ (panel de administración)

Hecho por: 

-Roberto Carlos Chavez Campos

-Edwin Josue Parada Campos
