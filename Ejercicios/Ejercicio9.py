#Ejercicio 9
#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def character_multiplier(char, multiply_times):
    return char * multiply_times

print("----------------------------------")
print("-------Character Multiplier-------")
print("----------------------------------\n")

char = input("Set a character > ")

while True:
    try:
        multiply_times = int(input("How many times you want to multiply your character? >  "))
        break
    except ValueError:
        print("Only set numbers!")

print(f"\nResult: {character_multiplier(char, multiply_times)}")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")