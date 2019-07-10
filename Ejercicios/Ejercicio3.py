#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud(cadena):
    tamano = 0
    txt = "El tamaño de la cadena es de: {} \n\n"
    validador = "Caracter recibido: {}"

    print("\nValidando cadena...")
    for x in cadena:
        print(validador.format(x))
        tamano += 1

    print(txt.format(tamano))

def longitud_lista(lista, elementos):
    txt = "El numero de elementos en la lista es de: {} \n\n"
    validador = "Elemento procesado: {}"

    print("\nValidando lista...")
    for x in lista:
        print(validador.format(x))
        elementos += 1

    print(txt.format(elementos))


print("----------------------------------")
print("---Longitud de cadenas y listas---")
print("----------------------------------\n")

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
        longitud(cadena)
        del cadena
        
    elif opcion == 2:
        elementos = int(input("Cuantos elementos tendra tu lista?: "))
        lista = list((""))

        while elementos > 0:
            lista.append(input("Escribe el elemento de la lista: "))
            elementos -= 1

        longitud_lista(lista, elementos)
        del lista
        del elementos

    elif opcion == 0:
        break

    else:
        print("Opcion no valida!")
    
    opcion = 0

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")