'''Escriba dos funciones, hex2int e int2hex, que conviertan entre dígitos hexadecimales (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) 
y enteros de base 10. La función hex2int es responsable de convertir una cadena que contiene un solo dígito hexadecimal en un entero de 
base 10, mientras que la función int2hex es responsable de convertir un entero entre 0 y 15 en un solo dígito hexadecimal. Cada función 
tomará el valor para convertir como su único parámetro y devolverá el valor convertido como el único resultado de la función. 
Asegúrese de que la función hex2int funcione correctamente para letras mayúsculas y minúsculas. 
Sus funciones deberían finalizar el programa con un mensaje de error significativo si se proporciona un parámetro no válido.'''
from funciones import limpiar_pantalla, hacer_menu, muestro_mensaje

def hex2int(numero):
    vuelta = 0
    hexadecimales="0123456789ABCDEF"
    for cada_hexa in hexadecimales:
        if cada_hexa == numero:
            return str(vuelta)
        vuelta +=1


def int2hex(numero):
    hexadecimales="0123456789ABCDEF"
    vuelta = 0
    for cada_hexa in hexadecimales:
        if vuelta == numero:
            return cada_hexa
        vuelta += 1

 

if __name__ == "__main__":
    opcion = 0
    while opcion != 3 :
        limpiar_pantalla()
        opcion = hacer_menu("1 - Convertir Hexadecimal a Entero", "2 - Convertir Entero a Hexadecimal", "3 - Salir")
        mensaje_continuar = True
        if opcion == 1:
            sigo = True
            while sigo:   
                limpiar_pantalla() 
                num_hexa = input("\tIngrese un numero hexadecimal entre 0 y F: ")
                if len(num_hexa)>1 or num_hexa.upper() not in "0123456789ABCDEF":
                    muestro_mensaje("ATENCION debe ingresar un numero hexadecimal entre 0 y F!!!!!", 
                    mensaje_continuar)
                else:
                    sigo = False
            muestro_mensaje(f"El numero entero correspondiente a {num_hexa.upper()} es: {hex2int(num_hexa.upper())}", 
                    mensaje_continuar)
            
        elif opcion == 2:
            sigo = True
            while sigo:
                limpiar_pantalla()    
                num_entero = input("\tIngrese un numero entero entre 0 y 15:")
                if num_entero in "0123456789101112131415": 
                    if int(num_entero) in range(1,16): 
                        sigo = False
                        muestro_mensaje(f"El numero hexadecimal correspondiente a {num_entero} es: {int2hex(int(num_entero))}",
                          mensaje_continuar) 
                    else :
                        muestro_mensaje("ATENCION debe ingresar un numero entero entre 0 y 15!!!!!",
                        mensaje_continuar)
                
            

    limpiar_pantalla()
    muestro_mensaje("******Gracias por venir!!!********")