'''Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada 
indicando: los tres atributos, sólo la hora y minuto,o sólo la hora. Crear además los métodos 
necesarios para modificar la hora en cualquier momento de forma manual. Mantenga la integridad 
de los datos en todo momento definiendo de tipo “private”. Crear  una  clase prueba_tiempo que 
 prueba  una  hora  concreta  y  la  modifique  a  su  gusto  mostrándola  por pantalla.'''

import os
import random


class Tiempo:
    def __init__(self, hora, minutos, segundos):
        if hora == "":
            self.__hora = "00"
            print("\tNo se recibio atributo Hora, se establece 00")
            self.__prueba_hora = True
        elif hora.isdigit() and hora in [str(x) for x in range(24)]:
            self.__hora = hora
            print("\tHora establecida!")
            self.__prueba_hora = True
        else:
            print("\tSe recibieron valores errados, Verifique!")
            self.__prueba_hora = False
            
        
        if minutos =="":
            self.__minutos = "00"
            print("\tNo se recibio atributo Minutos, se establece 00")
            self.__prueba_minutos = True
        elif minutos.isdigit() and minutos in [str(x) for x in range(60)]:
            self.__minutos = minutos
            print("\tMinutos establecidos!")
            self.__prueba_minutos = True
        else:
            print("\tSe recibieron valores errados, Verifique!")
            self.__prueba_minutos = False
            

        if segundos == "":
            self.__segundos = "00"
            print("\tNo se recibio atributo Segundos, se establece 00")
            self.__prueba_segundos = True
        elif segundos.isdigit() and segundos in [str(x) for x in range(60)]:
            self.__segundos = segundos
            print("\tSegundos establecidos!")
            self.__prueba_segundos = True
        else:
            print("\tSe recibieron valores errados, Verifique!")
            self.__prueba_segundos = False
        
        if not self.__prueba_segundos or not self.__prueba_minutos or not self.__prueba_hora:
            self.__hora = None
            self.__minutos = None
            self.__segundos = None
            
    def setHora(self, hora):
        if hora.isdigit() and hora in [str(x) for x in range(24)]:
            self.__hora = hora
            print("\tHora Modificada")
            self.__modif_hora = True
        else:
            print("\tSe deja hora como esta (se recibien valores errados o vacio)")
            self.__modif_hora = False

    def setMinutos(self, minutos):
        if minutos.isdigit() and minutos in [str(x) for x in range(60)]:
            self.__minutos = minutos
            print("\tMinutos Modificados")
            self.__modif_minutos = True
        else:
            print("\tSe deja minutos como esta (se recibien valores errados o vacio)")
            self.__modif_minutos = False

    def setSegundos(self, segundos):
        if segundos.isdigit() and segundos in [str(x) for x in range(60)]:
            self.__segundos = segundos
            print("\tSegundos Modificados")
            self.__modif_segundos = True
        else:
            print("\tSe deja segundos como esta (se recibien valores errados o vacio)")
            self.__modif_segundos = False

    def resultadoInstancia(self):
        if self.getHora() and self.getMinutos() and self.getSegundos():
            return "\tPrueba exitosa, instanciacion correcta"
            
        else:
            return "\tLa instanciacion fallo, verifique!"

    def resultadoModificacion(self):
        if self.__modif_hora and self.__modif_minutos and self.__modif_segundos:
            return "\tPrueba exitosa, modificacion correcta"
            
        else:
            return "\tLa modificacion fallo, verifique!"

    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__minutos

    def getSegundos(self):
        return self.__segundos

    

class Prueba_tiempo:

    def genero_random(self, correctos = True):
        if correctos:
            inicio_hora = 0
            fin_hora = 23
            inicio_resto = 0
            fin_resto = 59
        else:
            inicio_hora = 24
            fin_hora = 100
            inicio_resto = 60
            fin_resto = 100

        hora = random.randint(inicio_hora,fin_hora)
        minutos = random.randint(inicio_resto, fin_resto)
        segundos = random.randint(inicio_resto, fin_resto)

        return [str(hora), str(minutos), str(segundos)]

    def prueba_correcta(self):
        print("\tGenerando horas, minutos y segundos aleatorios")
        hora_prueba, minutos_prueba, segundos_prueba = self.genero_random()
        print(f"\tHora: {hora_prueba}")
        print(f"\tMinutos: {minutos_prueba}")
        print(f"\tSegundos: {segundos_prueba} ")
        print("\tInstanciando valores creados...")
        prueba_correctos = Tiempo(hora_prueba, minutos_prueba, segundos_prueba)
        print(prueba_correctos.resultadoInstancia())
        print(f"\tHora actual: {prueba_correctos.getHora()}:{prueba_correctos.getMinutos()}:{prueba_correctos.getSegundos()}")
        print("\tGenerando horas, minutos y segundos aleatorios para modificacion")
        hora_prueba, minutos_prueba, segundos_prueba = self.genero_random()
        print(f"\tHora: {hora_prueba}")
        print(f"\tMinutos: {minutos_prueba}")
        print(f"\tSegundos: {segundos_prueba} ")
        print("\tAplicando modificaciones...")
        prueba_correctos.setHora(hora_prueba)
        prueba_correctos.setMinutos(minutos_prueba)
        prueba_correctos.setSegundos(segundos_prueba)
        print(prueba_correctos.resultadoModificacion())
        print(f"\tHora actual: {prueba_correctos.getHora()}:{prueba_correctos.getMinutos()}:{prueba_correctos.getSegundos()}")
        input()

    def prueba_incorrecta(self):
        print("\tGenerando horas, minutos y segundos aleatorios incorrectos")
        hora_prueba, minutos_prueba, segundos_prueba = self.genero_random(correctos = False)
        print(f"\tHora: {hora_prueba}")
        print(f"\tMinutos: {minutos_prueba}")
        print(f"\tSegundos: {segundos_prueba} ")
        print("\tInstanciando valores creados...")
        prueba_incorrectos = Tiempo(hora_prueba, minutos_prueba, segundos_prueba)
        print(prueba_incorrectos.resultadoInstancia())
        print("\tGenerando horas, minutos y segundos aleatorios para modificacion")
        hora_prueba, minutos_prueba, segundos_prueba = self.genero_random(correctos = False)
        print(f"\tHora: {hora_prueba}")
        print(f"\tMinutos: {minutos_prueba}")
        print(f"\tSegundos: {segundos_prueba} ")
        print("\tAplicando modificaciones...")
        prueba_incorrectos.setHora(hora_prueba)
        prueba_incorrectos.setMinutos(minutos_prueba)
        prueba_incorrectos.setSegundos(segundos_prueba)
        print(prueba_incorrectos.resultadoModificacion())
        input()



            

if __name__== "__main__":
    hora = ""
    primera_vez = True
    while True:
        os.system("cls")
        if primera_vez:
            print(f"\n\t1 - Inicio hora? \n\tEnter para salir")
            respuesta = input()
            if respuesta == "":
                break               
            elif respuesta == "1":
                horas = input("\tIngrese las Horas (Enter inicia en cero)").strip()
                minutos = input("\tIngrese los Minutos (Enter inicia en cero)").strip()
                segundos = input("\tIngrese los Segundos (Enter inicia en cero)").strip()
                nuevo_tiempo = Tiempo(horas, minutos, segundos)
                input()
                if nuevo_tiempo.getHora():
                    primera_vez = False
        else:
            print(f"\n\thora iniciada {nuevo_tiempo.getHora()}:{nuevo_tiempo.getMinutos()}:{nuevo_tiempo.getSegundos()}\n\t2 - Modifica hora \n\t3 - Prueba Automatica \n\tEnter para salir")
            respuesta = input()
            if respuesta == "":
                break               
            elif respuesta == "2":
                horas = input("\tIngrese las Horas (Enter sin cambios)").strip()
                nuevo_tiempo.setHora(horas)
                input()
                minutos = input("\tIngrese los Minutos (Enter sin cambios)").strip()
                nuevo_tiempo.setMinutos(minutos)
                input()
                segundos = input("\tIngrese los Segundos (Enter sin cambios)").strip()
                nuevo_tiempo.setSegundos(segundos)
            elif respuesta == "3":
                testing = Prueba_tiempo()
                testing.prueba_correcta()
                testing.prueba_incorrecta()
                
        
        