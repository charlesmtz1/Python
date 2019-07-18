#Ejercicio 17
#Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def registrar(personas, nombre, edad):
    personas.append(dict(Nombre= nombre, Edad= edad))
    return print("Persona registrada con exito!\n")

def mostrar(personas):
    print("\nLista de personas registradas:")

    for x in personas:
        print(x)

def mayor_de_20(personas):
    print("\nEstas personas son mayores de 20 años:")

    for x in personas:
        if x["Edad"] > 20:
            print(x)
        else:
            continue

print("-------------------------------")
print("------Validador de edades------")
print("-------------------------------\n")

personas = list()

for x in range(10):
    nombre = input(f'Escribe el nombre de la persona {x+1}: ')
    edad = int(input("Que edad tiene?: "))
    registrar(personas, nombre, edad)

mostrar(personas)

mayor_de_20(personas)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")