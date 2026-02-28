from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    print("\n===== INVENTARIO AVANZADO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Mostrar resumen")
    print("7. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            try:
                id_ = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print(" Datos inválidos.")

        elif opcion == "2":
            inventario.eliminar_producto(input("ID: "))

        elif opcion == "3":
            id_ = input("ID: ")
            cantidad = input("Nueva cantidad (Enter omitir): ")
            precio = input("Nuevo precio (Enter omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_, cantidad, precio)

        elif opcion == "4":
            resultados = inventario.buscar_por_nombre(input("Nombre: "))
            for p in resultados:
                print(p)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            total, valor = inventario.obtener_resumen()
            print(f"Total productos: {total}")
            print(f"Valor total inventario: ${valor:.2f}")

        elif opcion == "7":
            print(" Saliendo...")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    main()