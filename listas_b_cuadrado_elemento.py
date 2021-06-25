'''b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada 
componente sea igual al cuadrado del componente original. El programa mostrara la lista resultante por 
pantalla.'''

from funciones import limpiar_pantalla, muestro_mensaje


def elevar_lista(lista):
    return [x**2 for x in lista]

def es_numero(elemento):
    for cada_letra in elemento:
            if cada_letra.lower() in "abcdefghijkllmnopqrstuvwxyz":
               
                return False
    return True    

if __name__ == "__main__":
    sigo = True
    lista = list()
    muestro_continua=True
    while sigo:
        limpiar_pantalla()
        sigo2= True
        while sigo2:
            elemento = input("\tIngrese un numero (Para Salir presione Enter):")
            if elemento == "":
                sigo = False
                break

            if es_numero(elemento):
                lista.append(int(elemento))
            else:
                muestro_mensaje("ERROR...Debe ingresar un numero.....", muestro_continua)
                continue
            muestro_mensaje(f"La lista tiene {len(lista)} elementos")

        if lista:
            muestro_mensaje(f"La lista original es:\n\t{lista}")
            muestro_mensaje(f"La lista elevada al cuadrado es:\n\t{elevar_lista(lista)}", muestro_continua)
            lista = list()
            sigo = True

    limpiar_pantalla()
    muestro_mensaje("Gracias por Venir")    
     