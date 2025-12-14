# PROGRAMA ENFOCADO EN PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

class DiaClima:
    # Clase que representa la información de un día.

    def __init__(self, nombre_dia):
        self.nombre = nombre_dia
        self.temperatura = None

    def ingresar_temperatura(self):
        while True:
            try:
                self.temperatura = float(input(f"Ingrese la temperatura para {self.nombre}: "))
                break
            except ValueError:
                print("Valor inválido. Por favor ingrese un número.")

    def __str__(self):
        return f"{self.nombre}: {self.temperatura}°C"


class SemanaClima:
    # Clase que representa la semana completa.

    def __init__(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.dias_clima = [DiaClima(d) for d in dias]

    def registrar_temperaturas(self):
        for dia in self.dias_clima:
            dia.ingresar_temperatura()

    def promedio_semanal(self):
        temp_totales = [dia.temperatura for dia in self.dias_clima if dia.temperatura is not None]
        if not temp_totales:
            return 0
        return sum(temp_totales) / len(temp_totales)

    def mostrar_informe(self):
        print("\n--- Temperaturas Registradas ---")
        for dia in self.dias_clima:
            print(dia)
        print(f"\nPromedio semanal: {self.promedio_semanal():.2f}°C")


def main():
    print("=== Registro de Temperaturas (POO) ===")

    semana = SemanaClima()
    semana.registrar_temperaturas()
    semana.mostrar_informe()


# Punto de entrada
if __name__ == "__main__":
    main()
