import os
from modelos.producto import Producto


class Inventario:

    # Clase que gestiona los productos y la persistencia en archivo.

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # CARGAR PRODUCTOS

    def cargar_desde_archivo(self):

        # Carga los productos desde el archivo.
        # Maneja excepciones como:
        # - FileNotFoundError
        # - PermissionError
        # - Errores por archivo corrupto

        try:
            if not os.path.exists(self.archivo):
                # Si no existe, lo crea vacío
                open(self.archivo, "w").close()
                print(" Archivo de inventario creado automáticamente.")
                return

            with open(self.archivo, "r", encoding="utf-8") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                    except ValueError:
                        print(" Línea corrupta ignorada:", linea.strip())

            print(" Inventario cargado correctamente desde archivo.")

        except PermissionError:
            print(" Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(" Error inesperado al cargar archivo:", e)


    # GUARDAR PRODUCTOS

    def guardar_en_archivo(self):

        # Guarda el inventario en el archivo
        # Sobrescribe el contenido

        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                for producto in self.productos:
                    file.write(producto.to_line())

            print(" Inventario guardado correctamente en archivo.")

        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(" Error inesperado al guardar archivo:", e)


    # AÑADIR PRODUCTO

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" ID duplicado.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto añadido y guardado en archivo.")


    # ELIMINAR PRODUCTO

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print(" Producto eliminado y cambios guardados.")
                return

        print(" Producto no encontrado.")


    # ACTUALIZAR PRODUCTO

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print(" Producto actualizado y guardado.")
                return

        print(" Producto no encontrado.")


    # BUSCAR

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]


    # MOSTRAR

    def mostrar_inventario(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        print("\n===== INVENTARIO =====")
        for p in self.productos:
            print(p)