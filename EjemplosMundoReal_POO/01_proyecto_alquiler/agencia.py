from modelos import Coche, Cliente, Alquiler


# La clase AgenciaAlquiler coordina coches, clientes y alquileres.
# Su responsabilidad es gestionar las listas de coches y alquileres,
# y ofrecer métodos para alquilar y devolver coches.
class AgenciaAlquiler:
    def __init__(self, nombre: str):
        # Nombre de la agencia de alquiler.
        self.nombre = nombre
        # Lista de coches que maneja la agencia (objetos Coche).
        self.coches = []
        # Lista de alquileres realizados (objetos Alquiler).
        self.alquileres = []

    def agregar_coche(self, coche: Coche):
        """Agrega un objeto Coche a la lista de coches de la agencia."""
        self.coches.append(coche)

    def listar_coches_disponibles(self):
        """Muestra en pantalla todos los coches que están disponibles."""
        print(f"Coches disponibles en la agencia {self.nombre}:")
        for coche in self.coches:
            if coche.disponible:
                print(" -", coche)

    def alquilar_coche(self, cliente: Cliente, matricula: str, dias: int) -> Alquiler | None:
        """Intenta alquilar un coche por matrícula a un cliente.

        - Busca un coche disponible con esa matrícula.
        - Si lo encuentra, crea un Alquiler, actualiza el estado del coche
          y devuelve el objeto Alquiler.
        - Si no lo encuentra o no está disponible, devuelve None.
        """
        for coche in self.coches:
            if coche.matricula == matricula and coche.disponible:
                coche.marcar_como_alquilado()
                nuevo_alquiler = Alquiler(cliente, coche, dias)
                self.alquileres.append(nuevo_alquiler)
                return nuevo_alquiler

        # Si no se encontró coche disponible con esa matrícula
        print(f"No se pudo alquilar el coche con matrícula {matricula} (no existe o no disponible).")
        return None

    def devolver_coche(self, alquiler: Alquiler):
        """Recibe un objeto Alquiler y lo finaliza.

        Esto muestra cómo la agencia colabora con la clase Alquiler
        y cómo, a través de ella, se actualiza el estado del Coche.
        """
        if alquiler in self.alquileres and alquiler.activo:
            alquiler.finalizar_alquiler()
            print("Alquiler finalizado con éxito.")
        else:
            print("El alquiler ya estaba finalizado o no pertenece a esta agencia.")