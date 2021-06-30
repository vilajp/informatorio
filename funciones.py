import os

def limpiar_pantalla():
    os.system("cls")

def es_entero(string):
    string = string.strip()
    orden = 0
    for cada_letra in string:
        if orden == 0 and cada_letra in "-+":
            orden += 1
            continue
        elif cada_letra in "01234567890":
            continue
        else:
            return False
    return True

def hacer_menu(*opciones):
    opcion = len(opciones)+2
    largo = opcion_mas_larga(opciones)
    print("\t"+"*"*largo)
    for cada_opcion in opciones:
        print("\t",cada_opcion)
    print("\t"+"*"*largo)
    while opcion not in range(1, len(opciones)+1):
        opcion = int(input("\tIngrese una opcion del menu:"))
    return opcion

def opcion_mas_larga(lista):
    mas_larga = 0
    for cada_elemento in lista:
        if mas_larga < len(cada_elemento):
            mas_larga = len(cada_elemento)
    return mas_larga + 2   


def muestro_mensaje(texto, mensaje_continua=False):
    if not mensaje_continua:
        print("\t"+"*"*len(texto))
        print("\t",texto)
        print("\t"+"*"*len(texto))
    else:
        print("\t"+"*"*len(texto))
        print("\t",texto)
        print("\t"+"*"*len(texto))
        input("\tPresione cualquier tecla para continuar....")  