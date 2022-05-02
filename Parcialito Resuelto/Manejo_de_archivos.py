#Ejercicio 4
#Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada _Resultado_

# por otro, que lea todos los archivos con extensión `.txt` y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*,
#  que tiene que estar dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**

import os, glob

#Esta es la forma correcta

def unit_txt():
    os.mkdir("Resultado")
    lista_txt = glob.glob("*.txt")
    with open("Resultado/texto_completo.txt", "a") as a:
        for txt in lista_txt:
            with open(txt, "r") as archivo:
                a.write(archivo.read())

#glob (short for global) is used to return all file paths that match a specific pattern.
#We can use glob to search for a specific file pattern, or perhaps more usefully,
#search for files where the filename matches a certain pattern by using wildcard characters.