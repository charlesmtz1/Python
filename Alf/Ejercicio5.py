#Ejercicio 5
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por 
# pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre = input("Cual es tu nombre? > ").upper()
num_letras = 0

for x in nombre:
    num_letras += 1

print(f"El nombre {nombre} tiene {num_letras} letras!")
