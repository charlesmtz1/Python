#Ejercicio 15
#Construir un pequeño programa que convierta números binarios en enteros. 

def convertidor(binario):
    num_entero = 0
    exponente = 1
    posicion = len(binario) - 1

    for x in range(len(binario)):
        if binario[posicion] == '1':
            num_entero += (int(binario[posicion]) * exponente)
            exponente *= 2
            posicion -= 1
        else:
            exponente *= 2
            posicion -= 1

    return num_entero
    

def validador(binario):
    num_valido = True

    for x in binario:
        if x == '1' or x == '0':
            continue
        else:
            num_valido = False
            break

    return num_valido


print("------------------------------")
print("-----Validador de numeros-----")
print("------------------------------\n")

num_binario = input("Escribe un numero en formato binario: ")

if validador(num_binario):
    print(f'\nEl numero binario convertido a entero es: {convertidor(num_binario)}')
else:
    print("\nEl numero ingresado no es valido!!")

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")