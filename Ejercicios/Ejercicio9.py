#Ejercicio 9
#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(numero, caracter):
    return numero * caracter


repeticion = 5
caracter = 'x'

print(generar_n_caracteres(repeticion, caracter))
