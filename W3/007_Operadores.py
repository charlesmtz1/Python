#Operadores Aritmeticos

x = 10
y = 5

suma = x + y
resta = x - y
multi = x * y
div = x / y
mod = x % y
exp = x ** y
floor = x //y

print(suma)
print(resta)
print(multi)
print(div)
print(mod)
print(exp)
print(floor)

#Operadores de asignacion
#Estos operadores permiten de manera sintetizada sustituir una asignacio x = x + 1, a una asi: x += 1
x = 10
x += 10
y -= 3
y *= 2

print(x)
print(y)

#Operadores de comparacion.
if (x == 10):
    print("True")

if (x < 30):
    print("True")

if (x <= 20):
    print("True")

if (x != 10):
    print("True")

#Operadores logicos
if (x > 10 and y < 20):
    print("Acierto")

if (x > 10 or y == 5):
    print("Acierto")

#Operadores de identidad.
if (x is y):
    print("Verdad")

if (x is not y):
    print("Verdad")
