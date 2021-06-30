'''c. Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega y se 
ubica en la cola de menor cantidad de personas. Al finalizar el proceso indique cuántos elementos tiene cada 
cola.'''

from funciones import limpiar_pantalla, muestro_mensaje, hacer_menu
from random import randint

cola1 = list()
cola2 = list()
sigo = True
primera_vez = True
mensaje_continua = True
turno = ""
salio = 0
while sigo:
    
    movimiento = input("Presione Enter para simular el movimiento (Presione '*' para salir): ")
    if movimiento == "*":
        sigo = False
        continue
    else:    
        llego = randint(0,1)
        if llego:
            limpiar_pantalla()
            muestro_mensaje("Llego alguien!!!!")
            
            if len(cola1)==len(cola2):
                cola_llega = str(randint(1,2))
                if cola_llega == "1":
                    cola1.append("*")
                elif cola_llega == "2":
                    cola2.append("*")
            elif len(cola1)<len(cola2):
                    cola1.append("*")
            elif len(cola1)>len(cola2):
                    cola2.append("*")

            muestro_mensaje(f"La cola 1 esta asi: {cola1}")
            muestro_mensaje(f"La cola 2 esta asi: {cola2}")

        if cola1 or cola2:
            salio = randint(0,1)

            if salio:
                
                muestro_mensaje("Salio alguien!!!!")
                
                if  cola1 and cola2:
                    cola_sale = str(randint(1,2))
                    if cola_sale == "1":
                        cola1.pop()
                        
                    else:
                        cola2.pop()
                        
                elif cola1:
                        cola1.pop()
                elif cola2:
                        cola2.pop()

                muestro_mensaje(f"La cola 1 esta asi: {cola1}")
                muestro_mensaje(f"La cola 2 esta asi: {cola2}")
            

limpiar_pantalla()
muestro_mensaje(f"La cola 1 termino con {len(cola1)} personas")
muestro_mensaje(f"La cola 2 termino con {len(cola2)} personas")


    
    
     