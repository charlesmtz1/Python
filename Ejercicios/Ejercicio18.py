#Ejercicio 18
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def buscar(letra, nombres):
    cantidad_nombres = 0
    nombres_encontrados = list()

    for x in nombres:
        if x[0].lower() == letra or x[0].upper() == letra:
            nombres_encontrados.append(x)
            cantidad_nombres += 1

    print(f"\nNombres encontrados que coinciden con la letra ingresada: {cantidad_nombres}")
    print(f"Nombres encontrados: {nombres_encontrados}")


print("--------------------------------")
print("------Validador de cadenas------")
print("--------------------------------\n")

nombres = list(("Rei", "Carlos", "Dia", "Riko", "Mizuki", "Rin", "Rosa"))

letra = input("Escribe la primera letra de los nombres que deseas encontrar: ")

buscar(letra, nombres)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")