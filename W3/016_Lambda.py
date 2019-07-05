#Una Lambda es una funcion anonima pequeña
#Puede llevar varios argumentos, sin embargo es una funcion de una sola fila.

x = lambda a: a + 10

print(x(10))

#Lambda permite varios argumentos para usarse en una linea.

y = lambda a, b: a + b

print(y(5, 2))


#Las ventajas de Lambda es que permiten realizar funciones anonimas a partir de valores "desconocidos".

def doble(n):
    return lambda a : a * n

valor = doble(2)

print(valor(3))
