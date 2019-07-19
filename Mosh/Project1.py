#Proyecto 1
#Creacion de un programa que calcula libras o kilos de una persona

peso = float(input("Cual es tu peso?: "))
opcion = input("Lo quieres visualisar en libras(L) o Kilos(K)?: ")

if opcion.lower() == 'l':
    print(f"Tu peso en libras es: {peso / 0.453592}")
elif opcion.lower() == 'k':
    print(f"Tu peso en kilogramos es: {peso * 0.453592}")
else:
    print("Opcion incorrecta!")