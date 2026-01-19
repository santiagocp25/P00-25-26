# modelos/persona.py

class Persona:
    # Clase base que representa a una persona

    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre  # atributo encapsulado
        self._edad = edad      # atributo encapsulado

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_edad(self) -> int:
        return self._edad

    def set_edad(self, edad: int) -> None:
        if edad >= 0:
            self._edad = edad
        else:
            print("Edad no válida. Debe ser >= 0")

    def mostrar_info(self) -> str:
        # Metodo base para mostrar información (polimorfismo)
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

class Estudiante(Persona):
    # Clase derivada de Persona que representa a un estudiante

    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        self._carrera = carrera

    def get_carrera(self) -> str:
        return self._carrera

    def set_carrera(self, carrera: str) -> None:
        self._carrera = carrera

    def mostrar_info(self) -> str:
        # Sobrescribe mostrar_info (polimorfismo)
        base = super().mostrar_info()
        return f"{base}, Carrera: {self._carrera}"
