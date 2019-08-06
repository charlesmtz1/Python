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

##############################
#Las clases contienen metodos, son acciones que puede realizar un objeto. Estos tienen comportamientos similares a las funciones cotidianas de Python.

#El parametro self se utiliza para hacer referencia al objeto activo que esta utilizando los atributos y/o metodos de la clase. Puede llevar cualquier nombre, pero
#la palabra self es la forma comun de hacer dicha referencia.

class Persona:
    def __init__(self, nombre):     #Recuerda iniciar constructor con atributos
        self.nombre = nombre

    def saludo(self):       #Definicion de un metodo. Hace llamado del atributo del objeto al que esta utilizando dicho metodo
        print(f"Hola, mi nombre es {self.nombre}")   


p1 = Persona("Carlos")

p1.saludo() #Se invoca metodo igual que una funcion.

#Se puede modificar el valor de los atributos de un objeto apuntando directamente hacia ellos:

p1.nombre = "Rei"

p1.saludo()

#Tambien se pueden borrar atributos con del

del p1.nombre

#Se pueden destruir objetos completamente

del p1
