#Juego del numero secreto

secreto = 1
intentos = 1

print("Adivina el numero del 1 al 9!! Gana lindos premios :3")
print("Solo tienes 3 oportunidades :0")
print("Listo??")

while intentos < 4:
    opcion = int(input("\nEscribe el numero: "))

    if opcion == secreto:
        print("\nFelicidades!! Haz ganado!! :D")
        break
    else:
        if intentos != 3:
            print("Incorrecto! Vuelve a intentarlo!")
        intentos += 1
else:
    print("\nGracias por participar!")
    