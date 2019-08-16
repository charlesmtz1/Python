#Ejercicio 4
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas 
#el nombre del usuario tantas veces como el número introducido.

nombre = input("Cual es tu nombre? > ")
num_impresiones = int(input("Cuantas veces quieres imprimir tu nombre? > "))

for x in range(num_impresiones):
    print(nombre)
