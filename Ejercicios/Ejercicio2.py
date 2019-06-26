#Ejercicio 2
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("El primer numero es el mayor:", num1)
    elif num2 > num1 and num2 > num3:
        print("El segundo numero es el mayor:", num2)
    else:
        print("El tercer numero es el mayor:", num3)


primero = 5
segundo = 7
tercero = 9

max_de_tres(primero, segundo, tercero)