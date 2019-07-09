#Ejercicio 10
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimiento(lista):
    
    contador = 0

    for x in lista:
        while x > contador:
            print('*',end="")
            contador += 1
        print("")
        contador = 0
        

histograma = list((5,2,10))

procedimiento(histograma)

