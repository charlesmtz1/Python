#Ejercicio 6
#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    
    posicion = len(cadena) - 1

    while posicion >= 0:
        print("Caracter recibido:", cadena[posicion])
        posicion -= 1

    print("La cadena ha quedado invertida:", cadena)


cadena = "estoy probando"

inversa(cadena)

print("----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")