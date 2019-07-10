#Ejercicio 1
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(num1, num2):
    print("\nValidando numeros...")
    txt = "El numero mayor es: {}"

    if num1 > num2:
        print(txt.format(num1))
    elif num1 == num2:
        print("Ambos numeros son iguales!")
    else:
        print(txt.format(num2))


print("----------------------------")
print("----Validador de numeros----")
print("----------------------------\n")

num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))

max(num1, num2)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")