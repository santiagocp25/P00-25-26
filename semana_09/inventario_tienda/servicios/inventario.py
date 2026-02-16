from modelos.producto import Producto

class Inventario:
    # Clase encargada de gestionar los productos.
    # Utiliza una lista como estructura principal de almacenamiento.


    def __init__(self):

        # Constructor de la clase Inventario.
        # Inicializa la lista de productos.

        self.productos = []

    # Añadir producto

    def añadir_producto(self, producto):

        # Añade un nuevo producto validando que el ID no esté repetido.

        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        print(" Producto añadido correctamente.")


    # Eliminar producto

    def eliminar_producto(self, id_producto):

        # Elimina un producto por su ID.

        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(" Producto eliminado correctamente.")
                return

        print(" Producto no encontrado.")


    # Actualizar producto

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        # Actualiza cantidad y/o precio de un producto por ID.

        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print(" Producto actualizado correctamente.")
                return

        print(" Producto no encontrado.")

    # Buscar producto por nombre

    def buscar_por_nombre(self, nombre):

        # Permite busqueda por coincidencias parciales (insensible a mayúsculas).

        resultados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        return resultados


    # Mostrar inventario

    def mostrar_inventario(self):

        # Muestra todos los productos registrados.

        if not self.productos:
            print(" El inventario está vacío.")
            return

        print("\n INVENTARIO ACTUAL ")
        for p in self.productos:
            print(p)