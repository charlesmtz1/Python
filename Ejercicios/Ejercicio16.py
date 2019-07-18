#Ejercicio 16
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

def registro(personas):
    for x in range(num_personas):
        nombre_persona = input(f'\nComo se llama la persona {x+1}?: ')
        año_nacimiento = int(input("En que año nacio?: "))
        personas.append(dict(Nombre= nombre_persona, Año_de_Nacimiento= año_nacimiento))
        print("Persona registrada con exito!")

def mostrar(persona):
    return print(persona)

def calcula_edad(personas, año_actual):
    print("\nSe muestran las personas ingresadas con sus edades actuales:")

    for x in personas:
        edad = año_actual - x['Año_de_Nacimiento']
        x["Edad"] = edad
        mostrar(x)

print("-------------------------------")
print("------Validador de edades------")
print("-------------------------------\n")

personas = list()

año_actual = int(input("Escribe el año en curso: "))
num_personas = int(input("Cuantas personas seran incluidas en la lista?: "))

registro(personas)

#mostrar(personas)

calcula_edad(personas, año_actual)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")