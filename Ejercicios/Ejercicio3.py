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


print("----------------------------------")
print("---Longitud de cadenas y listas---")
print("----------------------------------")
print("")

opcion = 0

while opcion == 0:
    print("Que tipo de dato deseas analizar? Selecciona la opcion del menu:")
    print("1. Cadena.")
    print("2. Lista")
    print("0. Salir")
    print("")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        cadena = input("Escribe una cadena: ")
    elif opcion == 2:
        elemento = int(input("Cuantos elementos tendra tu lista?: "))


longitud(cadena)
print("---------------------------")
#longitud_lista()

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")