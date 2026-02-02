# herencia.py

class Animal:
    """
    Clase base (superclase).
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Este animal hace un sonido.")


class Perro(Animal):
    """
    Clase hija que hereda de Animal.
    """

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")


class Gato(Animal):
    """
    Otra clase hija.
    """

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")


# Programa principal
if __name__ == "__main__":
    print("=== Ejemplo de Herencia ===")

    perro = Perro("Firulais")
    gato = Gato("Michi")

    perro.hacer_sonido()
    gato.hacer_sonido()
