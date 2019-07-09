#Ejercicio 7
#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(cadena):

    start = 0
    end = len(cadena)
    validador = 0

    for x in cadena:
        if cadena[start].lower() == cadena[end-1].lower():
            validador += 1
            start += 1
            end -= 1

    if validador == len(cadena):
        print("La palabra es palindromo!")
    else:
        print("La palabra no es palindromo...")


palabra = "HopoH"

es_palindromo(palabra)