import math

def calcular_area_rectangulo(base: float, altura: float) -> float:
    # Calcula el área de un rectángulo.
    # parametro base: Base del rectángulo (float)
    # parametro altura: Altura del rectángulo (float)
    # return: Área del rectángulo (float)

    return base * altura

def calcular_area_circulo(radio: float) -> float:
    # Calcula el área de un círculo.
    # param radio: Radio del círculo (float)
    # return: Área del círculo (float)

    return math.pi * (radio ** 2)

def programa_principal() -> None:
    print("¡Bienvenido al calculador de áreas!\n")

    # Pedimos al usuario qué figura quiere calcular
    figura_elegida: str = input("Ingresa 'R' para rectángulo o 'C' para círculo: ").upper().strip()

    figura_valida: bool = figura_elegida in ["R", "C"]

    if not figura_valida:
        print("Opción no válida. Finalizando el programa.")
        return

    if figura_elegida == "R":
        base_rectangulo: float = float(input("Ingresa la base del rectángulo: "))
        altura_rectangulo: float = float(input("Ingresa la altura del rectángulo: "))
        area_rectangulo: float = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

        print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} "
            f"es: {area_rectangulo:.2f}")

    elif figura_elegida == "C":
        radio_circulo: float = float(input("Ingresa el radio del círculo: "))
        area_circulo: float = calcular_area_circulo(radio_circulo)

        print(f"El área del círculo con radio {radio_circulo} "
            f"es: {area_circulo:.2f}")

    print("\nGracias por usar el programa. ¡Hasta pronto!")

# Ejecutar el programa
programa_principal()
