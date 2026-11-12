# El checkpoint pide realizar los imports desde main.py. Estas exportaciones
# se mantienen solo para probar la importación de funciones desde el paquete.
from .modelos import Autor, Blog, Post
from .datos import cargar_posts, guardar_posts
