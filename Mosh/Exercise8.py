#Write a program to remove the duplicates in a list.

numeros = [2, 4, 7, 4, 4, 4, 4, 4, 8, 8, 10, 8, 8, 7, 8]

print(numeros)

for item in numeros:
    if numeros.count(item) > 1:
        for x in range(numeros.count(item) - 1):
            numeros.remove(item)

numeros.sort()

print(numeros)

#Solucion 2

numbers = [2, 2, 3, 5, 7, 8, 5, 7, 9]
unicos = []

for item in numbers:
    if item not in unicos:
        unicos.append(item)

print(unicos)