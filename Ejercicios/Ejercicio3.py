#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud(cadena):
    tamano = 0
    print("Validando cadena...")
    for x in cadena:
        print("Caracter recibido:", x)
        tamano += 1

    print("El tamaño de la cadena es de:", tamano)

def longitud_lista(lista):
    elementos = 0
    print("Validando lista...")
    for x in lista:
        print("Elemento procesado:", x)
        elementos += 1

    print("El numero de elementos en la lista es de:", elementos)


cadena = "Intel"
lista = list(("Rei", "Dia", "Umi"))

longitud(cadena)
print("---------------------------")
longitud_lista(lista)

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")
