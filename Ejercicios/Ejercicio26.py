#Ejercicio 26
#Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y posterior a ello 
#pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.

def catalogo():
    peliculas = {
        1 : ("Favoritos", 2.50, 0.50),
        2 : ("Nuevos", 3.00, 0.75),
        3 : ("Estrenos", 3.50, 1.00),
        4 : ("Super Estrenos", 4.00, 1.50)
    }

    return peliculas


def mostrar_catalogo():
    print("Categoria        Precio      Codigo      Recargo / Dia de Atraso")
    for item in catalogo():
        print(f"{catalogo()[item][0]} ....... {catalogo()[item][1]} ....... {item} ....... {catalogo()[item][2]}")


def calcula_pago(codigo, dias_de_atraso):
    precio = catalogo()[codigo][1]
    recargo_atraso = catalogo()[codigo][2]

    return precio + (recargo_atraso * dias_de_atraso)


mostrar_catalogo()

codigo = int(input("Introduzca el codigo de la categoria de la pelicula: "))
dias_de_atraso = int(input("Introduzca el numero de dias de atraso de la devolucion: "))

print(f"El total a pagar es de ${calcula_pago(codigo, dias_de_atraso)} dolares") 