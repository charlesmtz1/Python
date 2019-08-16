#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = float(input("Escribe tu peso en kgs> "))
estatura = float(input("Escribe tu altura en cms> "))

imc = peso / ((estatura/100)**2)

print(f"Tu indice de masa corporal es {round(imc,2)}")
