##### **Ejercicio 1**
#Dadas las siguientes clases responder:
#* cuales son sus estados
#* cuales son sus interfaces
#* ¿Comparten interfaz? --> si 
#* ¿Son polimórficas? --> Si comparten init
class Perro:
    def __init__(self): #Interfaces
        self.alimento = 0 #Estado
        self.caricias = 0#Estado

    def energia(self): #Interfaces
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):#Interfaces
        self.alimento += gramos

    def alimento(self):#Interfaces
        print(self.alimento)
    
    def acariciar(self):#Interfaces
        self.caricias += 1

    def estaDebil(self):#Interfaces
        return self._caricias < 2

    def pasear(self, km):#Interfaces
	    self.alimento -= km / 4

class Gato:
    def __init__(self): #Interfaces
        self.alimento = 0 #Estado
        self.caricias = 0 #Estado

    def energia(self):#Interfaces
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):#Interfaces
        self.alimento += gramos * 1.5

    def caricias(self):#Interfaces
        print(self.caricias)

    def acariciar(self):#Interfaces
        self.caricias += 1

    def estaDebil(self):#Interfaces
        return self._caricias < 4

##### **Ejercicio 2**
#Modificar la clase **Golondrina** vista en la teoría para poder preguntar si una golondrina está en equilibrio.
#Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

class Golondrina():
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

  def esta_debil(self):
    return self.energia < 10

  def esta_en_equilibrio(self):
      print (150 <= self.energia <= 300)

pepita = Golondrina(160)
pepita.esta_en_equilibrio()
print("---------------------------------------------------")

##### **Ejercicio 3** 
#Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. 
# Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. 

#Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en:
# hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos.

#Se propone:
#* implementar la clase Ornitologo, de forma tal que acepte las operaciones:
# estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio().
# Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio.
# Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio,que responden True cuando se les consulta estaEnEquilibrio().

#* comprobar el código que se escribió con esta secuencia:
	#* definir un ornitólogo, dos golondrinas y dos gorriones,
	#* inicializar las aves con valores conocidos,
	#* decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
	#* decirle al ornitólogo que realice su rutina sobre aves,
	#* verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.


class Ornitologo():
    def __init__(self):
        self.aves = []
    def estudiarAve(self, ave):
        self.aves.append(ave)
    def avesEnEstudio(self):
        print(self.aves)
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.come(80)
            ave.vuela(70)
            ave.come(10)
    def avesEnEquilibrio(self):
        print (self.aves[i].esta_en_equilibrio() for i in range(len(self.aves)))

class Golondrina():
    def __init__(self, energia):
        self.energia = energia
    def come(self, gramos):
        self.energia += 4 * gramos
    def volar_en_circulos(self):
        self.vuela(0)
    def vuela(self, kms):
        self.energia -= 10 + kms
    def comer_peces(self, unidades):
        self.energia += 100 * unidades
    def esta_debil(self):
        return self.energia < 10
    def esta_en_equilibrio(self):
        return 150 <= self.energia <= 300

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
        return 0.5 <= css <= 2
        
    
    def CSSP(self):
        cssp = self.km_mayor / self.comida_mayor
        print("CSSP: ", cssp)
    
    def CSSV(self):
        if self.comida_total != 0:
            cssv = self.km_total / self.comida_total
            print("CSSV: ", cssv)
        else:
            print("CSSV: None")

    def esta_en_equilibrio(self):
        return 0.5 <= self.CSS() <=2  

lucho = Ornitologo()
golondrina_1 = Golondrina(10)
golondrina_2 = Golondrina(10)
gorrion_1 = Gorriones()
gorrion_2 = Gorriones()

print("Antes de la rutina")
print(golondrina_1.energia)
print(golondrina_2.energia)
gorrion_1.CSSV()
gorrion_2.CSSV()

lucho.estudiarAve(golondrina_1)
lucho.estudiarAve(gorrion_1)
lucho.estudiarAve(gorrion_2)
lucho.realizarRutinaSobreAves()
lucho.avesEnEquilibrio()

print("Despues de la rutina")
print(golondrina_1.energia)
print(golondrina_2.energia)
gorrion_1.CSSV()
gorrion_2.CSSV()
lucho.avesEnEquilibrio()