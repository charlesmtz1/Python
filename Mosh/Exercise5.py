#


name = input("Escribe tu nombre: ")

if len(name) < 3:
    print("Tu nombre ocupa mas de 3 caracteres")
elif len(name) > 50:
    print("Solo se admite un maximo de 50 caracteres")
else:
    print("Tu nombre es genial!")