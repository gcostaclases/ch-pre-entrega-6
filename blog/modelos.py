class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales or []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
        }


class Post:
    ESTADOS_VALIDOS = ("borrador", "publicado", "archivado")

    def __init__(self, id, titulo, contenido, autor, tags, estado="borrador"):
        if not isinstance(autor, Autor):
            raise TypeError(
                "El autor de un post debe ser una instancia de Autor.")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado,
        }

    def validar(self):
        errores = []

        if not isinstance(self.titulo, str) or not self.titulo.strip():
            errores.append("El título está vacío o no es texto.")
        if not isinstance(self.contenido, str) or not self.contenido.strip():
            errores.append("El contenido está vacío o no es texto.")
        if not isinstance(self.tags, list):
            errores.append("Los tags deben ser una lista.")
        if self.estado not in self.ESTADOS_VALIDOS:
            errores.append("El estado no es válido.")

        return errores


class Blog:
    def __init__(self, posts=None):
        self.posts = list(posts or [])

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        termino = termino.lower()
        resultados = []

        for post in self.posts:
            titulo = post.titulo.lower()

            if termino in titulo:
                resultados.append(post)

        return resultados

        # Con compresión de listas quedaría así:
        # return [post for post in self.posts if termino in post.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag = tag.lower()
        resultados = []

        for post in self.posts:
            for etiqueta in post.tags:
                if etiqueta.lower() == tag:
                    resultados.append(post)

        return resultados

    def agregar_post(self, post):
        if not isinstance(post, Post):
            raise TypeError("El blog solo admite objetos Post.")
        self.posts.append(post)

    def validar_posts(self):
        resultados = []

        for post in self.posts:
            errores = post.validar()
            resultados.append((post, errores))

        return resultados

    def siguiente_id(self):
        return max((post.id for post in self.posts), default=0) + 1
