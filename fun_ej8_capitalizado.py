'''Ejercicio 8: Capitalízalo

Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos 
pequeños como teléfonos inteligentes. En este ejercicio, escribirá una función que capitaliza los caracteres 
apropiados en una cadena. Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y 
seguida de un espacio. El primer carácter de la cadena también debe estar en mayúscula, así como el primer 
carácter no espacial después de un ".", "!" o "?" Por ejemplo, si la función se proporciona con la cadena 
"¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué hora 
tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa principal que lea una cadena del usuario, 
la capitalice utilizando su función y muestre el resultado.'''

from funciones import muestro_mensaje, limpiar_pantalla

def capitalizar(texto):
    espa_o_signo = False
    espacio_antes = False
    largo = len(texto)
    nro_letra = 0
    nuevo_texto = ""
    for cada_letra in texto:

        if nro_letra == 0 and cada_letra not in ".¡!¿?":
            nuevo_texto += cada_letra.upper()
            nro_letra += 1

        elif cada_letra in ".¡!¿?":
            espa_o_signo = True
            nuevo_texto += cada_letra
            nro_letra += 1
        
        elif cada_letra == " ":
            espacio_antes = True
            nuevo_texto += cada_letra
        
        elif espa_o_signo or espacio_antes and cada_letra == "i":
            nuevo_texto += cada_letra.upper()
            nro_letra += 1
            espa_o_signo = False
        
        else:
            nuevo_texto += cada_letra
    return nuevo_texto

if __name__ == "__main__":
    sigo = True
    muestro_continua = True
    while sigo:
        limpiar_pantalla()
        texto = input("\tIngrese una texto para capitalizar (Presione Enter Para salir):")
        if texto == "":
            sigo = False
            continue
        muestro_mensaje(capitalizar(texto), muestro_continua)
    limpiar_pantalla()
    muestro_mensaje("Gracias Por Venir")


            

        


