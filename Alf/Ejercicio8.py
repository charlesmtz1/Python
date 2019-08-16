#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
# los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num_1 = int(input("Escribe un numero> "))
num_2 = int(input("Escribe otro numero> "))

cociente = num_1 // num_2
resto = num_1 % num_2

print(f"La division de {num_1} entre {num_2} da un cociente {cociente} y un resto {resto}")
