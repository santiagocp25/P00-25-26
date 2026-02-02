# clases_basicas.py

class Persona:
    """
    Clase básica que representa una persona.
    Demuestra atributos y métodos.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora {self.nombre} tiene {self.edad} años.")


# Programa principal
if __name__ == "__main__":
    print("=== Ejemplo de Clase Básica ===")

    persona1 = Persona("Carlos", 20)
    persona1.saludar()
    persona1.cumplir_anios()
