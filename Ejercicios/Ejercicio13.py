#Ejercicio 13
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista, filtro):
    print("\nEsta es la lista que se aplicara el filtro:")
    print(lista)

    print("\nEstas son las palabras que fueron filtradas de la lista:")
    for x in lista:
        if len(x) >= filtro:
            print(x)


print("------------------------------")
print("-----Validador de cadenas-----")
print("------------------------------\n")

palabras = list()

for x in range(int(input("Escribe el numero de palabras que se agregaran a la lista: "))):
    palabras.append(input("Agrega una palabra a la lista: "))
    
max_caracteres = int(input("\nEscribe el minimo de caracteres que tienen que tener las palabras para ser filtradas: "))

filtrar_palabras(palabras, max_caracteres)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")