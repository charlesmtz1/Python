#Ejercicio 12
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(palabras):
    print("\nEsta es tu lista de palabras:")
    print(palabras)
    palabra_mayor = palabras[0]
    txt = "\nLa palabra mas larga es: {}"

    for x in range(len(palabras)):
        if len(palabra_mayor) < len(palabras[x]):
            palabra_mayor = palabras[x]

    print(txt.format(palabra_mayor))


print("------------------------------")
print("-----Validador de cadenas-----")
print("------------------------------\n")

palabras = list()

for x in range(int(input("Cuantas palabras vas a agregar a tu lista?: "))):
    palabras.append(input("Agrega una palabra a tu lista: "))

mas_larga(palabras)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")