# **Manipulación de archivos**

from os import pread
from urllib.parse import _ParseResultBase


path = "/Users/lucho/Desktop/Informatica/Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt"


##### **Ejercicio 1**
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo **no** empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").


def lineadearchivo(archivo, letra):
    with open(archivo, "r") as s:
        contador = 0
        for linea in s:
            if linea[0] != letra:
                contador += 1        
    print(contador) 

lineadearchivo(path, "s")

##### **Ejercicio 2**
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

def leaeimprima(archivo, n):
    with open(archivo, "r") as s:
        for i in range(n):
            print(s.readline())

leaeimprima(path, 2)

##### **Ejercicio 3**
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def guardeeimpirma(archivo, n_ulitmas):
    with open(archivo) as s:
            lineas = [lineas.strip('\n') for lineas in s.readlines()]
            print(lineas[-n_ulitmas])

guardeeimpirma(path, 1)

##### **Ejercicio 4**
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def cuentepalabras(archivo):
    with open(archivo) as s:
        palabras = s.read()
        cantidad_palabras = palabras.split()
    print(len(cantidad_palabras))

cuentepalabras(path)

##### **Ejercicio 5**
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplaceletra(archivo, letra):
    import re
    with open(archivo, "r") as s:
        linea = s.read()
        linea_2 = linea.replace(letra, (letra + "\n"))
        with open("/Users/lucho/Desktop/Informatica/Fundamentos_de_informatica-master/Python_intro/archivo_nuevo", "w") as s2:
            s2.write(linea_2)

reemplaceletra(path, "s")

##### **Ejercicio 6**
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def sinsalto(archivo):
    with open(archivo, "r") as s:
        linea = s.read()
        lineas = linea.replace("\n", "")
        with open("/Users/lucho/Desktop/Informatica/Fundamentos_de_informatica-master/Python_intro/archivo_nuevo2", "w") as f2:
            f2.write(lineas) 
            
##### **Ejercicio 7**
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_mas_larga(archivo):
    palabra = ""
    max_long = 0
    with open(archivo, "r") as f:
        lista_palabra = f.read().split()
        for word in lista_palabra:
            if len(word) > max_long:
                max_long = len(word)
                palabra = word
    print("la palabra mas larga es", palabra, "con", max_long, "caracteres")

palabra_mas_larga(path)

##### **Ejercicio 8**
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def join_files(file1, file2, file3):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "r") as f3:
        f3.write(f1.read() + f2.read())
join_files("Documento", "Documento2", "Documento3")#Hay q crear esos documentos y poner el path

##### **Ejercicio 9**
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo.
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuenciapalabras(archivo):
    with open(archivo, "r") as f:
        contenido = f.read().lower()
        palabras = contenido.split()
        numero_palabras = len(palabras)

        print(numero_palabras)

        diccionario_frecuencias = {}
        for palabra in palabras:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1 
            else:
                diccionario_frecuencias[palabra] = 1

        for palabra in diccionario_frecuencias:
            frecuencia = diccionario_frecuencias[palabra]
            frecuencia2 = frecuencia / numero_palabras
            print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia2}")

frecuenciapalabras(path)

##### **Ejercicio 10**
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

def  agregararchivos(path_carpeta):
    import os
    lista = os.listdir(path_carpeta)
    for i in lista:
        if i.endswith(".txt"):
            with open("documento", "a") as f:
                with open(i, "r") as f2:
                    f.write(f2)

agregararchivos("/Users/lucho/Desktop/A")

##No logro hacerlo funcionar