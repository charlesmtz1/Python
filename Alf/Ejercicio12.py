#Ejercicio 12
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "ballenita"

user_password = input("Escribe la contraseña > ").lower()

if user_password == password:
    print("Contraseña correcta!")
else:
    print("Contraseña incorrecta...")
