#Ejercicio 5
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un 
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

grupo_A = list()
grupo_B = list()
nombres_seccion1 = "ABCDEFGHIJKLM"
nombres_seccion2 = "NOPQRSTUVWXYZ"


while True:
    nombre = input("Escribe el nombre del alumno > ").upper()
    sexo = input("Cual es el sexo del alumno? (M/F) > ").upper()

    if (nombre[0] in nombres_seccion1 and sexo == 'F') or (nombre[0] in nombres_seccion2 and sexo == 'M'):
        grupo_A.append(nombre)
    else:
        grupo_B.append(nombre)


    print(f"Grupos actuales: \n Grupo A: \n {grupo_A} \n Grupo B: \n {grupo_B}")

    if input("Desea agregar mas alumnos? (Y/N) > ").upper() != 'Y':
        del grupo_A
        del grupo_B
        break
    