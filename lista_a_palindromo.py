from funciones import muestro_mensaje, limpiar_pantalla

def es_palindromo(palabra):
    return str(palabra == palabra[::-1])
        

sigo = True
muestro_continua = True
while sigo:
    limpiar_pantalla()
    palabra = input("\Ingrese una palabra para probar(Presione Enter para salir): ")
    if palabra == "":
        sigo = False
        continue
    muestro_mensaje(es_palindromo(palabra), muestro_continua)
limpiar_pantalla()
muestro_mensaje("Gracias por venir")