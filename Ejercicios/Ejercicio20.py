#Ejercicio 20
#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto. Un año bisiesto es divisible por 4, pero no por 100. 
#También es divisible por 400

def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        print("\nEl año es bisiesto!")
    else:
        print("\nEl año no es bisiesto...")

print("--------------------------------")
print("------Validador de cadenas------")
print("--------------------------------\n")

año = int(input("Escribe un año para calcular si es bisiesto: "))

es_bisiesto(año)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")