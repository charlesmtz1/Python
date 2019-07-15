#Ejercicio 14
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 

def mayusculas(cadena):
    num_mayus = 0

    for x in cadena:
        if x == x.upper():
            num_mayus += 1

    print(f'La palabra tiene {num_mayus} mayusculas.')

cadena = input("Escribe una cadena: ")

mayusculas(cadena)