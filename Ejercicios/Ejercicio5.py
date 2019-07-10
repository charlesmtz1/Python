#Ejercicio 5
#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(numeros):
    suma = 0
    txt = "La suma de los numeros de la lista es: {}"
    for x in numeros:
        suma += x
    print(txt.format(suma))

def multip(numeros):
    producto = 1
    txt = "El producto de los numeros de la lista es: {}"
    for x in numeros:
        producto *= x
    print(txt.format(producto))


print("-----------Sumador-----------")
print("--------------y--------------")
print("---------Multiplicador-------\n")

numeros = list((""))
elementos = int(input("Cuantos numeros vas a capturar en la lista?: "))

print("\nA continuacion, escribe los numeros que iran dentro de la lista:")
for x in range(elementos):
    txt = "Numero {}: "
    numeros.append(int(input(txt.format(x+1))))

while True:
    print("\nEsta es tu lista de numeros:")
    print(numeros)
    print("\nSelecciona una opcion del menu: ")
    print("1. Sumar")
    print("2. Multiplicar")
    print("0. Salir\n")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        sum(numeros)
        break
    elif opcion == 2:
        multip(numeros)
        break
    elif opcion == 0:
        break
    else:
        print("\n\nOpcion invalida!!")

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")