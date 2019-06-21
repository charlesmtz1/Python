#A partir de las funciones de tipo de variable, se pueden realizar conversiones, de acuerdo a las posibilidades de cada
#tipo de variable.

#Al hacer conversiones a enteros, se puede hacer con numeros directos en la funcion o por medio de variables.
#Si se quiere convertir una cadena a entero, es importante que la cadena solo incluya numeros, de lo contrario marcara error.
a = int(2)
b = int(3.5)
c = int("7")

print(a, b, c)

#Al hacer conversiones a flotantes, se puede hacer con numeros directos en la funcion o por medio de variables.
#Si se quiere convertir una cadena a flotante, es importante que la cadena solo incluya numeros junto a su decimal, 
#de lo contrario marcara error.
d = float(4)
e = float(7.8)
f = float("10")
g = float("15.2")

print(d, e ,f, g)

#Al hacer conversiones a cadena, se puede hacer con numeros directos en la funcion o por medio de variables.
#Las cadenas no cuentan con restriccion de conversion.
h = str(1)
i = str(6.3)
j = str("9")

print(h, i ,j)

print(type(h))
print(type(i))
print(type(j))
