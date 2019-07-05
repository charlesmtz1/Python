#Ejercicio 4
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def validador(caracter):
    print("Validando caracter insertado...")

    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        txt = "El caracter {} es una vocal!"
        print(txt.format(caracter.upper()))
    else:
        txt = "El caracter {} no es vocal..."
        print(txt.format(caracter.upper()))


caracter = 'r'

validador(caracter)

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")