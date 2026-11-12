import json
from pathlib import Path

from .modelos import Autor, Post

ARCHIVO_POSTS = Path(__file__).resolve().parent.parent / "posts.json"
estados_post = Post.ESTADOS_VALIDOS

def posts_iniciales():
    autor_1 = Autor(
        "Guillermina Costa",
        "Desarrolladora web y creadora de contenido sobre programación.",
        "Python y Django",
        ["@guilledev", "@guillecosta"],
    )
    autor_2 = Autor(
        "Luis Martínez",
        "Desarrollador y entusiasta de la automatización.",
        "Python y testing",
        ["@luispython"],
    )
    datos = [
        (1, "Primeros pasos con Python", "Conceptos básicos de Python.",
         ["Python", "Principiantes", "Backend"], "publicado", autor_1),
        (2, "Qué es Django", "Django es un framework web escrito en Python.",
         ["Python", "Django", "Web"], "borrador", autor_1),
        (3, "Organizando datos con diccionarios", "Los diccionarios almacenan pares clave-valor.",
         ["Python", "Diccionarios"], "archivado", autor_1),
        (4, "Manejo de errores en Python", "Aprendé a manejar errores comunes.", [
         "Python", "Errores"], "publicado", autor_1),
        (5, "Automatizando tareas con Python",
         "Algunas tareas repetitivas pueden resolverse con scripts.",
         ["Python", "Automatización"], "publicado", autor_2),
        (6, "Pruebas para código más confiable",
         "Las pruebas ayudan a detectar errores antes de publicar.",
         ["Python", "Testing"], "borrador", autor_2),
        (7, "", "", "Python", "publicado", autor_1),
    ]
    posts = []

    for id, titulo, contenido, tags, estado, autor in datos:
        post = Post(id, titulo, contenido, autor, tags, estado)
        posts.append(post)

    return posts


def crear_autor_desde_dict(datos):
    return Autor(
        datos["nombre"],
        datos.get("bio", ""),
        datos.get("especialidad", ""),
        datos.get("redes_sociales", []),
    )


def crear_post_desde_dict(datos):
    claves = {"id", "titulo", "contenido", "autor", "tags", "estado"}
    if not isinstance(datos, dict):
        raise ValueError("El post debe ser un diccionario.")
    faltantes = claves - datos.keys()
    if faltantes:
        raise ValueError(
            f"El post no puede reconstruirse; faltan: {', '.join(sorted(faltantes))}."
        )
    autor = crear_autor_desde_dict(datos["autor"])
    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        autor,
        datos["tags"],
        datos["estado"],
    )


def cargar_posts(ruta=ARCHIVO_POSTS):
    ruta = Path(ruta)
    if not ruta.exists():
        print("No existe posts.json; se cargarán datos iniciales.")
        return posts_iniciales()
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not datos:
            print("posts.json está vacío; no hay posts cargados.")
            return []
        posts = []

        for item in datos:
            post = crear_post_desde_dict(item)
            posts.append(post)

        return posts
    except (
        AttributeError,
        json.JSONDecodeError,
        KeyError,
        OSError,
        TypeError,
        ValueError,
    ) as error:
        print(f"No se pudieron cargar los posts: {error}")
        return []


def guardar_posts(posts, ruta=ARCHIVO_POSTS):
    ruta = Path(ruta)
    try:
        datos = [post.to_dict() for post in posts]
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        print(f"Posts guardados en {ruta.name}.")
    except (AttributeError, OSError, TypeError) as error:
        print(f"No se pudieron guardar los posts: {error}")
