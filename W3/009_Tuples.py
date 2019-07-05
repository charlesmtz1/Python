#Los tuples son colecciones de datos que es ordenada y no pueden ser modificados. se declaran entre parentesis.
mytuple = ("Dia", "Umi", "Yoshiko")
print(mytuple)

#Se pueden acceder a los elementos de un tuple
print(mytuple[0])

#LOS TUPLES NO SE PUEDEN MODIFICAR, por lo tanto no se puede realizar la siguiente sentencia:
# mytuple[1] = "Cebollita"

#Se puede recorrer un tuple completo con la instruccion FOR
for x in mytuple:
    print(x)

#Se puede validar si un elemento pertenece a un tuple
if "Dia" in mytuple:
    print(":)")

#La funcion len() permite mostrar el numero de elementos dentro de un tuple
print(len(mytuple))

#LOS TUPLES NO PERMITEN INSERCION DE NUEVOS ELEMENTOS. Estas instrucciones son incorrectas:
# mytuple.append("Ruby")
# mytuple.insert(2, "Ruby")

#LOS TUPLES TAMPOCO PUEDEN ELIMINAR ELEMENTOS
# mytuple.remove("Umi")
# mytuple.pop()
# del mytuple[2]
#Sin embargo, un tuple si puede ser eliminado completamente.

del mytuple


#LOS TUPLES NO PUEDEN SER COPIADOS CON COPY() Y LIST()

#Se puede utilizar el constructor TUPLE() para generar nuevos TUPLES desde una variable, o bien para realizar una copia de las mismas
primetuple = tuple(("Rei", "Dia", "Mizuki")) #INCLUYE DOBLES PARENTESIS!!!

primetuple2 = tuple(primetuple)

print(primetuple)
print(primetuple2)