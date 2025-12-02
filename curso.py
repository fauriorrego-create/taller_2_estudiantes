
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir(self, estudiante):
        # aquí suponemos que 'estudiante' tiene atributo 'nombre' y 'grado'
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"----- Curso: {self.nombre} -----")
        for idx, est in enumerate(self.estudiantes, start=1):
            # si el estudiante tiene mostrar_info, lo usamos; si no, mostramos atributos
            if hasattr(est, "mostrar_info"):
                print(f"{idx}. ", end="")
                est.mostrar_info()
            else:
                print(f"{idx}. {getattr(est,'nombre','<sin nombre>')} - {getattr(est,'grado','<sin grado>')}")
