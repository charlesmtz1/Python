#Los sets son colecciones de datos que no tienen un orden definido ni un indice. se declaran entre llaves.
myset = {"Rei", "Dia", "Umi"}

print(myset) #Los elementos seran impresos de forma aleatoria, debido a que un set no cuenta con un orden definido.

#LOS SETS NO PUEDE SER ACCEDIDO A SUS ELEMENTOS DE FORMA DEFINIDA. Es decir, no se puede utilizar esta declaracion:
# print(myset[0])
#Debido a que los elementos de un set no tienen indice.
#Sin embargo, se puede acceder a los elementos de forma generica o se puede validar si un elemento se encuentra dentro de un set.
for x in myset:
    print(x) #Los elementos seran impresos de forma aleatoria

if "Rei" in myset:
    print("♥")

#LOS SETS NO PERMITEN AGREGAR ELEMENTOS DE FORMA INDEXADA. Estas instrucciones no estan permitidas:
# myset.append("Ruby")
# myset.insert(0, "Ruby")
#Sin embargo se pueden agregar elementos con la funcion add()
myset.add("Yoshiko")
print(myset)

#Tambien se puede incluir multiples elementos al set con la funcion update()
myset.update(["Ruby", "Haruna-Chan"]) #IMPORTANTE! La funcion update() lleva corchetes dentro de los parentesis para agregar los elementos al set.
print(myset)

#Se puede obtener la longitud de un set con la funcion len()
print(len(myset))

#Se pueden remover elementos de un set usando remove() o discard().
#remove() se recomienda usar cuando conocemos el elemento que queremos eliminar del set
#discard() se recomienda cuando no se tiene certeza que el elemento este dentro del set.

myset.remove("Ruby")
print(myset)

myset.discard("Shiho")
print(myset)

#Tambien se puede utilizar la funcion pop(), sin embargo pop() elimina el ultimo elemento del set, pero debido a que es aleatorio, no sabremos con certeza
#el elemento eliminado. Se puede conocer dicho elemento si se almacena en una variable durante su ejecucion.
pop = myset.pop()
print(pop)

print(myset)

#clear() deja vacio el set, mientras que el comando del lo elimina completamente.
myset.clear()
print(myset)

del myset

#Se puede utilizar el constructor set() para generar nuevos sets desde una variable, o bien para realizar una copia de las mismas
primeset = set(("Rei", "Dia", "Mizuki")) #INCLUYE DOBLES PARENTESIS!!!

primeset2 = set(primeset)

print(primeset)
print(primeset2)




