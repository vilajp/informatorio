'''Un programa que me permita cargar los datos de los alumnos del info, nombre, localidad, dni
Me permita agregar  la nota de los exámenes, teniendo en cuenta que hay dos módulos.
Debe tener un menú interactivo que permita:
Mostrar el alumno con mayor promedio
Mostrar todos los que aprobaron ambos módulos
Dado el DNI de un alumno, me muestre sus notas'''
from funciones import hacer_menu, limpiar_pantalla, es_entero


def cargo_alumno(base=dict()):
    
    sigo = True
    while sigo:    
        dni = input("\tIngrese DNI del alumno(Enter para salir): ")
        if dni == "":
            sigo = False
            continue
        elif es_entero(dni):
            base[dni] = dict()
            base[dni]["nombre"]= input("\tIngrese nombre del alunmo: ")
            base[dni]["localidad"] = input("\tIngrese localidad:")
            print()
            continuo = " "
            while continuo.lower() not in ("sn"):
                continuo = input("\tCarga otro alumno? (s/n):")
                if continuo.lower()== "n":
                    sigo = False
    return base


if __name__ == "__main__":
    sigo = True
    base_alumnos = dict()
    while sigo:
        limpiar_pantalla()
        opcion = hacer_menu("1 - Cargar Nuevo Alumno", "2 - Consultar Notas Alumnos", 
        "3 - Ranking Promedios", "4 - Alumnos Aprobados", "5 - Salir")
        if opcion == 5:
            sigo = False
            continue
        elif opcion == 1:
            limpiar_pantalla()
            if not base_alumnos:
                base_alumnos = cargo_alumno()
            else:
                base_alumnos = cargo_alumno(base_alumnos)
            print(base_alumnos.items())
            input()
        elif opcion == 2:
            limpiar_pantalla()
            consulto_notas(base_alumnos)
        elif opcion == 3:
            limpiar_pantalla()
            ranking_promedios(base_alumnos)
        elif opcion == 4:
            limpiar_pantalla()
            alumnos_aprobados(base_alumnos)
        
        

