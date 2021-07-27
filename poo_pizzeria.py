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
import random

class Pizzeria:
    def __init__(self):
        self.pedidos = list()
        self.facturas = list()
        self.pedidos_historicos = list()

    def tomo_pedido(self, un_pedido):
        self.pedidos.append(un_pedido)
        self.pedidos_historicos.append(un_pedido)

    def getPedidos(self):
        return self.pedidos

    def elimino_pedido(self, pedido):
        self.pedidos.remove(pedido)
        

    def cargofactura(self, una_factura):
        self.facturas.append(una_factura)


    def getFacturas(self):
        return self.facturas

    def getPedidos_historicos(self):
        return self.pedidos_historicos

    def pizzas_mas_pedidas(self):
        contador = dict()
        os.system("cls")
        
        for cada_pedido in self.getPedidos_historicos():
            for cada_pizza in cada_pedido.muestro_pedido()[1]:
                if not cada_pizza[0]+"-"+cada_pizza[1] in contador.keys():
                    contador[cada_pizza[0]+"-"+cada_pizza[1]]=  0
                    contador[cada_pizza[0]+"-"+cada_pizza[1]] += int(cada_pizza[3])
                else:
                    contador[cada_pizza[0]+"-"+cada_pizza[1]] += int(cada_pizza[3])
        
        
        
        ranking = dict()
        while len(contador):
            pizza_mas_pedida, cantidad_mas_pedida = busco_mayor(contador)
            
            ranking[pizza_mas_pedida] = cantidad_mas_pedida
            del contador[pizza_mas_pedida]
        print("\t*********************************")    
        print("\tListado de pizzas mas solicitadas")
        print("\t*********************************")
        print()
        for pizza, cantidad in ranking.items():
            print(f"\tPizza Variedad {pizza.split('-')[0]} de {pizza.split('-')[1]} porciones --> {cantidad}")


    def ingresos_por_tiempo(self):
        os.system("cls")
        fecha_inicio = input("\tIngrese fecha inicio de busqueda(dd-mm-aaaa):\t")
        fecha_fin = input("\tIngrese fecha final de busqueda(dd-mm-aaaa):\t")
        hora_inicio = input("\tIngrese hora de inicio Actividad(hh:mm):\t")
        hora_fin = input("\tIngrese hora fin de Actividad(hh:mm):\t")
        intervalo = input("\tIngrese el intervalo de tiempo a evaluar en minutos:\t")

        # [self.fecha, self.cliente, self.descripcion, self.total_factura, self.hora_actual]
        hora_intervalo = horas_a_segundos(hora_inicio, intervalo)
        while horas_a_segundos(hora_intervalo) <= horas_a_segundos(hora_fin):
            for cada_factura in self.getFacturas():
                
                if doy_vuelta_fecha(fecha_inicio) <= doy_vuelta_fecha(cada_factura[0]) <= doy_vuelta_fecha(fecha_fin):
                    
                    if horas_a_segundos(hora_inicio)<= horas_a_segundos(cada_factura[4])<=horas_a_segundos(hora_intervalo):
                        print(f"\t*****{hora_inicio}*******{hora_intervalo}**********")
                        print("\t"+cada_factura[0], cada_factura[4], cada_factura[1], cada_factura[3])
            
            hora_inicio = hora_intervalo
            
            hora_intervalo = horas_a_segundos(hora_inicio, intervalo)
            print(f"\t*******************************************************************************")



    def pedidos_por_tiempo(self):
        pass          

def doy_vuelta_fecha(fecha, separador = ""):
    if not separador:
        return int(separador.join(reversed(fecha.split("-"))))
    else:
        return separador.join(reversed(fecha.split("-")))

class Factura:
    def __init__(self, pedido_facturar):
        self.cliente = pedido_facturar.muestro_pedido()[0]
        self.descripcion = pedido_facturar.muestro_pedido()[1]
        self.fecha = pedido_facturar.muestro_pedido()[2]
        self.hora_pedido = pedido_facturar.muestro_pedido()[3]
        self.total_factura = 0
        self.now = datetime.now()
        self.hora_actual = str(self.now.time()).split(".")[0]

    def genero_factura(self):
        
        print("\t**************************************************")
        print(f"\tCliente: {self.cliente}  Resistencia,{self.fecha}")
        print("\t**************************************************")
        print("\tVariedad\tTamaño Pizza\tCantidad\tTotal Parcial")
        for cada_item in self.descripcion:
            variedad, porciones, precio, cantidad = cada_item
            total_parcial = precio * int(cantidad)
            print(f"\t{variedad}\t{porciones} porciones\t{cantidad}\t{total_parcial}")
            self.total_factura += total_parcial
        print(f"\t Total a pagar: \t{self.total_factura}")
        return [self.fecha, self.cliente, self.descripcion, self.total_factura, self.hora_actual]
    




class Menu:
    def __init__(self):
        self.pizza = {"piedra":{"8":500, "10":600, "12":700},
        "parrilla":{"8":500, "10":600, "12":700},
        "molde":{"8":500, "10":600, "12":700}}

    def seleccion_pizza(self):
        lista_pizzas = list(self.pizza.keys())
        
        while True:
            items = 1
            print("\tSeleccione su pizza")
            for cada_pizza in self.pizza.keys():
                print(f"\t{items} - {cada_pizza}")
                items +=1
            respuesta = input("\tSeleccione su pizza:\t")
            if respuesta in [str(n) for n in range(1, len(lista_pizzas)+1)]:
                variedad = lista_pizzas[int(respuesta)-1]
                break
            else:
                print("\tRespuesta incorrecta! intente nuevamente")
                input()
        lista_porciones = list(self.pizza[variedad].keys())
        
        while True:
            items = 1
            print("\tSeleccione cantidad de porciones!")
            for cada_porcion in self.pizza[variedad].keys():
                print(f"\t{items} - {cada_porcion} porciones")
                items +=1
            respuesta = input("\tSeleccione su opcion:\t")
            if respuesta in [str(n) for n in range(1,len(lista_porciones)+1)]:
                porcion = lista_porciones[int(respuesta)-1]
                break
            else:
                print("\tRespuesta incorrecta! intente nuevamente")
                input()
        precio = self.pizza[variedad][porcion]
        return [variedad, porcion, precio]




class Pedido:
    
    def __init__(self, nombre_cliente):
        
        self.nombre_cliente = nombre_cliente
        self.pizzas = list()
        self.now = datetime.now()
        self.fecha = doy_vuelta_fecha(str(self.now.date()),"-")
        self.hora_entrega = ""

    def cargo_pizza(self, pizza_pedida):
        self.pizzas.append(pizza_pedida)
        
    def cargo_demora(self, demora_estimada):
        self.hora_entrega = self.calculo_demora(demora_estimada)


    def calculo_demora(self, demora):
        self.hora_actual = str(self.now.time()).split(".")[0]
        hora, minutos, segundos = self.hora_actual.split(":")
        horas_a_segundos = int(hora)*3600 + int(minutos)*60 + int(segundos)
        hora_demora_en_segundos = horas_a_segundos + int(demora)*60
        hora_demora = int(hora_demora_en_segundos /3600)
        minutos_demora = int((hora_demora_en_segundos%3600)/60)
        segundos_demora = int((hora_demora_en_segundos%3600)%60)
        hora, minutos, segundos = ["0"+ str(x) if len(str(x))<2 else str(x) for x in [hora_demora, minutos_demora, segundos_demora] ]
        return f"{hora}:{minutos}:{segundos}"

    def muestro_pedido(self):
        return [self.nombre_cliente, self.pizzas, self.fecha, self.hora_actual, self.hora_entrega]


def cargo_datos():
    pedido1 = Pedido("Andrea Miron")
    pedido2 = Pedido("Dulcinea Vila")
    pedido3 = Pedido("Django Vila")
    pizza_selecc_pedido1 =["piedra","10",600, "1"]
    pizza2_selecc_pedido1 = ["parrilla","12",700, "2"]
    pizza_selecc_pedido2 =["molde","10",600, "1"]
    pizza2_selecc_pedido2=["molde","10",600, "2"]
    pizza_selecc_pedido3 =["piedra","12",700, "1"]
    pizza2_selecc_pedido3 =["parrilla","10",600, "2"]
    pedido1.cargo_pizza(pizza_selecc_pedido1)
    pedido1.cargo_pizza(pizza2_selecc_pedido1)
    pedido2.cargo_pizza(pizza_selecc_pedido2)
    pedido2.cargo_pizza(pizza2_selecc_pedido2)
    pedido3.cargo_pizza(pizza_selecc_pedido3)
    pedido3.cargo_pizza(pizza2_selecc_pedido3)
    pedido1.cargo_demora("40")
    pedido2.cargo_demora("50")
    pedido3.cargo_demora("30")
    pizzeria.tomo_pedido(pedido1)
    pizzeria.tomo_pedido(pedido2)
    pizzeria.tomo_pedido(pedido3)

def horas_a_segundos(hora_origen, incremento = "0"):
    hora, minutos, segundos = hora_origen.split(":")
    horas_a_segundos = int(hora)*3600 + int(minutos)*60 + int(segundos)
    if incremento == "0":
        return horas_a_segundos
    hora_demora_en_segundos = horas_a_segundos + int(incremento)*60
    hora_demora = int(hora_demora_en_segundos /3600)
    if hora_demora > 23:
        hora_demora -= 24
    minutos_demora = int((hora_demora_en_segundos%3600)/60)
    segundos_demora = int((hora_demora_en_segundos%3600)%60)
    hora, minutos, segundos = ["0"+ str(x) if len(str(x))<2 else str(x) for x in [hora_demora, minutos_demora, segundos_demora] ]
    return f"{hora}:{minutos}:{segundos}"

def cargo_facturas():
    # [self.fecha, self.cliente, self.descripcion, self.total_factura, self.hora_actual]
    nombres = ["Andrea","Django","Dulcinea","Juan Pablo","Carlos", "Nicolas", "Gonzalo", "Andrea", "Hugo"]
    apellidos = ["Miron", "Vila", "Tortosa", "Villamandos", "Morinigo", "Schneider"]
    horas = ["20:00:00", "03:00:00"] #genero horas aleatorias entre ese periodo
    fechas = ["01-03-2021", "21-03-2021"]
    pizzas = [["piedra","8",500, "1"],
            ["parrilla","8",500,"1"],
            ["molde","8",500, "1"],
            ["piedra","10",600,"1"],
             ["parrilla","10",600, "1"],
             ["molde","10",600,"1"],
             ["piedra","12",700, "1"],
             ["parrilla","12",700,"1"],
             ["molde","12",700,"1"]]

    cantidad_facturas = 1500
    
    while cantidad_facturas !=0:
        pizza = list()
        cliente = f"{nombres[random.randint(0,8)]} {apellidos[random.randint(0,5)]}"
        fecha = str(int(fechas[0][0:2])+random.randint(0,20))+"-03-2021"
        hora = horas_a_segundos(horas[0], str(random.randint(5,480)))
        for i in range(random.randint(1,3))  :  
            pizza.append(pizzas[random.randint(0,8)])
        total = 0
        for cada_pizza in pizza:
            total += cada_pizza[2]
        print(f"{fecha} {cliente} {pizza} {total} {hora}")
        pizzeria.cargofactura([fecha,
                                cliente,
                                pizza,
                                total,
                                hora])
        cantidad_facturas -= 1
        
    
    pizzeria.cargofactura(["22-03-2021", 
                            "Andrea Miron", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "21:43:00"])
    pizzeria.cargofactura(["22-03-2021", 
                            "Django Vila", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "20:30:00"])   
    pizzeria.cargofactura(["22-03-2021", 
                            "Dulcinea Vila", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "19:15:00"]) 
    pizzeria.cargofactura(["22-03-2021", 
                            "Juan Pablo Vila", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "18:50:00"])  
    pizzeria.cargofactura(["23-03-2021", 
                            "Carlos Vila", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "21:43:00"])   
    pizzeria.cargofactura(["23-03-2021", 
                            "Nicolas Tortosa", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "18:23:00"])   
    pizzeria.cargofactura(["24-03-2021", 
                            "Gonzalo Villamandos", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "23:05:00"])  
    pizzeria.cargofactura(["24-03-2021", 
                            "Andrea Morinigo", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "21:43:00"])  
    pizzeria.cargofactura(["24-03-2021", 
                            "Hugo Schneider", 
                            [["piedra","12",700, "1"],["parrilla","10",600,"1"]],
                            1300,
                            "22:05:00"])   
 
 


 
  

   

def busco_mayor(diccionario):
    clave_mayor = ""
    valor_mayor = 0
    for clave, valor in diccionario.items():
                
        if valor > valor_mayor:
            clave_mayor = clave
            valor_mayor = valor
    return [clave_mayor, valor_mayor]


if __name__=="__main__":
    
    pizzeria = Pizzeria()

    cargo_datos() #Cargo pedidos para pruebas
    cargo_facturas() #Cargo facturas para pruebas

    while True:
        
        os.system("cls")
        print("\t*********************************")
        print("\tBienvenido a Pizzeria Rica Pizza!")
        print("\t*********************************")
        print("\n\t1 - Nuevo Pedido \n\t2 - Genero Factura \n\t3 - Listo Pizzas mas pedidas \n\t4 - Recaudacion por hora \n\t5 - Pedidos por hora ")
        respuesta = input("\n\tSeleccione una opcion (Enter para Salir):")
        if respuesta == "":
            break
        
        elif respuesta == "1":
            while True:
                os.system("cls")
                cliente = input("\tIngrese Nombre del Cliente:\t")
                nuevo_pedido = Pedido(cliente)
                while True:
                    nuevo_menu = Menu()                   
                    pizza_seleccionada = nuevo_menu.seleccion_pizza()
                    cantidad_deseada = input("\tIngrese cantidad de pizza que quiere:\t")                 
                    respuesta = input("\n\tSigue seleccionando otras pizzas? s/n:\t")
                    pizza_seleccionada.append(cantidad_deseada)
                    
                    nuevo_pedido.cargo_pizza(pizza_seleccionada)
                    
                    if respuesta.lower() == "n":
                        demora = input("\tIngrese demora estimada:\t")
                        nuevo_pedido.cargo_demora(demora)
                        
                        break
                    
                pizzeria.tomo_pedido(nuevo_pedido)
                respuesta = input("\tCarga otro pedido? s/n:\t")
                if respuesta.lower()== "n":
                    break
        elif respuesta == "2":
            while True:
                os.system("cls")
                print("\tEstos son los pedidos que Ud. tiene cargados:")
                items = 1
                for cada_pedido in pizzeria.getPedidos():
                        print(f"\t{items} - Cliente: {cada_pedido.muestro_pedido()[0]}")
                        items +=1
                        for descripcion in cada_pedido.muestro_pedido()[1]:
                            print(f"\t\t--{descripcion[0]}--{descripcion[1]} porciones {descripcion[3]} ${descripcion[2]} ${int(descripcion[3])*descripcion[2]}")
                            
                respuesta = input("\tSeleccione nro de pedido a facturar:\t")
                if respuesta in [str(x) for x in range(len(pizzeria.getPedidos())+1)]:
                    pedido_a_facturar = pizzeria.getPedidos()[int(respuesta)-1]
                    nueva_factura = Factura(pedido_a_facturar)
                    factura = nueva_factura.genero_factura()
                    input()
                    pizzeria.cargofactura(factura)
                    pizzeria.elimino_pedido(pedido_a_facturar)
                break
        elif respuesta == "3":
            pizzeria.pizzas_mas_pedidas()
            input()

        elif respuesta == "4":
            pizzeria.ingresos_por_tiempo()
            input()



             