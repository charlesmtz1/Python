#La funcion input permite ingresar datos a la consola de Python
input("Cual es tu nombre?: ")

#Tambien permite asignar valores a una variable que declaremos
nombre = input("Cual es tu nombre?: ")

print(nombre)

#OJO, todos los datos que pasan por la funcion input pasan como cadenas. Si se desea pasar numeros enteros, es importante convertirlos!
edad = int(input("Cuantos años tienes?: "))
print(type(edad))

#Se puede combinar con funciones de cadena o de lista para añadir elementos o eliminarlos.

lista = ['Carlos', 'Rei']
lista.append(input("Inserta un dato a la lista: "))

print(lista)

lista.remove(input("Elimina un dato de la lista: "))
print(lista)