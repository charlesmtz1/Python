#Ejercicio 5
#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def plus(number_list):
    plus = 0

    for number in number_list:
        plus += number
    
    return plus

def multiply(number_list):
    times = 1

    for number in number_list:
        times *= number
    
    return times


print("-----------Plus-----------")
print("------------&-------------")
print("---------Multiply---------\n")

number_list = list()
items_number = int(input("How many number have in your list?: "))

while len(number_list) < items_number:
    try:
        number_list.append(int(input(f"Set number {len(number_list) + 1}: ")))
    except ValueError:
        print("You only can set numbers!\n")

print("\nThis is your list:")
print(number_list)

while True:
    print("\nSelect one option: ")
    print("1. Plus")
    print("2. Multiply")
    print("0. Quit\n")
    
    try:
        option = int(input("> "))

        if option == 1:
            print(f"Result: {plus(number_list)}")
            break
        elif option == 2:
            print(f"Result: {multiply(number_list)}")
            break
        elif option == 0:
            break
        else:
            print("\n\nInvalid Option!!")
    except ValueError:
        print("Invalid Option!")

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")