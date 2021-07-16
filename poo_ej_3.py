'''Desarrollar un programa que cargue los datos de un triángulo.

Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del 
lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).'''


import os

class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = int(lado1)
        self.lado2 = int(lado2)
        self.lado3 = int(lado3)

    def es_triangulo(self):
        if (self.lado1 + self.lado2) > self.lado3 and (self.lado1 + self.lado3) > \
        self.lado2 and (self.lado2 + self.lado3) > self.lado1:
            return True
        else:
            return False

    def que_soy(self):
        if self.lado1 == self.lado2 == self.lado3:
            return  "Equilatero"
        elif self.lado1 != self.lado2 != self.lado3 and self.lado1 != self.lado3:
            return "Escaleno" 
        else:
            return "Isosceles"
    
    def mayor_lado(self):
        if self.que_soy() != "Equilatero":
            return str(max([self.lado1, self.lado2, self.lado3]))
        else:
            return "\tTodos los lados son iguales"

    

    
if __name__ == "__main__":
    os.system("cls")
    mensaje = ""
    lados = dict()
    print("\t*****************************************")
    print("\tVamos a cargar 3 lados de un Triangulo\n")
    print("\t*****************************************")
    while True:
        
        
        print(mensaje)
        lista_lados = input("\n\tIngrese los tres lados separados por comas:").split(",")
        if len(lista_lados) == 3:
            lado1, lado2, lado3 = lista_lados
        else:
            mensaje = '''\tERROR! Se ingresaron valores incorrectos!
            ingrese nuevamente!'''
            continue

        if lado1 and lado2 and lado3:

            lado1, lado2, lado3 = [lado.strip() for lado in [lado1,lado2,lado3]]
            
            if (lado1 + lado2 + lado3).isdigit():
                lados[lado1] = "lado1"
                lados[lado2] = "lado2"
                lados[lado3] = "lado3"
                un_triangulo = Triangulo(lado1, lado2, lado3)
                if un_triangulo.es_triangulo():
                    if un_triangulo.que_soy()  != "Equilatero":
                        print(f"\tEl lado mas grande es: {lados[un_triangulo.mayor_lado()]}\n")
                    else:
                        print(un_triangulo.mayor_lado())
                    print(f"\tSoy {type(un_triangulo).__name__} {un_triangulo.que_soy()}")
                else:
                    mensaje = '''\tERROR! los valores ingresados no corresponden a un triangulo
                        La suma de dos lados debe ser mayor al tercer lado!, 
                        Vuelva a cargar!'''
                    continue
            else:
                mensaje = '''\tERROR Debe ingresar solo numeros!
                        Vuelva a cargar!'''
                continue
        else:
            mensaje ='''\tERROR! Debe ingresar los tres valores separados por comas!
                    Vuelva a cargar! Ej: valor1, valor2, valor3'''
            continue
        opcion = input("\tContinua Cargando? (Enter  = s o N = Sale)")
        if opcion.lower() == "n":
            break
    print("\n\t*********************")
    print("\tGracias! Hasta Pronto")
    print("\t*********************")



