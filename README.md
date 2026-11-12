# Blog por consola: POO y persistencia JSON

Este programa administra publicaciones de un blog desde la terminal. La
entrega 6 refactoriza el sistema anterior para trabajar con objetos y guardar
los datos en `posts.json`.

## Como ejecutar

Desde la carpeta `blog_consola`:

```bash
python main.py
```

El menú permite listar posts, buscar por título, filtrar por tag, crear posts,
validarlos, guardarlos y salir. Las búsquedas ignoran mayúsculas y minúsculas.

## Clases principales

- `Autor`: representa los datos de una persona autora.
- `Post`: representa una publicación y recibe un objeto `Autor`, además de su
  título, contenido, tags y estado.
- `Blog`: contiene la lista de objetos `Post` y centraliza las operaciones de
  listado, búsqueda, filtrado, creación y validación.

Cada `Autor` y `Post` implementa `to_dict()`. Las funciones
`crear_autor_desde_dict()` y `crear_post_desde_dict()` reconstruyen los objetos
al cargar el archivo. Así se convierten los objetos a diccionarios antes de
guardarse en JSON y se recuperan como objetos al iniciar el programa.
Los datos iniciales incluyen dos autores y posts asociados a cada uno. También
incluyen un post con datos inválidos para probar la opción de validación.

## Persistencia

El módulo `blog/datos.py` se encarga exclusivamente de cargar y guardar
`posts.json`. Si el archivo no existe, se usan datos iniciales. Si está vacío o
contiene JSON inválido, se informa el problema y el programa continúa sin
cerrarse inesperadamente.

Al crear un post, este se agrega al objeto `Blog`. La opción 6 guarda todos los
posts actuales y permite recuperarlos en la siguiente ejecución. Si
`posts.json` no existe, se crea al elegir esa opción.

## Estructura

```text
blog_consola/
|-- main.py
|-- README.md
|-- posts.json                 # se crea al guardar
|-- blog/
    |-- __init__.py
    |-- datos.py               # carga y guardado JSON
    |-- menu.py                # menú y validación de opciones
    |-- modelos.py             # Autor, Post y Blog
    |-- operaciones.py         # presentación de posts
    |-- validaciones.py        # compatibilidad y validaciones
```

## Cambios respecto de la entrega 5

La lista de diccionarios fue reemplazada por objetos `Autor`, `Post` y `Blog`.
La lógica principal ahora pertenece a `Blog`, el menú trabaja con esa
instancia y los datos se persisten mediante serialización JSON.
