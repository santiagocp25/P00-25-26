from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    print("\n===== BIBLIOTECA DIGITAL =====")

    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar por título")
    print("8. Buscar por autor")
    print("9. Buscar por categoría")
    print("10. Ver libros prestados de usuario")
    print("11. Ver catálogo completo")
    print("0. Salir")


def main():

    biblioteca = BibliotecaServicio()

    # cargar datos existentes
    biblioteca.cargar_datos()

    while True:

        menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID usuario: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":

            titulo = input("Título: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "9":

            categoria = input("Categoría: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "10":

            id_usuario = input("ID usuario: ")
            biblioteca.libros_prestados_usuario(id_usuario)

        elif opcion == "11":

            biblioteca.listar_catalogo()

        elif opcion == "0":

            biblioteca.guardar_datos()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()