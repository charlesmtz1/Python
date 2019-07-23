#Try/except permite realizar validaciones y permite ejecutar codigo en respuesta a que ocurra algun error o excepcion dentro del codigo.

while True:
    try:
        number = int(input("Escribe un numero: "))
        break
    except ValueError:
        print("Solo se admiten numeros!")

print(number)


#Try/except puede incluir cualquier cantidad de excepciones dependiendo la cantidad de errores que puedan ocurrir dentro de un bloque de codigo
while True:
    try:
        number = int(input("Escribe un numero: "))
        result = 100 / number
        break
    except ValueError:
        print("Solo se admiten numeros!")
    except ZeroDivisionError:
        print("No se puede dividir entre cero!!")

print(result)

#La instruccion ELSE permite ejecutar un nuevo bloque de codigo siempre y cuando el bloque dentro de TRY no cuenta con algun error.
try:
    x = 2
    number = x
except NameError:
    print("x es una variable que no existe!")
else:
    print("Todo esta en orden :)")

#FINALLY se ejecuta sin importar si ocurrio un error o el bloque de codigo esta correcto.
try:
    number = y
except NameError:
    print("Y no esta declarada")
else:
    print("Todo en orden :)")
finally:
    print("continua ejecucion normal....")
