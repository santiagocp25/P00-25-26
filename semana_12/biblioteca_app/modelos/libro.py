# Clase que representa un libro en la biblioteca

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # titulo_autor se almacena como tupla (requisito del ejercicio)

        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.titulo_autor[0]

    def obtener_autor(self):
        return self.titulo_autor[1]

    def __str__(self):
        return f"Título: {self.obtener_titulo()} | Autor: {self.obtener_autor()} | Categoría: {self.categoria} | ISBN: {self.isbn}"