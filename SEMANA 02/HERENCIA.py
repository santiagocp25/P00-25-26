class Animal:
    def __init__(self, nombre):
        # atributo común a todos los animales
        self.nombre = nombre

    def info(self):
        # Muestra información básica del animal
        print("Este animal se llama:", self.nombre)

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

# Clase que hereda
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llama al constructor de la clase padre para inicializar nombre
        super().__init__(nombre)
        # atributo específico de Perro
        self.raza = raza

    # Metodo específico de Perro
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def hacer_sonido(self):
        # definimos comportamiento para perros
        self.ladrar()

if __name__ == "__main__":
    mi_animal = Animal("Perro")
    mi_animal.info()
    mi_animal.hacer_sonido()

    mi_perro = Perro("Firulais", "Labrador")
    mi_perro.info()
    mi_perro.ladrar()
    mi_perro.hacer_sonido()
