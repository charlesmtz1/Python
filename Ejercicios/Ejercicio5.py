#Ejercicio 5
#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(numeros):
    suma = 0

    for x in numeros:
        suma += x
    
    print("La suma de los numeros de la lista es:", suma)

def multip(numeros):
    producto = 1

    for x in numeros:
        producto *= x

    print("El producto de los numeros de la lista es:", producto)
    

lista = list((1,2,3,4))

sum(lista)
multip(lista)

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")