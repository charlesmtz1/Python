#Ejercicio 10
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimiento(lista):
    print("\nGeneracion de histograma:")
    for x in lista:
        for x in range(x):
            print('*',end="")
        print("")
        

print("------------------------------")
print("----------Histograma----------")
print("------------------------------\n")

histograma = list()

for x in range(int(input("Cuantos numeros se incluiran en el histograma?: "))):
    histograma.append(int(input("Escribe un numero: ")))

procedimiento(histograma)

print("\n----------------------------")
print("------Fin de ejecucion------")
print("----------------------------")