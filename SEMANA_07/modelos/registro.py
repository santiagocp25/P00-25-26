class RegistroSistema:

    # Clase encargada de manejar un archivo de registro (log).
    # Aquí sí tiene sentido un destructor para cerrar el archivo.


    def __init__(self, ruta_archivo: str):

        self.ruta_archivo = ruta_archivo
        self.archivo = open(self.ruta_archivo, "a", encoding="utf-8")
        print(f"[INIT] Archivo de registro abierto en: {self.ruta_archivo}")

    def escribir(self, mensaje: str):

        # Escribe una línea en el archivo de log
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()  # fuerza escritura inmediata

    def __del__(self):

        try:
            if not self.archivo.closed:
                self.archivo.close()
                print("[DEL] Archivo de registro cerrado correctamente.")
        except AttributeError:
            # Por si el archivo nunca se llegó a crear
            pass
