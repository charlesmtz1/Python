#Ejercicio 25
#Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente 
#no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número 
#entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente 
#recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento 
#determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el 
#programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.

#Ejercicio 25-A
#De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total a pagar, 
#como una factura. Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos 
#con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??

import random
from time import sleep

def productos():
    galeria = {
        1 : ["Camisa", 300.0],
        2 : ["Cinturon", 150.0],
        3 : ["Zapatos", 500.0],
        4 : ["Pantalon", 350.0],
        5 : ["Calcetines", 100.0],
        6 : ["Falda", 300.0],
        7 : ["Gorra", 150.0],
        8 : ["Sueter", 200.0],
        9 : ["Corbata", 150.0],
        10 : ["Chaqueta", 500.0]
    }
    
    return galeria


def calcula_total(codigo, unidades):
    return productos()[codigo][1] * unidades


def valida_total(cantidad_total):
    if cantidad_total >= 1000:
        print("Su gasto iguala o supera los $1000.00 y por tanto participa en la promocion.")
        return aplica_descuento(cantidad_total)
    else:
        return False


def aplica_descuento(cantidad_total):
    print("Girando la tombola...")
    sleep(5)

    tombola = {
        0 : "Bola Blanca",
        1 : "Bola Roja",
        2 : "Bola Azul",
        3 : "Bola Verde",
        4 : "Bola Amarilla"
    }

    print("""
            Color                   Descuento
        Bola Blanca                 No Tiene
        Bola Roja                10 de descuento
        Bola Azul                20 de descuento
        Bola Verde               25 de descuento
        Bola Amarilla            50 de descuento
    """)

    bola = random.randint(0,4)

    print(f"Aleatoriamente obtuvo una {tombola[bola]}\n")

    return calcula_descuento(cantidad_total, tombola, bola)


def calcula_descuento(cantidad_total, tombola, bola):
    if tombola[bola] == "Bola Blanca":
        print("Usted no ha obtenido ningun descuento :(")
        return cantidad_total
    elif tombola[bola] == "Bola Roja":
        print("Felicidades! Ha ganado un 10 por ciento de descuento!")
        return cantidad_total * .90
    elif tombola[bola] == "Bola Azul":
        print("Felicidades! Ha ganado un 20 por ciento de descuento!")
        return cantidad_total * .80
    elif tombola[bola] == "Bola Verde":
        print("Felicidades! Ha ganado un 25 por ciento de descuento!")
        return cantidad_total * .75
    elif tombola[bola] == "Bola Amarilla":
        print("Felicidades! Ha ganado un 50 por ciento de descuento!")
        return cantidad_total * .50


cantidad_total = 0
total_prendas = 0

while True:
    print("             El Pinguinito             ")
    for x in productos():
        print(f"{productos()[x][0]}  .............................. {x}")

    while True:
        codigo = int(input("\nIntroduzca el codigo del producto: "))
        print(f"Su precio es: ${productos()[codigo][1]}")

        unidades = int(input("\nIntroduzca el numero de unidades: "))
        cantidad_total += calcula_total(codigo, unidades)
        total_prendas += unidades

        if input("\nDesea seguir comprando?(s/n): ").lower() == 's':
            continue
        else:
            print(f"\n\nNumero de prendas: {total_prendas}")
            print(f"El total a pagar es de ${cantidad_total}\n\n")
            break
    
    promocion = valida_total(cantidad_total)

    if  promocion != False:
        print(f"\nSu nuevo total a pagar es: ${promocion}")
    else:
        print("\nSu compra no aplica para esta promocion :(")

    opcion = input("\nSi desea salir presione 1, o de lo contrario presione cualquier tecla: ")

    if opcion == '1':
        break
    else:
        cantidad_total = 0
        total_prendas = 0
        continue