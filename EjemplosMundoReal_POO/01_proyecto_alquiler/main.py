# En este archivo escribimos el "código de prueba" que usa las clases
# definidas en los otros módulos.

from modelos import Coche, Cliente
from agencia import AgenciaAlquiler


def main():
    # Creamos una agencia de alquiler.
    agencia = AgenciaAlquiler("Alquiler Rápido")

    # Creamos algunos coches y los agregamos a la agencia.
    coche1 = Coche("Toyota", "Corolla", "ABC-123")
    coche2 = Coche("Honda", "Civic", "XYZ-789")

    agencia.agregar_coche(coche1)
    agencia.agregar_coche(coche2)

    # Creamos un cliente.
    cliente1 = Cliente("Juan Pérez", "0102030405")

    # Mostramos coches disponibles antes del alquiler.
    agencia.listar_coches_disponibles()

    # El cliente alquila un coche por matrícula.
    print("Intentando alquilar el coche ABC-123 para Juan Pérez...")
    alquiler1 = agencia.alquilar_coche(cliente1, "ABC-123", dias=5)

    if alquiler1 is not None:
        print("Alquiler creado:")
        print(alquiler1)
    else:
        print("No se pudo crear el alquiler.")

    # Mostramos coches disponibles después del alquiler.
    print("Despues del alquiler:")
    agencia.listar_coches_disponibles()

    # Devolvemos el coche (finalizamos el alquiler).
    if alquiler1 is not None:
        print("Devolviendo el coche alquilado...")
        agencia.devolver_coche(alquiler1)
        print(alquiler1)

    # Mostramos coches disponibles después de la devolución.
    print("Después de la devolución:")
    agencia.listar_coches_disponibles()


if __name__ == "__main__":
    main()