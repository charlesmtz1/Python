#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Escribe un numero > "))
aux = 1

while aux <= numero:
    if (aux % 2) != 0:
        print(f"{aux}, ", end="")

    aux += 1
