#Ejercicio 30
#Para un número N imprimir su tabla de multiplicar.

def tabla_multiplicar(numero):
    for valor in range(1,11):
        print(f"{numero} x {valor} = {numero * valor}")


numero = int(input("Escribe un numero: "))

print("Se muestra su tabla de multiplicar:")
tabla_multiplicar(numero)
