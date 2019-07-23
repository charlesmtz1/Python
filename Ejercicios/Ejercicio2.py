#Ejercicio 2
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_of_three(number_list):
    max = 0

    for number in number_list:
        if number > max:
            max = number
    
    return max


print("----------------------------")
print("------Number Validator------")
print("----------------------------\n")

number_list = list()
sets = 1

while sets <= 3:
    try:
        number_list.append(int(input(f"Set number {sets}: ")))
    except ValueError:
        print("Invalid character!")
    else:
        sets += 1

print("\nVerifing...")
print(f"The biggest number is: {max_of_three(number_list)}")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")