#Ejercicio 4
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def validador(caracter):
    vocales = "aeiou"
    no_vocal = True

    print("\nValidando caracter insertado...")

    for x in vocales:
        if caracter.lower() == x:
            no_vocal = False
            txt = "El caracter {} es una vocal!"
            print(txt.format(caracter.upper()))
            break
    
    if no_vocal == True:
        txt = "El caracter {} no es vocal..."
        print(txt.format(caracter.upper()))


print("-----------------------------")
print("---Validador de caracteres---")
print("-----------------------------\n")

while True:
    caracter = input("Escribe un caracter: ")

    if len(caracter) < 2:
        validador(caracter)
        break
    else:
        print("Solo se puede escribir un caracter!\n")
    

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")