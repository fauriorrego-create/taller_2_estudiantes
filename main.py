# main.py
from persona import Persona
from acceso_persona import AccesoPersona
from estudiante import Estudiante
from estudiantecurso.curso import Curso

def main():
    # 1) Prueba de Persona y AccesoPersona
    p = Persona("Laura", 22)
    acceso = AccesoPersona()
    acceso.mostrar_info_persona(p)
    print()

    # 2) Prueba de set_edad y get_edad
    p.set_edad(23)
    print("Edad después de set_edad:", p.get_edad())
    print()

    # 3) Herencia: Estudiante y sobrescritura
    e = Estudiante("Carlos", 17, "11°")
    e.mostrar_info()
    print()

    # 4) Curso e inscripción
    curso = Curso("Programación")
    curso.inscribir(e)
    curso.inscribir(Estudiante("María", 16, "10°"))
    curso.mostrar_estudiantes()

if __name__ == "__main__":
    main()
