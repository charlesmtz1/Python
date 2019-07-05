#Los diccionarios son colecciones de datos que no tienen un orden definido , pero pueden ser cambiados e indexados. Se declaran entre llaves y especificando el nombre del indice.

diccionario = {
    "Marca" : "Ford",
    "Modelo" : "Mustang",
    "Año" : 1996
}

print(diccionario)

#Se puede acceder a los datos del diccionario haciendo referencia a su indice. Tambien se puede utilizar la funcion get()
x = diccionario["Modelo"]
print(x)

y = diccionario.get("Marca")
print(y)

#Se pueden cambiar los datos de un diccionario apuntando a su indice.
diccionario["Año"] = 1968

print(diccionario)

#Tambien se puede acceder al diccionario imprimiendo cada uno de sus elementos. Hay varias formas de hacerlo.
#Aqui solamente imprimira los indices del diccionario
for x in diccionario:
    print(x)

#Aqui imprimira los valores de los elementos indexados
for x in diccionario:
    print(diccionario[x])

#Aqui imprimira los valores de los elementos indexados utilizando la funcion values()
for x in diccionario.values():
    print(x)

#items() permite imprimir tanto el indice como el valor almacenado. Es importante definir dos variables para este FOR.
for x, y in diccionario.items():
    print(x, y)


#Se puede validar si existe algun indice dentro del diccionario.
if "Modelo" in diccionario:
    print("Si hay modelo")

#Se puede conocer la longitud de un diccionario.
print(len(diccionario))

#Se pueden insertar datos adicionales junto con su indice en el diccionario.
diccionario["Color"] = "Negro"
print(diccionario)

#Se pueden remover elementos de un diccionario utilizando pop() y haciendo referencia al indice.
diccionario.pop("Color")
print(diccionario)

#Tambien se puede remover el ultimo dato insertado con la funcion popitem()
diccionario["Puertas"] = 4
print(diccionario)

diccionario.popitem()
print(diccionario)

#Se puede utilizar el comando del para borrar un indice en particular o el diccionario completo.
del diccionario["Año"]
print(diccionario)

diccionario.clear() #clear() limpia el diccionario sin eliminarlo.
print(diccionario)

del diccionario

#Para poder copiar un diccionario es necesario utilizar la funcion copy()
diccionario = {
    "Marca" : "Ford",
    "Modelo" : "Mustang",
    "Año" : 1996
}

diccionario2 = diccionario.copy()
diccionario2["Modelo"] = "Figo"

print(diccionario)
print(diccionario2)

#Se puede utilizar el constructor dict() para generar nuevos diccionarios desde una variable, o bien para realizar una copia de las mismas
primedict = dict(marca= "Ford", modelo= "Mustang", año= 1996)

primedict2 = dict(primedict)

print(primedict)
print(primedict2)
