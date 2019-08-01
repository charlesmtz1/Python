#Python es un lenguaje que utiliza objetos en todo momento. Nosotros tambien podemos definir nuestros propios objetos para variables mas complejas.
#Se declara una clase de la siguiente manera:

class MyClass:
    x = 5   #Atributo

#Para crear un nuevo objeto a partir de la clase, se realiza la siguiente asignacion:
c1 = MyClass()

print(c1.x)    #Imprimimos el atributo que declaramos en la clase


#############################
#Todas las clases requieren de un constructor para ser inicializadas. Deben iniciar con el constructor __init__(self)

class Person:
    def __init__(self, nombre, edad):      #Declaracion de constructor mas atributos
        self.nombre = nombre
        self.edad = edad

p1 = Person("Carlos", 30)   #Se crea nuevo objeto proporcionando los atributos especificados en el constructor

print(p1.nombre)    #Se acceden a los atributos del objeto creado
print(p1.edad)
