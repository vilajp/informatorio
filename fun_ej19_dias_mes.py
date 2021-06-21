'''Ejercicio 18: Días en un mes

Escriba una función que determine mostrar cuántos días hay en un mes en particular. Su función tomará dos
parámetros: el mes como un número entero entre 1 y 12, y el año como un número entero de cuatro dígitos.
Asegúrese de que su función informa el número correcto de días en febrero para los años bisiestos. 
Incluya un programa principal que lea un mes y un año del usuario y muestre el número de días en ese mes.'''

from funciones import muestro_mensaje, limpiar_pantalla

def es_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0


def contar_dias(mes,anio):
    meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if es_bisiesto(anio) and mes==2:
        return meses[mes]+1
    else:
        return meses[mes]


if __name__ == "__main__":
    sigo = True
    muestro_continua = True
    while sigo:
        limpiar_pantalla()
        mes = input("\tIngrese mes en numero entre 1 y 12(Presione Enter para salir):")
        if mes == "":
            break
        if mes not in "01234567891011":
            muestro_mensaje("Por favor ingrese un numero!", muestro_continua)
            continue
        elif int(mes) not in range(1,13):
            muestro_mensaje("Por favor ingrese un numero en el rango solicitado!!", muestro_continua)
            continue
        sigo2 = True
        while sigo2:    
            anio = input("\tIngrese anio en 4 digitos: ")
            if len(anio) != 4:
                muestro_mensaje("Tiene que ingresar el año en cuatro digitos!")
                continue
            for nro in anio:    
                if nro in "0123456789":
                    sigo2 = False
                else:
                    muestro_mensaje("Por favor ingrese un numero!", muestro_continua)
                    sigo2 = True
                    break
                    
        muestro_mensaje(f"El numero de dias del mes {mes} de {anio} fue {str(contar_dias(int(mes),int(anio)))}", muestro_continua)
    limpiar_pantalla()
    muestro_mensaje("Gracias por Venir!")        
        