def listar_posts(lista_posts):
    for post in lista_posts:
        print(
            f"Título: {post.titulo} | Autor: {post.autor.nombre} | "
            f"Estado: {post.estado} | Etiquetas: {', '.join(post.tags)}"
        )


def buscar_por_titulo(lista, termino):
    resultados = []

    for post in lista:
        titulo = post.titulo.lower()

        if termino.lower() in titulo:
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    resultados = []

    for post in lista:
        for t in post.tags:
            if t.lower() == tag.lower():
                resultados.append(post)

    return resultados
