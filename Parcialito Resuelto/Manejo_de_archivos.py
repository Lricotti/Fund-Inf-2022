#Ejercicio 4
#Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada _Resultado_

# por otro, que lea todos los archivos con extensión `.txt` y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*,
#  que tiene que estar dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**
import os
from posixpath import abspath, relpath
import shutil

os.mkdir("Resultado") #Hay q estar parado en donde se quiere crear la carpeta, utilizando cd en la terminal y poniendo el path en donde se quiere crear#
path = os.getcwd() 
lista = os.listdir(path) #Dice que archivos hay en donde estes parado, en forma de lista
for i in lista:
    if i.endswith(".txt"):
        with open("texto_completo.txt", "a") as f:
            with open(i, "r") as g:
                f.write(g.read())

shutil.move("texto_completo.txt", "Resultado/texto_completo.txt") #Mueve el archivo texto_completo dentro de la carepta Resultado

