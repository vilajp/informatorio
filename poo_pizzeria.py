'''Una pizzería de la ciudad ofrece a sus clientes una amplia variedad de pizzas de fabricación propia,
varios tamaños (8, 10 y 12 porciones). 

Los clientes tienen a disposición un menú que describe para cada una de las variedades, el nombre, 
los ingredientes y el precio según el tamaño y el tipo (a la piedra, a la parrilla, de molde) de la 
pizza. Los clientes realizan sus pedidos en el mostrador. El pedido debe contener el nombre del 
Cliente, para llamarlo cuando su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, 
la fecha del pedido, la hora en la que el pedido debe entregarse y la demora estimada informada al 
cliente. El pedido va a la cocina y cuando está preparado se informa al que lo tomó para que se genere
 la factura correspondiente y se le entregue el pedido al cliente. 

El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la siguiente información: 

Variedades y tipos de pizzas más pedidas por los clientes. 

Ingresos (recaudaciones) por períodos de tiempo. 

Pedidos (cantidad y monto) por períodos de tiempo. 

Implementar un programa en Python que resuelva este caso de estudio a través de clases y métodos.
'''
import os
from datetime import datetime

class Pizzeria:
    def __init__(self):
        self.pedidos = list()
        self.facturas = list()

        def tomo_pedido(self, un_pedido):
            self.pedidos.append(un_pedido)

        def getPedidos(self):
            return self.pedidos

        def cargofactura(self, una_factura):
            self.facturas.append(una_factura)

        def pizzas_mas_pedidas(self):
            pass

        def ingresos_por_tiempo(self):
            pass

        def pedidos_por_tiempo(self):
            pass          

class Factura:
    def __init__(self, cliente, descripcion):
        self.cliente = cliente
        self.descripcion = descripcion

class Pizza:
    def __init__(self, tamaño, tipo, cantidad):     
        self.tamaño = tamaño
        self.tipo = tipo
        self.cantidad = cantidad
        self.precios = {"piedra":{"8":500, "10":600, "12":700},
        "parrilla":{"8":500, "10":600, "12":700},
        "molde":{"8":500, "10":600, "12":700}}

    def getTamaño(self):
        return self.tamaño
    
    def gettipo(self):
        return self.tipo
    
    def getCantidad(self):
        return self.cantidad

class Pedido:
        pedido = 0
    def __init__(self, nombre_cliente, demora_estimada):
        self.numero_pedido = pedido + 1
        self.nombre_cliente = nombre_cliente
        self.pizzas = list()
        self.now = datetime.now()
        self.fecha = "-".join(reversed(str(self.now.date()).split("-")))
        self.hora_entrega = self.calculo_demora(demora_estimada)

    def cargo_pizza(self, pizza_pedida):
        self.pizzas.append(pizza_pedida)

    def calculo_demora(self, demora):
        self.hora_actual = str(self.now.time()).split(".")[0]
        hora, minutos, segundos = self.hora_actual.split(":")
        hora_en_segundos = int(hora)*3600 + int(minutos)*60 + int(segundos)
        hora_demora_en_segundos = hora_en_segundos + int(demora)*60
        hora_demora = int(hora_demora_en_segundos /3600)
        minutos_demora = int((hora_demora_en_segundos%3600)/60)
        segundos_demora = int((hora_demora_en_segundos%3600)%60)
        hora, minutos, segundos = ["0"+ str(x) if len(str(x))<2 else str(x) for x in [hora_demora, minutos_demora, segundos_demora] ]
        return f"{hora}:{minutos}:{segundos}"

    def muestro_pedido(self):
        return [self.nombre_cliente, self.fecha, self.now.time(), self.hora_entrega]


if __name__=="__main__":
    os.system("cls")
    nuevo_pedido = Pedido("juan Pablo", "30")
    otro_pedido = Pedido("Andrea", "25")
    while True:
        print("\tBienvenido a Pizzeria Rica Pizza!")
        print("\t*********************************")
        print("\tSeleccione una opcion: \n1 - Nuevo Pedido \n2 - Genero Factura \n3 - Listo Pizzas mas pedidas \n4 - Recaudacion por hora \n5 - Pedidos por hora \n Enter para Salir")
        respuesta = input("\t")
        if respuesta == "":
            break
        
        elif respuesta == "1":
            os.system("cls")
            cliente = input("\tIngrese Nombre del Cliente:")
        
        for datos in nuevo_pedido.muestro_pedido():
            print(datos)

