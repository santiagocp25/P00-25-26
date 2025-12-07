class Calculadora:
    # Un ejemplo de abstraccion es una calculadora simple que ofrece operaciones básicas al usuario, y ocultamos los detalles de cómo se implementan internamente.

    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b
        # sumamos a+b

    def restar(self, a, b):
        return a - b
        # restamos a-b

    def multiplicar(self, a, b):
        return a * b
        # multiplicamos a*b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
        # dividimos a / b (siempre que b ≠ 0)

if __name__ == "__main__":
    calc = Calculadora()
    print(calc.sumar(8, 9))
    print(calc.restar(8, 9))
    print(calc.multiplicar(6, 7))
    print(calc.dividir(10, 2))
