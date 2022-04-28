

from operator import eq
from sqlite3 import enable_callback_tracebacks


class AnimalesAlados():
  def esta_feliz(self):
    return self.energia > 500

class Golondrina(AnimalesAlados):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
  
  def comer_peces(self, unidades):
    self.energia += 100 * unidades
#Debil
  def esta_debil(self):
    return self.energia < 10
#Feliz se pone arriba como una clase de clases,
# porque integra a ambas clases.
  


class Dragon(AnimalesAlados):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10
# Debil
  def esta_debil(self):
    return self.energia < 50
#Feliz se pone arriba como una clase de clases,
# porque integra a ambas clases.
  

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
# Crea a maria y chimuelo
chimuelo = Dragon(200, 1000)
maria = Golondrina(42)

#Desafio 2, clase no voladores
#Desde el punto de vista del entrenador no son polimorficas, 
#por lo tanto hay q definir una funcion que permita al entrenador entrenar a las aves no voladoras haciendolas correr_en_circulos.
#y modifcar el entrenamioento intensivo para incluir a esta nueva clase.

class AvesNoVoladoras():
  def __init__(self, energia):
    self.energia = energia
  
  def correr_en_circulos(self):
    self.energia -= 25
  
  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos



class Entrenador(): 
  "Un entrenador tiene un equipo y opuede admitir nuevos animales"
  def __init__(self, equipo):
    self.equipo = equipo

  def el_equipo(self):
    print(self.equipo)

  def agregar_animal(self, animal):
    self.equipo.append(animal)

  def entrenar_dragon(self, dragon):
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)
 
  def entrenar_golondrina(self, golondrina):
    for i in range(20):
      golondrina.volar_en_circulos()
    golondrina.comer_peces(3)

  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon
    for golondrina in self.equipo:
      self.entrenar_golondrina

  def entrenamiento_intensivo(self):
    for golondrina in self.equipo:
      contador1 = 0
      while not golondrina.esta_debil():
        golondrina.volar_en_circulos()
        contador1 += 1

    for dragon in self.equipo:
      while not dragon.esta_debil():
        dragon.volar_en_circulos()
    print ("Pepita dio ", contador1, " vueltas antes de cansarse") 
        

hipo = Entrenador([])