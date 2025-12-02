
from persona import Persona

class AccesoPersona:
    def mostrar_info_persona(self, persona: Persona):
        # accede al nombre (público) y a la edad mediante el getter
        print("- Información de la persona -")
        print("Nombre:", persona.nombre)
        print("Edad:", persona.get_edad())
