import os
import subprocess

def mostrar_codigo(ruta_script):
    """
    Lee y muestra el contenido de un archivo Python.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script en una nueva ventana de terminal.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Muestra el menú principal con las unidades disponibles.
    🔹 MODIFICACIÓN: Se agregó la 'Unidad 3'
    """
    ruta_base = os.path.dirname(__file__)

    # 🔥 SE AGREGÓ LA UNIDAD 3 AQUÍ
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Unidad 3'  # ← NUEVA UNIDAD DE POO
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])

            # 🔹 Validación adicional para evitar errores si la carpeta no existe
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print("La carpeta de esta unidad aún no existe.")
        else:
            print("Opción no válida. Intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas dentro de una unidad.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida.")


def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts Python disponibles dentro de la subcarpeta.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú principal")

        eleccion_script = input("Elige un script: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        else:
                            print("No se ejecutó el script.")

                        input("\nPresiona Enter para continuar.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida.")


# 🔹 PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    mostrar_menu()
