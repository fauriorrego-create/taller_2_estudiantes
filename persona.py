
class Persona:
    def __init__(self, nombre, edad):
        #nombre público y edad privada
        self.nombre = nombre        
        self.__edad = edad          

    # getter para la edad (encapsulamiento)
    def get_edad(self):
        return self.__edad

    # setter con validación (solo positiva)
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int, float)) and nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("Edad inválida: debe ser un número positivo.")

    # método para mostrar info básico
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.get_edad()}")
