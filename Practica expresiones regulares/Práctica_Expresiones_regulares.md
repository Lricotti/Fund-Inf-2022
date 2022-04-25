# **Expresiones Regulares**
from itertools import count
from mimetypes import common_types
from pydoc import cram
import re
import string
from xml.sax import SAXNotSupportedException 

#*https://docs.python.org/es/3/howto/regex.html#regex-howto*#

##### **Ejercicio 1**
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
#Estos caracteres son a-z, A-Z y 0-9.

def Caracter_Permitido(string):
    print(bool(re.findall(r'\w', string)))

Caracter_Permitido("Hola")

print()

##### **Ejercicio 2**

#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos.
# Estos caracteres son a-z, A-Z y 0-9.

def Caracter_Permitido(string):
    print(not bool(re.findall(r'\W', string)))

Caracter_Permitido("Hola!")

print()

##### **Ejercicio 3**
#Creá un programa que verifique las siguientes condiciones:
    
#* si un string dado tiene una _h_ seguida de ninguna o más _e_.
def tiene_h(string):
    print(bool(re.findall("he*", string)))

tiene_h("hola helicotpero heeeermoso sofia")
#* si un string dado tiene una _h_ seguida de una o más _e_.
def tiene_h(string):
    print(bool(re.findall("he+", string)))

tiene_h("heola")
#* si un string dado tiene una _h_ seguida de dos o tres _e_. #Imposible#
def tiene_h(string):
    print(bool(re.search("he{2,3}", string) and not re.search("heeee+", string)))

tiene_h("hee")

print('-----------------------------------')
##### **Ejercicio 4**
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado
#(el string no debe contener espacios).

def unidas_por_guion(string):
    print(re.findall(r'([A-Z]+[a-z]+)_([A-Z]+[a-z]+)', string))

unidas_por_guion("hola_chau")

print()
##### **Ejercicio 5**
#Escribí un programa que diga si un string empieza con un número específico.
def empieza_con(string, n):
    numero = "^" + n 
    print(bool(re.search(numero, string))) 

empieza_con("7hla", "7")

print()
##### **Ejercicio 6**
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.


LISTA = ["lucho", "123", "joaco", "Noemí", "s"]
FRASE = "Después le dijo su suegra Noemí: Hija mía, ¿no he de buscar hogar para ti, para que te vaya bien?"
def strings_en_frase(lista, frase):
    for element in lista:
        print (element)
        print (re.search(element, frase))
        print("--------------")
        

strings_en_frase(LISTA, FRASE)
    

##### **Ejercicio 7**
#Realizá un programa que encuentre un string que contenga solamente
#letras minúsculas, mayúsculas, espacios y números.

def MmEN(string):
    string_sin_espacios = string.replace(" ","")
    a = bool(re.search(r'[a-z]', string) and re.search(r'[A-Z]', string) and re.search(r"\s", string) and string_sin_espacios.isalnum())
    print(a)
MmEN("Aa1 ")

##### **Ejercicio 8**
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
def CN(string):
    a = (re.findall(r'\d', string))
    print(a)
CN("hola 3hola si 8union")

print()
##### **Ejercicio 9**
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: _"Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"_)

def encontrar_guion(cadena):
    a = re.findall('-.*-', cadena)
    print(a)
encontrar_guion("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

#Lo hicimos pero solo funciona con esa cadena, si la cambiamos falla!!!!!!!

##### **Ejercicio 10**
#Obtené las substrings y las posiciones de estas en una string dada, considerando que las substrings están delimitadas por los caracteres _@_ o _&_.

def obtene_substring(string):
    a = re.split(r"@|&", string)
    print (a)
    
obtene_substring("lucho&ricotti@gmail.com")
print()

##### **Ejercicio 11**
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima.
#(Lista de ejemplo: _["Práctica Python", "Práctica C++", "Práctica Fortran"]_).

lista_string = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def dos_con_p(variable):

    for lenguaje in lista_string:
        resultado = re.match("(P\w+)\W(P\w+)", lenguaje)

        if resultado:
            print(resultado.groups())

dos_con_p(lista_string)
print()
##### **Ejercicio 12**
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (**|**).

def reemplazar(string):
    ya_reemplazado = string.replace(" ", "|").replace(":", "|").replace("_", "|")
    print(ya_reemplazado)

reemplazar("Hola como:estas_lucho")
print()
##### **Ejercicio 13**
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def reemplazar2(string):
    a = (re.findall(r'\W', string))
    if a[0] == a[1]:
        ya_reemplazado_2 = string.replace(a[0], "_", 2)
        print(ya_reemplazado_2)
    else:
         ya_reemplazado_3 = string.replace(a[0], "_", 1).replace(a[1], "_", 1)
         print(ya_reemplazado_3)

reemplazar2("Hola:Chau?Lucho!")

#Otra forma con sub
def reemplazar(string):
    return re.sub("\W","_", string,2)

print(reemplazar("hola*comoestas??as"))
print(reemplazar("hola como esta??ass"))
print()
##### **Ejercicio 14**
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
def reemplazar3(string):
    a = re.sub(r'\s',";",string)
    print(a)
reemplazar3("Hola como   ")
##### **Ejercicio 15**
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.
def validar_mail_correcto(mail):
     valido = bool(re.match(r'(\S+)@(\w+)\.(\w+)', mail))
     print(valido)

validar_mail_correcto("hola@gmail.com")