#Ejercicio 13
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Escribe el numero a dividir > "))
divisor = int(input("Escribe el numero por cuando vas a dividir > "))

if divisor != 0:
    print(f"La division entre ambos numeros es: {dividendo / divisor}")
else:
    print("El divisor no puede ser 0!")
