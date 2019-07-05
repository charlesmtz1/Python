#Una funcion es un bloque de codigo que se ejecuta cuando es llamado.

def mifuncion():
    print("Hola mundo")

mifuncion()

#Es pueden enviar parametros a una funcion con los cuales va a trabajar

def apellidos(nombre):
    print(nombre + " Hino")

apellidos("Rei")
apellidos("Mizuki")

#Se pueden definir parametros default cuando la funcion se envia vacia.
def pais(country = "Japon"):
    print("Mi familia es de " + country)

pais("Mexico")
pais("China")
pais()

#Se pueden enviar cualquier tipo de datos dentro de una funcion, y dentro de la funcion se va a respetar el tipo.
def imprimir(lista):
    for x in lista:
        print(x)

colores = ["Rojo", "Azul", "Negro"]

imprimir(colores)
