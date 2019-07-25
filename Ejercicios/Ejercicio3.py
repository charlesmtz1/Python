#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada.

def lenght(user_string_list):
    lenght = 0

    for x in user_string_list:
        lenght += 1

    return lenght


print("----------------------------------")
print("-----Strings and lists Lenght-----")
print("----------------------------------\n")

option = 0

while True:
    try:
        print("What kind of data wish you to verify?:")
        print("1. String.")
        print("2. List")
        print("0. Quit\n")

        option = int(input(">"))

        if option == 1:
            string = input("Set a string: ")
            print("\nVerifing...")
            print(f"String lenght: {lenght(string)}")
            break    
        elif option == 2:
            items_list = list()
            items_number = int(input("How many items have in your list?: "))
            
            for item in range(items_number):
                items_list.append(input("Set the item: "))

            print("\nVerifing...")
            print(f"List lenght: {lenght(items_list)}")
            break
        elif option == 0:
            break
        else:
            print("Invalid Option!\n")
                
    except ValueError:
        print("Invalid Option!\n")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")