#Para imprimir en pantalla utilizaremos el siguiente comando:
print("Hello Python!")

#Si queremos imprimir pero no queremos salto de linea, utilizaremos un end="" al final:
print("Hola!    ", end="")
print("Como estas?")

#Tambien se puede utilizar para imprimir variables, tanto numericas como cadenas y listas
txt = "Hola!"
numero = 10

print(txt)
print(numero)

#Se pueden imprimir resultados de funciones, ya sean de Python o creadas por el usuario

def saludo():
    return "Hola!"

print(saludo())

nombre = "Rei Hino"

print(len(nombre))
