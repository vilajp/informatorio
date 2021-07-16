'''Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra 
mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que 
muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También 
debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía 
el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.'''
import os

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getRuedas(self):
        return self.ruedas

    def setRuedas(self, ruedas):
        self.ruedas = ruedas

    def mostrar_atributos(self):
        return f"color: {self.color}\ncon {self.ruedas} ruedas"

    

class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        
        self.velocidad = velocidad
        self.cilindrada = cilindrada  
        super().__init__(color, "4")
          

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, v):
        self.velocidad = v

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self):
        self.cilindrada = c

    def __str__(self):
        return "Coche"

    def mostrar_atributos(self):
        return super().mostrar_atributos() + f"\ncon velocidad: {self.velocidad} \ny {self.cilindrada}cc de cilindrada"
    
    

class Camioneta(Coche):
    
    def __init__(self, color, velocidad, cilindrada, carga):
        self.carga = carga
        super().__init__(color, velocidad, cilindrada)
    
    def getCarga(self):
        return self.carga

    def setCarga(self, carga):
        self.carga = carga

    def __str__(self):
        return "Camioneta"

    def mostrar_atributos(self):
        return super().mostrar_atributos() + f"\npuedo llevar una carga de {self.carga} kgs" 
    
    
class Bicicleta(Vehiculo):
    
    def __init__(self, color, tipo):
        self.tipo = tipo
        super().__init__(color, "2")
        

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def __str__(self):
        return "Bicicleta"

    def mostrar_atributos(self, moto=False):
        if moto:
            return super().mostrar_atributos()
        else:
            return super().mostrar_atributos() + f" \ny mi tipo es {self.tipo}"
    
    

class Motocicleta(Bicicleta):
    def __init__(self, color, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(color,  None)

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, v):
        self.velocidad = v

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self):
        self.cilindrada = c
    
    def __str__(self):
        return "Motocicleta"
    
    def mostrar_atributos(self):
        return super().mostrar_atributos(moto = True) + f" mi cilindrada es {self.cilindrada}cc \ny mi velocidad es {self.velocidad} km/h"

def catalogar(vehiculos, ruedas = "todas", conteo = 0):
             
    for cada_vehiculo in vehiculos: 
        if ruedas == "todas":
            print("*************************************")  
            print(type(cada_vehiculo).__name__)
            print(cada_vehiculo.mostrar_atributos())
            
        elif ruedas == cada_vehiculo.getRuedas():
            conteo +=1
    if ruedas !="todas":
        print(f"Se han encontrado {conteo} vehículos con {ruedas} ruedas:")
    input() 


if __name__=="__main__":
    os.system("cls")
    vehiculos = list()
    while True:
        os.system("cls")
        print(f"Hay {len(vehiculos)} cargados hasta ahora")
        print("Que tipo de vehiculo desea ingresar:\n1 - Coche  \n2 - Camioneta \n3 - Bicicleta \n4 - Motocicleta \nEnter para salir: \r")
        respuesta = input()

        if not respuesta:
            break

        if respuesta == "1":
            print("Ud eligio cargar un coche!")
            color = input("Ingrese Color:")
            cilindrada = input("Ingrese Cilindrada:")
            velocidad = input("Ingrese Velocidad:")
            nuevo_coche = Coche(color, velocidad, cilindrada)

            vehiculos.append(nuevo_coche)
        
        elif respuesta == "2":
            print("Ud eligio cargar una Camioneta!")
            color = input("Ingrese Color:")
            cilindrada = input("Ingrese Cilindrada:")
            velocidad = input("Ingrese Velocidad:")
            carga = input("Ingrese Carga:")
            nueva_camioneta = Camioneta(color, velocidad, cilindrada, carga)

            vehiculos.append(nueva_camioneta)
        
        elif respuesta == "3":
            while True:
                tipos = {"1":"Urbana", "2": "Deportiva"}
                print("Ud eligio cargar un Bicicleta!")
                color = input("Ingrese Color:")
                tipo = input("Ingrese Tipo (1-Urbana - 2-Deportiva):")
            
                if tipo in [str(x) for x in range(1,3)]:
                    nueva_bici = Bicicleta(color, tipos[tipo])
                    vehiculos.append(nueva_bici)
                    break
                else:
                    print("Error, no es un tipo de Bicicleta!")
        
        else:
            print("Ud eligio cargar una Motocicleta!")
            color = input("Ingrese Color:")
            cilindrada = input("Ingrese Cilindrada:")
            Velocidad = input("Ingrese Velocidad:")
            nueva_moto = Motocicleta(color, velocidad, cilindrada)
            vehiculos.append(nueva_moto)

    while True:
        os.system("cls")
        print(f"Tiene cargados {len(vehiculos)} vehiculos\n")
        print("\n1 - Listar todos los Vehiculos y sus atributos \n2 - Listar por cantidad de Ruedas \nPresione Enter para salir")
        opcion = input("Ingrese una opcion:")
        if opcion == "":
            break
        elif opcion == "1":
            catalogar(vehiculos)
        elif opcion == "2":
            nro_ruedas = input("Ingrese el nro de ruedas a buscar:")
            if nro_ruedas in [str(x) for x in range(9)]:
                catalogar(vehiculos, nro_ruedas)    