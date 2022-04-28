from ast import Num
from re import M
from tkinter import N


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

#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual.
#También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
#Este objeto debe entender los siguientes mensajes:

class Contador_2():
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