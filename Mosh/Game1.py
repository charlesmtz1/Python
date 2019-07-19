#Juego del numero secreto

secreto = 1
intentos = 1
win = True

print("Adivina el numero del 1 al 9!! Gana lindos premios :3")
print("Solo tienes 3 oportunidades :0")
print("Listo??")
opcion = int(input("Escribe el numero: "))


while intentos < 3:
    if opcion == secreto:
        win = True
        break
    else:
        win = False
        opcion = int(input("Incorrecto! Vuelve a intentarlo: "))
        intentos += 1

if win:
    print("Felicidades!! Haz ganado!! :D")
else:
    print("Gracias por participar!")