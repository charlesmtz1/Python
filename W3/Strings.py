#Las cadenas se pueden imprimir directamente.
#Las cadenas pueden ser de comillas dobles o comillas simples.
#Se pueden almacenar en variables.

print("Hello World!")
print('Hello World!')

cadena = "Intel"
print(cadena)

#<-------------------------------------------------------------------------------------------------------------->
#Las comillas triples sirven para almacenas en una variable cadenas multilinea. Tambien se pueden usar triples comillas simples
#""" Multilinea """
#''' Multilinea '''

multilinea = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#Al momento de imprimir una multilinea, se mostrara en pantalla tal cual fue asignada a la variable, eso incluye renglones
#y espaciados.
print(multilinea)

#<-------------------------------------------------------------------------------------------------------------->
#Las cadenas tambien se pueden considerar arreglos. Se pueden tomar los caracteres de ciertas posiciones,
#o de un rango establecido 

cadena = "Intel"

print(cadena[2])
#El rango inicia desde el primer numero especificado hasta el ultimo definido menos uno.
#En este ejemplo, se van a tomar los caracteres desde la posicion 1 hasta la 3, es decir, "nte".
print(cadena[1:4]) 

#<-------------------------------------------------------------------------------------------------------------->
#Funciones para arreglos.
cadena = " Intel "

print(cadena.strip()) #strip() elimina espacios en blanco al principio y final de una cadena.

print(len(cadena)) #len() cuenta el tamañodeuna cadena.

print(cadena.lower()) #lower() cambia una cadena a minusculas.

print(cadena.upper()) #upper() cambia una cadena a mayusculas.

print(cadena.replace("I", "O")) #replace() Remplaza los caracteres de una cadena en base a lo especificado en la funcion.

print(cadena.split("t")) #split() Separa una cadena a partir de una referencia, generando un arreglo con los elementos separados.

#<-------------------------------------------------------------------------------------------------------------->
#Funcion format()

#Permite insertar en una cadena los valores numericos de una o varias variables.
#Se utiliza las llaves {} para indicar que se inserata en esa posicion una variable numerica.
edad = 26
txt = "Rei tiene {} años" #Se colocan las llaves en la cadena

#Se realiza la impresion de la cadena. Con la funcion format() se especifica que variable numerica 
# se colocara en el area de las llaves {}
print(txt.format(edad))

#Declaracion de multiples variables para uso de funcion format()
dolar = 19.50
euro = 22.25
yen = 0.17

#Se realiza la impresion de la cadena. Con la funcion format() se especifica de acuerdo al orden con que se colocaron las 
# variables, como se imprimiran las variables en el area de las llaves {}
txt = "Hoy el dolar se cotiza en ${}, el euro en {}€ y el yen en {}¥"
print(txt.format(dolar,euro,yen))

#Tambien se puede especificar que variable se va imprimir dentro de las llaves. Al momento de hacer referencia dentro de la
#funcion format() de las variables, cada una se tomara como elemento de un arreglo. 
txt = "El yen vale {2}¥, y es mas barato que el dolar, que vale ${0}"
print(txt.format(dolar,euro,yen))
