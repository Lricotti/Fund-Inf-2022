# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 0
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
try:
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
except:
    print("Fallo el script")

# desafio 1:
#el erorr q se obtiene es: ZeroDivisionError
# a = 0. a deberia ser cualquier numero q no sea 0
#Me doy cuenta porque reemplace a por 1 y no tiro error

#NameError: name 'divisor' is not defined
#divisor no se definio anteriormente.

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# No se puede sumar un entero con un string.

#¿Qué tipo de excepción se maneja en el código anterior? "Try" y "Except"
#Se opuede manejar cualquier tipo de excepcion

#*-------------------------------------------------------------------*#

# desafio 2:

def mitades(numero):
    print (2 / numero)

mitades(6)
#mitades(9) --> retorna el resultado correcto
#mitades(0) --> retorna un error (ZeroDivisionError)

#*-------------------------------------------------------------------*#

# desafio 3:
def mitades2(numero):
    try:
        print (2 / numero)
    except:
        print ("No se puede dividir por cero")

mitades2(2)

#Excepciones personalizadas

