class Perro:
    def hablar(self):
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

def que_habla(animal):
    print(animal.hablar())

if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    que_habla(perro)  # Imprime: Guau!
    que_habla(gato)   # Imprime: Miau!

