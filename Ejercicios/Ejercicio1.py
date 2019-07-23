#Ejercicio 1
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(number_list):
    if number_list[0] > number_list[1]:
        return number_list[0]
    else:
        return number_list[1]


print("----------------------------")
print("------Number Validator------")
print("----------------------------\n")

number_list = list()
sets = 1

while sets <= 2:
    try:
        number_list.append(int(input(f"Set number {sets}: ")))
    except ValueError:
        print("Invalid character!")
    else:
        sets += 1

print("\nVerifing...")
print(f"The biggest number is: {max(number_list)}")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")