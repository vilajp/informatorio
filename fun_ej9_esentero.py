'''Ejercicio 9: ¿Un string representan un entero?

En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena 
representan un número entero válido. Al determinar si un string representa un número entero, debe ignorar
 cualquier espacio en blanco inicial o final. Una vez que se ignora este espacio en blanco, una cadena 
 representa un número entero si su longitud es al menos 1 y solo contiene dígitos, o si su primer carácter 
 es + o - y el primer carácter va seguido de uno o más caracteres, todos los cuales son dígitos Escriba un 
 programa principal que lea una cadena del usuario e informe si representa o no un número entero.

Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para cadenas útiles cuando complete 
este ejercicio.'''
from funciones import limpiar_pantalla, muestro_mensaje

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


if __name__ == "__main__":
    limpiar_pantalla()
    sigo = True
    while sigo:
        string = input("\n\tINGRESE UNA CADENA PARA VERIFICAR(Enter para terminar): ")
        if string == "":
            break
        respuesta = es_entero(string)
        if not respuesta:
            muestro_mensaje("BUUUUUUU!!!!!ESA CADENA NO REPRESENTA UN ENTERO")
        else:
            muestro_mensaje("FELICIDADES! SU CADENA REPRESENTA UN ENTERO!")
    limpiar_pantalla()
    muestro_mensaje("GRACIAS POR VENIR")