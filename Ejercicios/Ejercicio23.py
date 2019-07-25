#Ejercicio 23
#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
#Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

def valida_rima(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        print("Riman!")
    elif palabra1[-2:] == palabra2[-2:]:
        print("Riman poco")
    else:
        print("No Riman")


palabra1 = input("Escribe una palabra: ")
palabra2 = input("Escribe otra palabra: ")

valida_rima(palabra1, palabra2)