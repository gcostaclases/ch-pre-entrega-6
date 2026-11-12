from .datos import estados_post
from .modelos import Post

# Hago un set con las claves obligatorias
CLAVES_OBLIGATORIAS = {
    "id",
    "titulo",
    "contenido",
    "autor",
    "tags",
    "estado"
}


def validar_post(post):
    if isinstance(post, Post):
        return post.validar()

    errores = []

    # Compruebo que post sea un diccionario
    if not isinstance(post, dict):
        return ["El post no es un diccionario."]

    # Compruebo que todas las claves obligatorias estén presentes en el diccionario post
    claves_faltantes = CLAVES_OBLIGATORIAS - post.keys()

    if claves_faltantes:
        errores.append(
            f"Faltan claves obligatorias: {', '.join(claves_faltantes)}."
        )

    # Compruebo que el título sea una cadena de texto no vacía
    if "titulo" in post:
        if not isinstance(post["titulo"], str) or not post["titulo"].strip():
            errores.append("El título está vacío o no es texto.")

    # Compruebo que el contenido sea una cadena de texto no vacía
    if "contenido" in post:
        if not isinstance(post["contenido"], str) or not post["contenido"].strip():
            errores.append("El contenido está vacío o no es texto.")

    # Compruebo que el autor sea un diccionario
    if "autor" in post:
        autor = post["autor"]

        if not isinstance(autor, dict):
            errores.append("El autor debe ser un diccionario.")
        elif "nombre" not in autor:
            errores.append("El autor no tiene la clave 'nombre'.")

    # Compruebo que los tags sean una lista
    if "tags" in post:
        if not isinstance(post["tags"], list):
            errores.append("Los tags deben ser una lista.")

    # Compruebo que el estado del post esté dentro de los estados permitidos
    if "estado" in post:
        if post["estado"] not in estados_post:
            errores.append("El estado no es válido.")

    return errores
