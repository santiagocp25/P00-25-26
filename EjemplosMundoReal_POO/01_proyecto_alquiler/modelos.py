# La responsabilidad es conocer sus propios datos y si está disponible.
class Coche:
    def __init__(self, marca: str, modelo: str, matricula: str):
        # Marca del coche (por ejemplo, "Toyota").
        self.marca = marca
        # Modelo del coche (por ejemplo, "Corolla").
        self.modelo = modelo
        # Matrícula única del coche (por ejemplo, "ABC-123").
        self.matricula = matricula
        # Indica si el coche está disponible para ser alquilado.
        self.disponible = True

    def marcar_como_alquilado(self):
        """Marca el coche como no disponible (cambia el estado interno)."""
        self.disponible = False

    def marcar_como_disponible(self):
        """Marca el coche como disponible nuevamente tras una devolución."""
        self.disponible = True

    def __str__(self):
        estado = "disponible" if self.disponible else "no disponible"
        return f"{self.marca} {self.modelo} ({self.matricula}) - {estado}"


# La clase Cliente representa a la persona que alquila un coche.
# Su responsabilidad es guardar los datos básicos del cliente.
class Cliente:
    def __init__(self, nombre: str, documento: str):
        # Nombre completo del cliente.
        self.nombre = nombre
        # Documento de identidad (cédula, DNI, pasaporte, etc.).
        self.documento = documento

    def __str__(self):
        return f"Cliente: {self.nombre} - Documento: {self.documento}"


# La clase Alquiler representa el vínculo entre un Cliente y un Coche
# durante cierto número de días.
# Aquí se ve la COMPOSICIÓN: un Alquiler CONTIENE un Cliente y un Coche.
class Alquiler:
    def __init__(self, cliente: Cliente, coche: Coche, dias: int):
        # Objeto Cliente asociado al alquiler.
        self.cliente = cliente
        # Objeto Coche asociado al alquiler.
        self.coche = coche
        # Duración del alquiler en días.
        self.dias = dias
        # Indica si el alquiler está activo o ya fue finalizado.
        self.activo = True

    def finalizar_alquiler(self):
        """Finaliza el alquiler y marca el coche como disponible de nuevo."""
        self.activo = False
        self.coche.marcar_como_disponible()

    def __str__(self):
        estado = "activo" if self.activo else "finalizado"
        return (
            f"Alquiler de {self.coche.marca} {self.coche.modelo} "
            f"para {self.cliente.nombre} por {self.dias} días - Estado: {estado}"
        )
