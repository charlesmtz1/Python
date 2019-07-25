#Ejercicio 7
#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def is_palindrome(string):
    opposite_position = len(string) - 1
    palindrome = True

    for char in string:
        if char == string[opposite_position]:
            opposite_position -= 1
        else:
            palindrome = False
            break

    return palindrome


print("------------------------------")
print("-----Palindrome Validator-----")
print("------------------------------\n")

string = input("Set a string: ").lower()

print(f"Your string is palindrome?: {is_palindrome(string)}")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")