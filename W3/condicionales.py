#Condicionales. 
#Debido a que Python no utiliza llaves para bloques de codigo, los bloques inician con :
#La identacion de codigo es el que marcara la pauta para definir un bloquede codigo.

#Utilizando condicionales multiples. Se utiliza elif para poner mas de una condicion.
x = 10
y = 8

if x < y:
    z = x + y
    print(z)
elif x == y:
    z = x * y
    print(z)
else:
    z = x - y
    print(z)


#Este tipo de condicional explica como utilizar and y or como sustitucion de && y ||
w = 10
x = 20
y = 20
z = 10

if w == z and x == y:
    print("Los numeros coinciden!")

if w == z or x > y:
    print("Al menos alguno coincidio.")


#Sentencia condicional sencilla
if x > y:
    print("Verdarero")
else:
    print("Falso")

#Tambien esta la posibilidad de realizar condicionales en una sola linea, siempre y cuando solo se vaya a incliur una sola linea de ejecucion por cada caso.
if x == 20: print("x vale 20") #Usando solo if

print("w vale 10") if w == 10 else print("w es diferente de 10") #Usando if/else

print("z vale 10") if z == 10 else print("z vale mas de 10") if z > 10 else print("z vale menos de 10") #Usando elif


