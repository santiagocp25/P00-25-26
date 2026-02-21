# main.py

from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("\n===== SISTEMA INVENTARIO TIENDA CALZADO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print(" Datos inválidos.")

        elif opcion == "2":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID a actualizar: ")

            try:
                nueva_cantidad = input("Nueva cantidad (Enter para omitir): ")
                nuevo_precio = input("Nuevo precio (Enter para omitir): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print(" Datos inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print(" No se encontraron resultados.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    main()