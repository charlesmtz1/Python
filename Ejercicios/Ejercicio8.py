#Ejercicio 8
#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
#Escribir la función usando el bucle for anidado. 

def superposicion(lista1, lista2):

    elementos_en_comun = 0
    txt = "Existen {} elementos que coinciden en ambas listas"

    for x in lista1:
        for y in lista2:
            if x == y:
                elementos_en_comun += 1
            
    print(lista1)
    print(lista2)

    if elementos_en_comun > 0:
        print(txt.format(elementos_en_comun))
    else:
        print("No hay elementos en comun en ambas listas...")
            

club_de_canto = list(("Mizuki", "Umi", "Dia"))
club_de_arco = list(("Tomoyo", "Sayaka", "Hinata"))

superposicion(club_de_canto, club_de_arco)

