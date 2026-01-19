# servicios/gestion_personas.py

from modelos.persona import Persona, Estudiante

class GestionPersonas:
    # Clase que gestiona a varias personas/estudiantes.

    def __init__(self):
        self.lista_personas = []

    def agregar_persona(self, persona: Persona) -> None:
        # Agrega una persona o estudiante a la lista.
        self.lista_personas.append(persona)

    def mostrar_todas(self) -> None:
        # Muestra información de cada persona.
        for p in self.lista_personas:
            print(p.mostrar_info())  # Polimorfismo en acción
