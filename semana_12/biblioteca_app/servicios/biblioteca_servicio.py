from modelos.libro import Libro
from modelos.usuario import Usuario
import json


class BibliotecaServicio:

    def __init__(self):

        # Diccionario requerido para almacenar libros
        # clave = ISBN
        # valor = objeto Libro
        self.libros = {}

        # Usuarios registrados
        self.usuarios = {}

        # Conjunto para controlar IDs únicos
        self.ids_usuarios = set()

    # VALIDAR ISBN

    def validar_isbn(self, isbn):

        if not isbn.isdigit():
            return False

        if len(isbn) < 5:
            return False

        return True

    # GESTIÓN DE LIBROS

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if not self.validar_isbn(isbn):
            print("ISBN inválido.")
            return

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro agregado correctamente.")

    def eliminar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # USUARIOS

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado")

        else:
            print("Usuario no encontrado")

    # PRÉSTAMOS

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        if isbn not in self.libros:
            print("Libro no disponible")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:

            if libro.isbn == isbn:

                usuario.devolver_libro(libro)
                self.libros[isbn] = libro

                print("Libro devuelto correctamente")
                return

        print("El usuario no tiene ese libro")

    # BÚSQUEDAS

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():
            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)

    # LISTAR CATÁLOGO

    def listar_catalogo(self):

        if not self.libros:
            print("No hay libros disponibles")
            return

        print("\nCATÁLOGO DE LIBROS")

        for libro in self.libros.values():
            print(libro)

    # LIBROS PRESTADOS

    def libros_prestados_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[id_usuario]

        if not usuario.libros_prestados:
            print("No tiene libros prestados")
            return

        for libro in usuario.libros_prestados:
            print(libro)

    # GUARDAR DATOS

    def guardar_datos(self):

        datos = {
            "libros": [],
            "usuarios": []
        }

        for libro in self.libros.values():

            datos["libros"].append({
                "titulo": libro.obtener_titulo(),
                "autor": libro.obtener_autor(),
                "categoria": libro.categoria,
                "isbn": libro.isbn
            })

        for usuario in self.usuarios.values():

            datos["usuarios"].append({
                "nombre": usuario.nombre,
                "id": usuario.id_usuario
            })

        with open("biblioteca_datos.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print("Datos guardados correctamente")

    # CARGAR DATOS

    def cargar_datos(self):

        try:

            with open("biblioteca_datos.json", "r") as archivo:
                datos = json.load(archivo)

            for libro in datos["libros"]:

                nuevo_libro = Libro(
                    libro["titulo"],
                    libro["autor"],
                    libro["categoria"],
                    libro["isbn"]
                )

                self.libros[nuevo_libro.isbn] = nuevo_libro

            for usuario in datos["usuarios"]:

                nuevo_usuario = Usuario(
                    usuario["nombre"],
                    usuario["id"]
                )

                self.usuarios[nuevo_usuario.id_usuario] = nuevo_usuario
                self.ids_usuarios.add(nuevo_usuario.id_usuario)

            print("Datos cargados correctamente")

        except FileNotFoundError:
            print("No existe archivo de datos aún")