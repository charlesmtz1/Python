#Ejercicio 10
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def history_generation(number_list):
    history = ""

    for number in number_list:
        for char in range(number):
            history += "*"
        history += "\n"

    return history
        

print("-------------------------------")
print("-----------Histogram-----------")
print("-------------------------------\n")

number_list = list()

while True:
    try:
        for x in range(int(input("How many numbers you going to include in your history? > "))):
            while True:     
                try:
                    number_list.append(int(input(f"Set number {x + 1} > ")))
                    break
                except ValueError: 
                    print("Only set numbers!")
        break
    except ValueError:
        print("Only set numbers!")
    

print(f"\nHistory created:\n{history_generation(number_list)}")

print("----------------------------")
print("----------Finished----------")
print("----------------------------")