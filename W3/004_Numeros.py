#Tipos de numeros en Python

entero = 10 #Variable entera, puede ser positiva o negativa y no tiene limite de numeros
flotante = 5.25 #Variable flotante, puede ser positiva o negativa. puede usarse una E para el manejo de exponenciales
complejo = 3j #Numero complejo. Siempre van acompañados de una j.

#La funcion Type permite mostrar el tipo de una variable declarada.
print(type(entero))
print(type(flotante))
print(type(complejo))

print(entero + complejo)

#Existen formas de convertir los numeros entre los diferentes tipos:

a = float(entero)
b = complex(entero)
c = int(flotante)

print(a, b, c)

print(type(a))
print(type(b))
print(type(c))

#Se pueden generan numero aleatorios con el modulo random. No existe de forma nativa una funcion random()
import random

print(random.randrange(1,10))
