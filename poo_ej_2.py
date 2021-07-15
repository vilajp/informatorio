import os

class Vehiculo:
    def __init__(self, color):
        self.color = color
        

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getRuedas(self):
        return self.ruedas

    def setColor(self, ruedas):
        self.ruedas = ruedas

    def __str__(self):
        return self.color


class Coche(Vehiculo):
    def __init__(self, color, velocidad, cilindrada):
        self.ruedas = "4"
        self.velocidad = velocidad
        self.cilindrada = cilindrada  
        super().__init__(color)
          

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, v):
        self.velocidad = v

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self):
        self.cilindrada = c
    
    def __str__(self):
        return "-".join([self.color, self.ruedas, self.velocidad, self.cilindrada])

class Camioneta(Coche):
    
    def __init__(self, color, velocidad, cilindrada, carga):
        self.carga = carga
        super().__init__(color, velocidad, cilindrada)
    
    def getCarga(self):
        return self.carga

    def setCarga(self, carga):
        self.carga = carga
    
    def __str__(self):
        return "-".join([Coche.__str__(self), self.carga])


class Bicicleta(Vehiculo):
    
    def __init__(self, color, tipo):
        self.tipo = tipo
        self.ruedas = "2"
        super().__init__(color)
        

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "-".join([self.color, self.ruedas, self.tipo])


class Motocicleta(Bicicleta):
    def __init__(self, color, velocidad, cilindrada, tipo = None):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(color, tipo)

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, v):
        self.velocidad = v

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self):
        self.cilindrada = c
    
    def __str__(self):
        return "-".join([self.color, self.ruedas, self.velocidad, self.cilindrada])

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
            tipos = {"1":"Urbana", "2": "Deportiva"}
            print("Ud eligio cargar un Bicicleta!")
            color = input("Ingrese Color:")
            tipo = input("Ingrese Tipo (1-Urbana - 2-Deportiva):")
            
            nueva_bici = Bicicleta(color, tipos[tipo])

            vehiculos.append(nueva_bici)
        
        else:
            print("Ud eligio cargar una Motocicleta!")
            color = input("Ingrese Color:")
            cilindrada = input("Ingrese Cilindrada:")
            Velocidad = input("Ingrese Velocidad:")
            nueva_moto = Motocicleta(color, velocidad, cilindrada)
            vehiculos.append(nueva_moto)

    for cada_vehiculo in vehiculos:   
        print(cada_vehiculo)