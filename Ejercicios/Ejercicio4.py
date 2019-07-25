#Ejercicio 4
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vowel_validator(char):
    vowels = "aeiou"
    is_vowel = False

    for vowel in vowels:
        if char == vowel:
            is_vowel = True
            break
    
    return is_vowel


print("-----------------------------")
print("-----Character Validator-----")
print("-----------------------------\n")

while True:
    char = input("Set a character: ").lower()

    if len(char) < 2:
        print("\nVerifyng...")
        print(f"The character is vowel?: {vowel_validator(char)}")
        break
    else:
        print("Only you can set one character!\n")
    
print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")