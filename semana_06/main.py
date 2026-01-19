# main.py

from servicios.gestion_personas import GestionPersonas
from modelos.persona import Persona, Estudiante

def main():
    gestor = GestionPersonas()

    persona1 = Persona("Ana", 30)
    estudiante1 = Estudiante("Luis", 20, "Ingeniería")
    estudiante2 = Estudiante("María", 22, "Medicina")

    gestor.agregar_persona(persona1)
    gestor.agregar_persona(estudiante1)
    gestor.agregar_persona(estudiante2)

    print("Listado de personas:")
    gestor.mostrar_todas()

if __name__ == "__main__":
    main()
