#Los modulos permiten una mejor organizacion de codigo, separando funciones en diferentes archivos, permitiendo asi la reutilizacion de codigo.
#En nuestro archivo modulo escribiremos una funcion de saludo.
"""
def saludo(nombre):
    print(f"Hola {nombre}")
"""

#Para llamas nuestro modulo a nuestro codigo, usaremos la funcion import
import modulo_ejemplo

#Una vez importado, podremos utilizar las funciones que estan incluidas dentro del modulo para nuestro codigo principal.

modulo_ejemplo.saludo("Carlos")

#Tambien se puede acceder a variables y cambiarles su valor.

print(modulo_ejemplo.variable_ejemplo)

modulo_ejemplo.variable_ejemplo = 100

print(modulo_ejemplo.variable_ejemplo)

#Los modulos pueden tener un alias al momento de ser importados.
import modulo_ejemplo as caja

caja.saludo("Rei")


#Python incluye muchos modulos precargados, y permite ampliar las posibilidades de programacion.
import math
import random
import platform

x = platform.system()   #Valida el OS que estamos utilizando

print(x)    #Imprime el OS

#El comando dir nos permite ilustrar todas las funciones de un modulo para conocerlas.
x = dir(platform)

print(x)

#Si solo se quiere acceder a una funcion de un modulo, utilizaremos el comando from
from modulo_ejemplo import saludo

saludo("Carlos")
