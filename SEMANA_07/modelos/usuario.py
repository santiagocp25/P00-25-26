class Usuario:
    # Representa un usuario del sistema.
    # Solo modela datos (responsabilidad de entidad).

    def __init__(self, nombre: str, email: str):

        self.nombre = nombre
        self.email = email
        self.activo = True  # valor por defecto
        print(f"[INIT] Usuario creado: {self.nombre} ({self.email})")

    def desactivar(self):
        # Cambia el estado del usuario
        self.activo = False

    def __str__(self):
        return f"Usuario(nombre={self.nombre}, email={self.email}, activo={self.activo})"

    def __del__(self):

        print(f"[DEL] Usuario eliminado de memoria: {self.nombre}")
