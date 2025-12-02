
from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    # sobrescribe el método mostrar_info para agregar el grado
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.get_edad()}, Grado: {self.grado}")
