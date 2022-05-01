import re
#N1
print()
print("Ejercicio N1")
def funcion_1(string):
    print(len(re.findall("bc9", string)))

funcion_1("xsabc9cabcb3sabc9")
funcion_1("hola amigos mios")

def funcion_1_2(string):
    aa_gg = re.findall(r'aa([^c].*?)gg', string)
    print(aa_gg)
funcion_1_2("ttaatatggttaacatgg")

#N2
print()
print("Ejercicio N2")
#Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor.
# El prototipo de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 rpm.
#La velocidad del auto se calcula así: _**(rpm / 100) * (0.5 + (cambio / 2))**_. Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
#También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes: 

#* Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
#* Si el motor está en primera, entonces se multiplica por 3.
#* Si el motor está en segunda, entonces se multiplica por 2.

#Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
#El modelo debe entender estos mensajes:

#arrancar() , se pone en primera con 500 rpm.
#subirCambio()
#bajarCambio()
#subirRPM(cuantos)
#bajarRPM(cuantos)
#velocidad()
#consumoActualPorKm(), calcula el consumo actual y lo devuelve

class Auto():
    def __init__(self):
        self.cambio = 0
        self.rpm = 0
        self.consumo = 0.05
    
    def arrancar(self):
        self.cambio = 1
        self.rpm = 500
    
    def subirCambio(self):
        self.cambio += 1

    def bajarCambio(self):
        self.cambio -= 1
    
    def subirRPM(self, rpm):
        self.rpm += rpm

    def bajarRPM(self, rpm):
        self.rpm -= rpm

    def velocidad(self):
        velocidad = (self.rpm / 100) * (0.5 + (self.cambio / 2))
        print("La velocidad es:", velocidad)

    def consumoActualPorKm(self):
        if self.rpm >= 3000:
            consumo_por_rpm = self.consumo * ((self.rpm - 2500) / 500)
            if self.cambio == 1:
                print("El consumo es: ", consumo_por_rpm * 3)
            elif self.cambio == 2:
                print("El consumo es: ", consumo_por_rpm * 2)
            else:
                print("El consumo es: ", consumo_por_rpm)
        else:
            if self.cambio == 1:
                print("El consumo es: ", self.consumo * 3)
            elif self.cambio == 2:
                print("El consumo es: ", self.consumo * 2)
            else:
                print("El consumo es: ", self.consumo)

auto1 = Auto()
auto1.arrancar()
auto1.subirRPM(3500)
auto1.subirCambio()
auto1.subirCambio()
auto1.subirCambio()
auto1.bajarCambio()
print("Cambio del auto: ", auto1.cambio)
print("RPM del auto: ", auto1.rpm)
auto1.velocidad()
auto1.consumoActualPorKm()

print("---------------------------*Cambian los valores del auto*--------------------------")

auto1.bajarRPM(3000)
print("Cambio del auto: ", auto1.cambio)
print("RPM del auto: ", auto1.rpm)
auto1.velocidad()
auto1.consumoActualPorKm()





    
        
