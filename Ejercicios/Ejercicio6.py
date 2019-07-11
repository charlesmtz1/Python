#Ejercicio 6
#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    posicion = len(cadena) - 1
    invertida = ""
    txt = "\nSe ha devuelto la cadena invertida: {}"

    while posicion >= 0:
        invertida += cadena[posicion]
        posicion -=1

    print(txt.format(invertida))


print("------------------------------")
print("-----Validador de cadenas-----")
print("------------------------------\n")

cadena = input("Escribe una cadena: ")

inversa(cadena)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")