#Ejercicio 1
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(num1, num2):
    if num1 > num2:
        print("El numero mayor es:", num1)
    else:
        print("El numero mayor es:", num2)

x = 3
y = 5

max(x, y)
