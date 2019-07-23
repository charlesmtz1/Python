#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada.

def string_lenght(string):
    lenght = 0

    for x in string:
        lenght += 1

    return lenght


def longitud_lista(lista, elementos):
    txt = "El numero de elementos en la lista es de: {} \n\n"
    validador = "Elemento procesado: {}"

    print("\nValidando lista...")
    for x in lista:
        print(validador.format(x))
        elementos += 1

    print(txt.format(elementos))


print("----------------------------------")
print("-----Strings and lists Lenght-----")
print("----------------------------------\n")

option = 0

while True:
    print("What kind of data wish you to verify?:")
    print("1. String.")
    print("2. List")
    print("0. Quit\n")

    option = int(input(">"))

    if option == 1:
        string = input("Set a string: ")
        print("\nVerifing...")
        print(f"String lenght: {string_lenght(string)}")
        break    
    elif option == 2:
        lista = list()
        items = int(input("Cuantos elementos tendra tu lista?: "))
        
        while items > 0:
            lista.append(input("Escribe el elemento de la lista: "))
            items -= 1

        longitud_lista(lista, items)
    elif option == 0:
        break
    else:
        print("Opcion no valida!\n")

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")