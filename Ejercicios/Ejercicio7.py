#Ejercicio 7
#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(cadena):
    inicio = 0
    final = len(cadena) - 1
    validador = True

    while final >= 0:
        if cadena[inicio].lower() == cadena[final].lower():
            inicio += 1
            final -= 1
        else:
            validador = False
            break

    if validador == True:
        print("La palabra es palindromo!")
    else:
        print("La palabra", cadena,"no es palindromo...")


print("------------------------------")
print("-----Validador de cadenas-----")
print("------------------------------\n")

palabra = input("Escribe una palabra: ")

es_palindromo(palabra)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")