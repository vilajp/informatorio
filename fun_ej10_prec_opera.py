'''Ejercicio 10: Precedencia del operador

Escriba una función llamada precedencia que devuelve un número entero que representa la precedencia de un 
operador matemático. Una cadena que contiene el operador se pasará a la función como su único parámetro. 
Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ˆ. Si la cadena que se pasa a la función no 
es uno de estos operadores, la función debería devolver -1. Incluya un programa principal que lea un 
 del usuario y muestre la precedencia del operador o un mensaje de error que indique que la entrada no era 
 un operador.

En este ejercicio, se usa ˆ para representar la exponenciación, en lugar de la elección de Python de **, 
para facilitar el desarrollo de la solución.'''
from funciones import limpiar_pantalla, muestro_mensaje

def precedencia(operador):
    if operador in "+-":
        return 1
    elif operador in "*/":
        return 2
    elif operador == "ˆ":
        return 3
    else:
        return -1


if __name__== "__main__":
    sigo = True
    while sigo:
        limpiar_pantalla()
        muestro_mensaje("SUMA(+) - RESTA(-) - MULTIPLICACION (*) - DIVISION(/) - EXPONENCIACION(ˆ)")
        operador = input("\n\tINGRESE UN OPERADOR MATEMATICO (Enter para salir): ")
        if operador == "":
            break
        orden = precedencia(operador)
        mensaje_continua = True
        if orden > 0:
            muestro_mensaje(f"LA PRECEDENCIA ES {orden}", mensaje_continua)
        else:
            muestro_mensaje(f"ERROR - NO INGRESO UN OPERADOR!!!", mensaje_continua)
    limpiar_pantalla()
    muestro_mensaje("GRACIAS POR VENIR")

