#Ejercicio 18
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def buscar(letra, nombres):
    for x in nombres:
        for y in x:
            if y[0] == letra


nombres = list(("Rei", "Carlos", "Dia"))

letra = input("Escribe la primera letra de los nombres que deseas encontrar: ")

buscar(letra, nombres)
