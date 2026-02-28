import json
import os
from modelos.producto import Producto


class Inventario:

    # Gestiona el inventario usando un diccionario:
    # { id_producto: Producto }


    def __init__(self, archivo="data/inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario principal
        self.cargar()


    # AÑADIR PRODUCTO

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(" ID duplicado.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar()
        print(" Producto añadido correctamente.")


    # ELIMINAR PRODUCTO

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()
            print(" Producto eliminado.")
        else:
            print(" Producto no encontrado.")


    # ACTUALIZAR PRODUCTO

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)

            self.guardar()
            print(" Producto actualizado.")
        else:
            print(" Producto no encontrado.")


    # BUSCAR POR NOMBRE

    def buscar_por_nombre(self, nombre):
        # Retorna lista de coincidencias parciales.
        # Usa lista como colección secundaria.

        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]


    # MOSTRAR INVENTARIO

    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        for producto in self.productos.values():
            print(producto)


    # COLECCIONES ADICIONALES

    def obtener_nombres_unicos(self):

        # Devuelve un conjunto (set) con nombres únicos.

        return {p.get_nombre() for p in self.productos.values()}

    def obtener_resumen(self):

        # Devuelve una tupla con:
        # (total_productos, valor_total_inventario)

        total_productos = len(self.productos)
        valor_total = sum(
            p.get_cantidad() * p.get_precio()
            for p in self.productos.values()
        )
        return (total_productos, valor_total)


    # GUARDAR EN ARCHIVO

    def guardar(self):
        try:
            os.makedirs(os.path.dirname(self.archivo), exist_ok=True)

            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(
                    {id_: p.to_dict() for id_, p in self.productos.items()},
                    f,
                    indent=4
                )

        except PermissionError:
            print(" Error de permisos al guardar.")
        except Exception as e:
            print(" Error inesperado:", e)


    # CARGAR DESDE ARCHIVO

    def cargar(self):
        try:
            if not os.path.exists(self.archivo):
                self.guardar()
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)

                for id_, producto_data in data.items():
                    self.productos[id_] = Producto.from_dict(producto_data)

            print(" Inventario cargado correctamente.")

        except json.JSONDecodeError:
            print("⚠ Archivo JSON corrupto. Se iniciará vacío.")
            self.productos = {}
        except PermissionError:
            print(" Sin permisos para leer archivo.")
        except Exception as e:
            print(" Error inesperado:", e)