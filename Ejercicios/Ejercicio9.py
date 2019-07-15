#Ejercicio 9
#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(numero, caracter):
    txt = "\nEl caracter {} se multiplicara por {} veces..."
    print(txt.format(caracter, numero))
    return numero * caracter

print("---------------------------------")
print("---Multiplicador de caracteres---")
print("---------------------------------\n")

caracter = input("Escribe un caracter: ")
repetidor = int(input("Escribe el numero de veces que se multiplicara: "))

print(generar_n_caracteres(repetidor, caracter))

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")