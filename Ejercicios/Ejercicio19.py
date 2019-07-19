#Ejercicio 19
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0

    for x in palabra:
        if x.lower() == 'a':
            num_a += 1
        elif x.lower() == 'e':
            num_e += 1
        elif x.lower() == 'i':
            num_i += 1
        elif x.lower() == 'o':
            num_o += 1
        elif x.lower() == 'u':
            num_u += 1
        else:
            continue
    print(f"\nPalabra analizada: {palabra}")
    print(f"Vocales encontradas:")
    print(f"A: {num_a}")
    print(f"E: {num_e}")
    print(f"I: {num_i}")
    print(f"O: {num_o}")
    print(f"U: {num_u}")


print("--------------------------------")
print("------Validador de cadenas------")
print("--------------------------------\n")

palabra = input("Escribe una palabra o nombre: ")

contar_vocales(palabra)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")