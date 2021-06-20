'''Ejercicio 15: Verificar una contraseña

En este ejercicio escribirá una función que determina si una contraseña es buena o no. Definiremos como 
una buena contraseña aquella que tenga una longitud de al menos 8 caracteres y contenga al menos una letra 
mayúscula, al menos una letra minúscula y al menos un número. Su función debe devolver verdadero si la 
contraseña que se le pasó, como único parámetro, es buena, de lo contrario debería devolver falso. 
Incluya un programa principal que lea una contraseña del usuario e informe si es buena o no.'''

from funciones import limpiar_pantalla, muestro_mensaje

def probar_contraseña(string):
    if len(string) >= 8:
        abecedario = "abcdefghijklmnñopqrstuvwxyz"
        numeros = "0123456789"
        mayuscula = False
        minuscula = False
        numero = False
        for cada_letra in string:
            if cada_letra in abecedario:
                minuscula = True
            elif cada_letra in abecedario.upper():
                mayuscula = True
            elif cada_letra in numeros:
                numero = True
        if minuscula and mayuscula and numero:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    sigo = True
    muestro_continua = True
    while sigo:
        limpiar_pantalla()
        muestro_mensaje("UNA CONTRASEÑA CORRECTA DEBE TENER: 1- MAS DE 8 CARACTERES 2 - AL MENOS 1 LETRA MAYUSCULA")
        muestro_mensaje("3 - AL MENOS 1 LETRA MINUSCULA  4 - AL MENOS 1 NUMERO")
        string = input("\tIngrese una cadena para probar como contraseña(Presione Enter para salir):")
        if string =="":
            sigo = False
            continue
        muestro_mensaje(str(probar_contraseña(string)), muestro_continua)
    limpiar_pantalla()
    muestro_mensaje("Gracias por venir")
    
