#Ejercicio 18
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Escribe tu edad > "))
años = 1

while años <= edad:
    print(años)
    años += 1
