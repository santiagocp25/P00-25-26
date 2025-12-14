# PROGRAMA ENFOCADO EN PROGRAMACIÓN TRADICIONAL

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura de {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


# Función principal para controlar el flujo
def main():
    print("=== Registro de Temperaturas Diarias ===")
    datos = ingresar_temperaturas()

    promedio = calcular_promedio(datos)
    print("\nResultados:")
    print(f"Temperaturas ingresadas: {datos}")
    print(f"Promedio semanal: {promedio:.2f}°C")


# Punto de entrada
if __name__ == "__main__":
    main()
