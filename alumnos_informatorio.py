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
        limpiar_pantalla()
        print()
        print("\t**** SISTEMA DE CARGA DE ALUMNOS ****")    
        print()
        dni = input("\tIngrese DNI del alumno(Enter para salir): ")
        if dni == "":
            sigo = False
            continue
        elif es_entero(dni) and dni not in base.items():
            base[dni] = dict()
            base[dni]["nombre"]= input("\tIngrese nombre del alumno: ")
            base[dni]["localidad"] = input("\tIngrese localidad: ")
            print()
            continuo = " "
            while continuo.lower() not in ("sn"):
                continuo = input("\tCarga otro alumno? (s/n):")
                if continuo.lower()== "n":
                    sigo = False
    return base

def cargo_notas(base):
    sigo = True
    while sigo:    
        dni = input("\tIngrese DNI del alumno(Enter para salir): ")
        if dni == "":
            sigo = False
            continue
        elif es_entero(dni) and dni in base.keys():
            print(f"Alumno: {base[dni]['nombre']}")
            print()
            base[dni]["notasBD"] = input("\tIngrese Notas de Base de Datos separadas por comas: ").split(",")
            base[dni]["notasPW"] = input("\tIngrese Notas de Programacion Web separadas por comas: ").split(",")
            print()
            continuo = " "
            while continuo.lower() not in ("sn"):
                continuo = input("\tCarga notas de otro alumno? (s/n):")
                if continuo.lower()== "n":
                    sigo = False
        
    return base

def consulto_notas(base):
    sigo = True
    while sigo:
        limpiar_pantalla()
        opcion = hacer_menu("1 - Lista un alumno", "2 - Lista todos los Alumnos", "3 - Salir")
        if opcion == 3:
            sigo = False
            continue
        elif opcion == 1:
            dni = input("\tIngrese Numero de Documento a listar: ")
            if dni  not in base.keys():
                print("\tEse alumno no se encuentra en la base verifique!!!!!")
                input("\tPresione una tecla para continuar...")
                continue
            else:
                print(f"\tListado de notas para {base[dni]['nombre']}")
                print(f"\tNotas de Base de Datos")
                for nota in base[dni]["notasBD"]:
                    print("\tNota: ", nota )
                input()


if __name__ == "__main__":
    sigo = True
    base_alumnos = dict()
    while sigo:
        limpiar_pantalla()
        opcion = hacer_menu("1 - Cargar Nuevo Alumno", "2 - Cargar Notas de Examen",
        "3 - Consultar Notas Alumnos", 
        "4 - Ranking Promedios", "5 - Alumnos Aprobados","6 - Actualizar Alumnos", 
        "7 - Salir")
        if opcion == 7:
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
            if base_alumnos:
                limpiar_pantalla()
                cargo_notas(base_alumnos)
        elif opcion == 3:
            
            if base_alumnos:
                limpiar_pantalla()
                consulto_notas(base_alumnos)
        elif opcion == 4:
            
            if base_alumnos:
                limpiar_pantalla()
                ranking_promedios(base_alumnos)
        elif opcion == 5:

            if base_alumnos:
                limpiar_pantalla()
                alumnos_aprobados(base_alumnos)
        
        elif opcion == 6:
            if base_alumnos:
                limpiar_pantalla()
                actualizo_alumnos(base_alumnos)
    
        
        

