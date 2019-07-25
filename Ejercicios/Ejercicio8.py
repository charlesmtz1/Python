#Ejercicio 8
#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
#Escribir la función usando el bucle for anidado. 

def common_finder(club_1, club_2):
    common_members = 0

    for member_club_1 in club_1:
        for member_club_2 in club_2:
            if member_club_1 == member_club_2:
                common_members += 1

    return common_members
            

print("-------------------------------")
print("---------Compare Lists---------")
print("-------------------------------")

singing_club = list()
cooking_club = list()

while True:
    try:
        for x in range(int(input("\nHow many members have the singing club?: "))):
            singing_club.append(input("Set member name!: "))
        break
    except ValueError:
        print("Only set numbers!")

while True:
    try:
        for x in range(int(input("\nHow many members have the cooking club?: "))):
            cooking_club.append(input("Set member name!: "))
        break
    except ValueError:
        print("Only set numbers!")

print("\nClub list:")
print(f"Singing club: {singing_club}")
print(f"Cooking club: {cooking_club}")

print(f"\nExists {common_finder(singing_club, cooking_club)} common members in both clubs.")

print("\n----------------------------")
print("----------Finished----------")
print("----------------------------")