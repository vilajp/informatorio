'''Ejercicio 6: Centrar una cadena en la terminal

Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la 
terminal en caracteres como segundo parámetro. Su función debe devolver una nueva cadena que 
consta de la cadena original y el número correcto de espacios iniciales para que la cadena 
original aparezca centrada dentro del ancho proporcionado cuando se imprima. No agregue ningún 
carácter al final de la cadena. Incluya un programa principal que use su función.'''

def centrar(string, ancho):
    if ancho > len(string):
        diferencia = (ancho - len(string))//2
        nuevo_string = (" "*diferencia)+string
    else:
        print("El ancho de la pantalla debe ser mayor que el largo de su cadena")
    return nuevo_string


string = input("Ingrese una cadena de caracteres para centrar: \n\t")
ancho = int(input("Ingrese ancho de la terminal en caracteres: \n\t"))

print("*" * ancho)
print(centrar(string, ancho))