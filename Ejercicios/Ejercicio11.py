#Ejercicio 11
#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. 
#Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(numeros):
    print("\nSe validaran los siguientes numeros:")
    print(numeros)
    num_mayor = numeros[0]
    txt = "\nEl numero mayor es: {}"

    for x in range(len(numeros)):
        if num_mayor < numeros[x]:
            num_mayor = numeros[x]

    print(txt.format(num_mayor))
        

print("----------------------------")
print("----Validador de numeros----")
print("----------------------------\n")

numeros = list()

for x in range(int(input("Escribe la cantidad de numeros que se van a comparar: "))):
    numeros.append(int(input("Agrega un numero a la lista: ")))

max_in_list(numeros)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")