# polimorfismo.py

class Ave:
    def moverse(self):
        print("El ave vuela en el cielo.")


class Pez:
    def moverse(self):
        print("El pez nada en el agua.")


class Caballo:
    def moverse(self):
        print("El caballo corre en la tierra.")


def mostrar_movimiento(animal):
    """
    Función que aplica polimorfismo:
    recibe cualquier objeto con método 'moverse'
    """
    animal.moverse()


# Programa principal
if __name__ == "__main__":
    print("=== Ejemplo de Polimorfismo ===")

    ave = Ave()
    pez = Pez()
    caballo = Caballo()

    mostrar_movimiento(ave)
    mostrar_movimiento(pez)
    mostrar_movimiento(caballo)
