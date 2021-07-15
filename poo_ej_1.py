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

    def setColor(self, ruedas):
        self.ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        
        self.velocidad = velocidad
        self.cilindrada = cilindrada  
        super().__init__(color, ruedas)
          

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, v):
        self.velocidad = v

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self):
        self.cilindrada = c


coche1 = Coche("azul",4 , 200, 125)

print(coche1.getColor(), coche1.getRuedas(), coche1.getVelocidad(), coche1.getCilindrada())