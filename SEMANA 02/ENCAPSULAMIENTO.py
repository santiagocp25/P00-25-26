
class CuentaSimple:
    def __init__(self, saldo_inicial):
        # Atributo privado: no debería modificarse directamente desde fuera
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        # Permite incrementar el saldo, si el monto es válido
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto debe ser positivo.")

    def obtener_saldo(self):
        # Devuelve el saldo actual sin permitir modificarlo directamente
        return self.__saldo


if __name__ == "__main__":
    cuenta = CuentaSimple(100)
    print("Saldo inicial:", cuenta.obtener_saldo())  # 100

    cuenta.depositar(50)
    print("Saldo después del depósito:", cuenta.obtener_saldo())  # 150

    # Intento de acceder directamente al saldo privado (no recomendado / dará error)
    # print(cuenta.__saldo)  # => AttributeError: 'CuentaSimple' object has no attribute '__saldo'
