#Las listas son colecciones de datos que es ordenada y puede ser cambiado alguno de sus elementos. se declaran entre corchetes.

lista = ["Dia", "Umi", "Yoshiko"]

print(lista)
print(lista[1])

#Se puede modificar los elementos de una lista
lista[2] = "Cebollita"
print(lista)

#Se puede recorrer una lista con la instruccion FOR
for x in lista:
    print(x)

#Se puede hacer una validacion de elementos dentro de una lista
if "Dia" in lista:
    print("Si esta en la lista!")

#Se pueden utilizar funciones para cadenas en las listas
print(len(lista))

#Se pueden agregar elementos adicionales a la lista con la funcion append(). Append coloca el elemento nuevo en la ultima posicion
lista.append("Ruby")

print(lista)

#Con la funcion insert() podemos colocar el nuevo elemento en la posicion que definamos.
lista.insert(0, "Rei")
print(lista)

#Se pueden remover elementos de la lista con la funcion remove()
lista.remove("Ruby")
print(lista)

#Con la funcion pop() se elimina el ultimo elemento de la lista.
lista.pop()
print(lista)

#La instruccion del puede eliminar un elemento en la posicion que definamos. Tambien se puede borrar la lista completa.
del lista[2]
print(lista)

del lista

#La funcion clear() limpia la lista de registros, pero sin destruir la variable
lista = ["Dia", "Umi", "Yoshiko"]
print(lista)
lista.clear()

print(lista)

#Las listas tambien se pueden copiar, sin embargo no se puede realizar una asignacion de este tipo: lista1 = lista2
#Al hacer una asignacion de este tipo, lo que genera es solo una referencia, mas no una copia de la variable.
#Para realizar una copia de una lista a una nueva variable, se ocupa la funcion copy()
lista = ["Dia", "Umi", "Yoshiko"]

mylist = lista.copy()
print(mylist)

#Se puede utilizar el constructor list() para generar nuevas listas desde una variable, o bien para realizar una copia de las mismas
primelist = list(("Rei", "Dia", "Mizuki")) #INCLUYE DOBLES PARENTESIS!!!

primelist2 = list(primelist)

print(primelist)
print(primelist2)

