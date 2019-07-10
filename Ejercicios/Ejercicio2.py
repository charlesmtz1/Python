#Ejercicio 2
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_de_tres(num1, num2, num3):
    print("\nValidando tres numeros...")
    txt = "El numero mayor es: {}"

    if num1 == num2 and num1 == num3:
        print("Todos los numeros son iguales!!")
    elif num1 > num2 and num1 > num3:
        print(txt.format(num1))
    elif num2 > num1 and num2 > num3:
        print(txt.format(num2))
    else:
        print(txt.format(num3))


print("----------------------------")
print("----Validador de numeros----")
print("----------------------------\n")

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
num3 = int(input("Escribe el ultimo numero: "))

max_de_tres(num1, num2, num3)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")