#Ejercicio 8
#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
#Escribir la función usando el bucle for anidado. 

def superposicion(lista1, lista2):
    elementos_en_comun = 0
    txt = "\nExisten {} miembros que coinciden en ambos clubes"

    for x in lista1:
        for y in lista2:
            if x == y:
                elementos_en_comun += 1
    
    print("")
    print(lista1)
    print(lista2)

    if elementos_en_comun > 0:
        print(txt.format(elementos_en_comun))
    else:
        print("\nNo hay miembros en comun en ambos clubes :( ")
            

print("-------------------------------")
print("------Validador de listas------")
print("-------------------------------\n")

club_de_canto = list()
club_de_cocina = list()

for x in range(int(input("Cuantos integrantes tiene el club de canto?: "))):
    club_de_canto.append(input("Ingresa al miembro del club!: "))

for x in range(int(input("\nCuantos integrantes tiene el club de cocina?: "))):
    club_de_cocina.append(input("Ingresa al miembro del club!: "))

superposicion(club_de_canto, club_de_cocina)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")