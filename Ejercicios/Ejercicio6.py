#Ejercicio 6
#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def invert_string(string):
    position = len(string) - 1
    inverted_string = ""

    while position >= 0:
        inverted_string += string[position]
        position -=1

    return inverted_string


print("------------------------------")
print("--------String Reverse--------")
print("------------------------------\n")

string = input("Set a string: ")

print(f"Inverted string: {invert_string(string)}")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")