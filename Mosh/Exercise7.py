#Write a program to find the largest number in a list

numeros = list((10,11,9,1,12))

max = 0

for item in numeros:
    if max < item:
        max = item

print(max)    