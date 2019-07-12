#El modulo MATH permite realizar operaciones matematicas mas complejas. Se declara de la siguiente manera:
import math

#Algunas funciones matematicas se pueden utilizar sin importar el modulo, como son el valor absoluto y el redondeo.
x = 10.2
y = -8

print(round(x))
print(abs(y))

#Funciones como seno, coseno, tangente, etc, deben ser llamados del modulo math
print(math.cos(0.5))
print(math.tan(0.5))
print(math.sin(0.5))

#Se pueden combinar para realizar operaciones complejas con otras variables.
z = 10 * math.cos(0.5)
print(z)

#Aqui hay otras funciones del modulo MATH
print(math.floor(x))
print(math.ceil(x))