from ast import Num
from re import M
from tkinter import N

#### **Ejercicio 2**
#Modificá el método **volar** de la clase `Golondrina` visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía 
#toma el valor 0 o valor negativo.

class Golondrina():
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
      if self.energia > 0:
          self.energia -= 10 + kms
      else:
          print("No tiene energia para volar")
#Debil
  def esta_debil(self):
    return self.energia < 10

pepita = Golondrina(-10)

print(pepita.energia)
pepita.volar(10)
print(pepita.energia)
print("--------------------------------------------")

#### **Ejercicio 3**
#Creá una clase `Notebook` cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio,
#el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento.
#Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.
class Notebook():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, entero):
        entero_con_cero = entero / 100
        self.precio -= self.precio * entero_con_cero
        print("EL precio de la notebook es: ", self.precio)

MacBookAir = Notebook("Apple", "Air", 1000)

MacBookAir.descuento(10)

#### **Ejercicio 4**
#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual.
# También puede resetear este valor y al hacerlo se pone en cero.
# Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
#* inc()
#* dis()
#* reset()
#* valorActual()
#* valorNuevo(nuevoValor)

#Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.
#```python
#contador = Contador(10)
#contador.inc()
#contador.inc()
#contador.dis()
#contador.inc()
#contador.valorActual()
#contador.valorNuevo(27)
#contador.dis()
#contador.dis()
#contador.valorActual()

class Contador():
    def __init__(self, Numero_inicial):
        self.Numero_inicial = Numero_inicial

    def inc(self):
        self.Numero_inicial += 1

    def dis(self):
        self.Numero_inicial -= 1
    
    def reset(self):
        self.Numero_inicial = 0
    
    def valorActual(self):
        print (self.Numero_inicial)
    
    def valorNuevo(self, valor):
        self.Numero_inicial = valor

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
print("------------------------------------------")

##### **Ejercicio 5**
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje.
# Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo).
# El método para saber el último comando es `ultimoComando`, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador_2():
    def __init__(self, Numero_inicial):
        self.Numero_inicial = Numero_inicial
        self.ultimo_comando = []

    def inc(self):
        self.Numero_inicial += 1
        self.ultimo_comando.append("incremento")

    def dis(self):
        self.Numero_inicial -= 1
        self.ultimo_comando.append("disminución")
    
    def reset(self):
        self.Numero_inicial = 0
        self.ultimo_comando.append("reset")
    
    def valorActual(self):
        print (self.Numero_inicial)
    
    def valorNuevo(self, valor):
        self.Numero_inicial = valor
        self.ultimo_comando.append("actualización")
    
    def ultimoComando(self):
        print("El ultimo comando fue: ", self.ultimo_comando[-1])


contador2 = Contador_2(10)
contador2.valorActual()
contador2.inc()
contador2.inc()
contador2.valorActual()
contador2.ultimoComando()
contador2.valorNuevo(15)
contador2.valorActual()
contador2.ultimoComando()
print("------------------------------------------")

##### **Ejercicio 6**
#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:
#* cargar(numero)
#* sumar(numero)
#* restar(numero)
#* multiplicar(numero)
#* valorActual()

#Si se evalúa la siguiente secuencia:
#calculadora = Calculadora()
#calculadora.cargar(0)
#calculadora.sumar(4)
#calculadora.multiplicar(5)
#calculadora.restar(8)
#calculadora.multiplicar(2)
#calculadora.valorActual()
#el resultado debe ser 24.

class Calculadora:
    def __init__(self):
        self.numero = 0
    
    def cargar(self, numero):
        self.numero = numero
    
    def sumar(self, numero):
        self.numero += numero
    
    def restar(self, numero):
        self.numero -= numero
    
    def multiplicar(self, numero):
        self.numero *= numero
    
    def valorActual(self):
        print(self.numero)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
print("---------------------------------------")


##### **Ejercicio 7**
##Definí una clase de gorriones, de los cuales nos interesa conocer tres medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”).
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. 
#El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió.
#El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser `None`.
#Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorriones():
    def __init__(self):
        self.km_mayor = 0
        self.km_total = 0
        self.comida_mayor = 0
        self.comida_total = 0
    def vuela(self, km):
        self.km_total += km
        if km > self.km_mayor:
            self.km_mayor = km
    
    def come(self, gramos):
        self.comida_total += gramos
        if gramos > self.comida_mayor:
            self.comida_mayor = gramos 

    def CSS(self):
        css = self.km_total / self.comida_total
        print("CSS: ", css)
        if 0.5 <= css <= 2:
            print("Esta en equilibrio")
        else:
            print("No esta en equilibrio")
    
    def CSSP(self):
        cssp = self.km_mayor / self.comida_mayor
        print("CSSP: ", cssp)
    
    def CSSV(self):
        if self.comida_total != 0:
            cssv = self.km_total / self.comida_total
            print("CSSV: ", cssv)
        else:
            print("CSSV: None")


lucho = Gorriones()
lucho.vuela(10)
lucho.CSSV()
print()
lucho.come(100)
lucho.vuela(50)
lucho.CSS()
print()
lucho.come(1000)
lucho.vuela(1000)
lucho.CSSP()
print()
lucho.CSSV()
lucho.CSS()

