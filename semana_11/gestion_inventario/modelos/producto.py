class Producto:

    # Representa un producto del inventario.
    # Aplica encapsulamiento y métodos de serializacion.

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # GETTERS
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # SETTERS
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio

    # SERIALIZACIÓN
    def to_dict(self):

        # Convierte el objeto a diccionario para guardarlo en JSON.

        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data):
        # Reconstruye un objeto Producto desde un diccionario.

        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self.__id} | {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"