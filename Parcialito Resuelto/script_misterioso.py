from logging import exception

muestras_1 = [1, 2, 3]
muestras_2 = []

def obtener_media(lista):
    sumatoria = 0
    for valor in lista:
        sumatoria += valor
    longitud = len(lista)
    try:
        print(sumatoria / longitud) 
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("La lista solo acepta enteros")


obtener_media(muestras_2)
obtener_media(muestras_1)




#**Consigna N°3** (Manejo de exepciones)
#Ejecutá el script_misterioso.py y realizá resolvé:
#    1. ¿Qué tipo de exepción arroja la corrida del script? **El error que arroja es: ZeroDivisionError**
#    2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error ###Se usa try except###
#    3. ¿Qué otras excepciones deberias considerar? ###TypeError###

    
