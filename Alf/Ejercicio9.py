#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla 
# el capital obtenido en la inversión.

capital = int(input("Cuanto es la cantidad de dinero que vas a invertir? > "))
interes = int(input("Que porcentaje de interes vas a manejar? > "))
años = int(input("Por cuantos años vas a realizar la inversion? > "))


inversion = capital * ((1 + interes/100) * años)

print(f"El capital obtenido de la inversion es de ${inversion}")
