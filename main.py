from blog.datos import cargar_posts, guardar_posts
from blog.menu import obtener_opcion_menu
from blog.modelos import Autor, Blog, Post
from blog.operaciones import listar_posts


def main():
    blog = Blog(cargar_posts())
    while True:
        opcion = obtener_opcion_menu()

        if opcion == 1:
            print("\nListado de posts:")
            listar_posts(blog.listar_posts())

        elif opcion == 2:
            termino = input("Ingrese el titulo a buscar: ").strip()
            if termino:
                resultados = blog.buscar_por_titulo(termino)
                listar_posts(resultados)
            else:
                print("La búsqueda no puede estar vacía.")

        elif opcion == 3:
            tag = input("Ingrese el tag para filtrar: ").strip()
            if tag:
                resultados = blog.filtrar_por_tag(tag)
                listar_posts(resultados)
            else:
                print("El tag no puede estar vacío.")

        elif opcion == 4:
            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()
            nombre = input("Nombre del autor: ").strip()
            tags = [tag.strip() for tag in input(
                "Tags separados por coma: ").split(",") if tag.strip()]
            if not titulo or not contenido or not nombre or not tags:
                print("Título, contenido, autor y tags son obligatorios.")
                continue
            autor = Autor(nombre)
            post = Post(blog.siguiente_id(), titulo, contenido, autor, tags)
            blog.agregar_post(post)
            print("Post creado correctamente.")

        elif opcion == 5:
            print("\nValidación de posts:")
            for post, errores in blog.validar_posts():

                if not errores:
                    print(f"El post '{post.titulo}' es válido.")
                else:
                    print(f"El post con ID {post.id} tiene errores:")
                    for error in errores:
                        print(f"- {error}")

        elif opcion == 6:
            guardar_posts(blog.posts)

        elif opcion == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
