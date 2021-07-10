from funciones import *

def agrega_modifica(tabla_contactos = dict()):
    nombre = input("Ingrese nombre a buscar: ")
    if nombre.lower() not in tabla_contactos.keys():
        muestro_mensaje("Ese contacto no existe en la agenda!")
        muestro_mensaje("Agrega ese contacto?(s/n):\r")
        opcion = input()
        if opcion.lower() == "s":
            codigo = str(len(tabla_contactos.items())+1)
            tabla_contactos[codigo] = input("\tIngrese Nombre del contacto:")

        

    return tabla_contactos


def buscar():
    pass


def borrar():
    pass


def listar():
    pass


def Main()
    while True:
        limpiar_pantalla()
        opcion = hacer_menu("1 - Agrega/Modifica un contacto", "2 - Buscar contacto", "3 - Borrar contacto", 
                    "4 - Listar contacto", "5 - Salir")
        if opcion == 1:
            tabla_contactos = agrega_modifica(tabla_contactos)
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            borrar()
        elif opcion == 4:
            listar()
        else:
            break


Main()
