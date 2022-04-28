from aves import pepita, anastasia, roberta, hipo

#pepita.cantar_boleros() --> No funciona porque no esra definido
#pepita.comer_alpiste() --> falta la variable gramos

print(pepita.energia)

pepita.volar_en_circulos() #Consume 10 de energia
print(pepita.energia)

pepita.comer_alpiste(10) #Le otorga 40 de energia
print(pepita.energia)

print("-----------------Aparaece anastacia------------")

print(anastasia.energia) #tiene el doble de energia q pepita

anastasia.volar_en_circulos()
print(anastasia.energia)

anastasia.comer_alpiste(10)
print(anastasia.energia)

print("-----------------Aparaece roberta------------")

print(roberta.energia) #Tiene 10 veces mas energia que pepita

roberta.volar_en_circulos() # Gasta solo 1 de energia
print(roberta.energia)

#roberta.comer_alpiste(10) # No funciona, no esta definido

roberta.comer_peces(1) #Aumenta 100 la energia
print(roberta.energia) 

roberta.escupir_fuego() #Gasta 20 de energia
print(roberta.energia)

####pepita = Golondrina(100)#### ASI ES COMO SE CREAN
####anastasia = Golondrina(200)#### "Golondrina es la clase y (200) la energia variable"

print("-----------------Aparaece hipo------------")
print(roberta.energia)
hipo.agregar_animal(roberta)
hipo.agregar_animal(pepita)
hipo.el_equipo()

print("Antes de volar roberta ", roberta.energia)
print("Antes de volar pepita ", pepita.energia)

hipo.entrenamiento_intensivo()
print("Despues de volar roberta ", roberta.energia)
print("Despues de volar pepita ", pepita.energia)


