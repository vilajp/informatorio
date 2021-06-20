from random import randint
'''Escriba una función que genere una contraseña aleatoria. La contraseña debe tener una longitud aleatoria de entre 7 
y 10 caracteres. Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII. Su función no 
tomará ningún parámetro y devolverá la contraseña generada aleatoriamente como su único resultado. Desarrolle un programa 
principal y muestre la contraseña generada aleatoriamente.

Sugerencia: Probablemente encuentre útil la función chr cuando complete este ejercicio.'''

def crear_password(password=""):
    rango = randint(7,10)
    for cada_letra in range(rango):
        caracter = randint(33,126)
        password += chr(caracter)
    return password


print(crear_password())




