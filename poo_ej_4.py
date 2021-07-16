'''Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.

Añadir contacto

Lista de contactos

Buscar contacto

Editar contacto

Cerrar agenda'''

import os

class Agenda:

    def __init__(self):
        self.contactos = list()
    
    def nuevo_contacto(self, contacto):
        self.contactos.append(contacto)
        return "Contacto guardado exitosamente!"
    
    def listar_contactos(self):
        for cada_contacto in self.contactos:
            print(f"\tNombre: {cada_contacto.nombre}")
            print(f"\tTelefono: {cada_contacto.telefono}")
            print(f"\temail: {cada_contacto.email}")
        input()

    def buscar_contacto(self, cadena):
            for cada_contacto in self.contactos:
                if cadena in cada_contacto.nombre or cadena in cada_contacto.telefono or \
                cadena in cada_contacto.email:
                    print(f"\tNombre: {cada_contacto.nombre}")
                    print(f"\tTelefono: {cada_contacto.telefono}")
                    print(f"\temail: {cada_contacto.email}")
            input()
    
    def editar_contacto(self, cadena):
        contactos_modificar = list()
        for cada_contacto in self.contactos:
            if cadena in cada_contacto.nombre or cadena in cada_contacto.telefono or \
                cadena in cada_contacto.email:
                contactos_modificar.append(cada_contacto)
        return contactos_modificar
                    

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


    def setNombre(self, nombre):
        if nombre != "":   
            self.nombre = nombre
    
    def setTelefono(self, telefono):
        if telefono != "":   
            self.telefono = telefono

    def setEmail(self, email):
        if email != "":   
            self.email = email
    
if __name__ == "__main__":
    mensaje = ""
    agenda = Agenda()
    andrea = Contacto("Andrea Miron", "3624241674", "andreamiron_1@hotmail.com")
    agenda.nuevo_contacto(andrea)
    dulcinea =  Contacto("Dulcinea Vila", "3624697086", "viladulcinea1@gmail.com")
    agenda.nuevo_contacto(dulcinea)
    juan = Contacto("Juan Pablo Vila", "3624201972", "vilajp@gmail.com")
    agenda.nuevo_contacto(juan)

    while True:
        os.system("cls")
        print("\n\t1 - Añadir Contacto \n\t2 - Lista de Contactos \n\t3 - Buscar Contacto \n\t4 - Editar Contacto \n\t5 - Cerrar Agenda")
        opcion = input("\tSeleccione una opcion(Enter para salir):")
        if opcion == "":
            break
        elif opcion == "1":
            nombre = input("\tIngrese Nombre del Contacto:\t")
            telefono = input("\tIngrese telefono del Contacto:\t")
            email = input("\tIngrese email del Contacto:\t")
            un_contacto = Contacto(nombre, telefono, email)
            print(agenda.nuevo_contacto(un_contacto))
            input()
        elif opcion == "2":
            agenda.listar_contactos()
        elif opcion == "3":
            cadena = input("\tIngrese un dato a buscar:")
            agenda.buscar_contacto(cadena)
        elif opcion == "4":
            cadena = input("\tIngrese un dato a buscar:")
            lista_modificar  = agenda.editar_contacto(cadena)
            print(f"\tEstos {len(lista_modificar)} contactos coinciden con su busqueda:")
            for i in range(len(lista_modificar)):
                print(f"{i + 1} - {lista_modificar[i].nombre} ")
            opcion = input("\tIngrese su opcion:")
            print(f"\tUsted va a editar {lista_modificar[int(opcion)-1].nombre}")

            print(f"\tNombre :{lista_modificar[int(opcion)-1].nombre}")
            nombre = input("Ingrese nuevo nombre: \t(Vacio deja el mismo)")
            lista_modificar[int(opcion)-1].setNombre(nombre)

            print(f"\tTelefono :{lista_modificar[int(opcion)-1].telefono}")
            telefono = input("Ingrese nuevo telefono: \t(Vacio deja el mismo)")
            lista_modificar[int(opcion)-1].setTelefono(telefono)

            print(f"\temail :{lista_modificar[int(opcion)-1].email}")
            email = input("Ingrese nuevo email: \t(Vacio deja el mismo)")
            lista_modificar[int(opcion)-1].setEmail(email)

            





