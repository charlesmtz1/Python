#La herencia permite crear clases hijas a partir de clases padre, las cuales heredan todos sus metodos y atributos.
#Primero se requiere definir una clase padre
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

p1 = Person("Rei", "Hino")
p1.printname()


#Posteriormente se crea la clase que heredara los metodos y atributos del padre.
class Student(Person):
    pass

p1 = Student("Rei", "Hino")
p1.printname()


#Para agregar atributos al hijo junto con los atributos padre, se requerira utilizar el contructor __init__ en el hijo
#Con respecto a los metodos, no se requiere nada en especial.
class Student2(Person):
    def __init__(self, fname, lname, year):       #NOTA!! Si se declara el constructor en el hijo, este perdera los atributos heredados del padre...
        Person.__init__(self, fname, lname)     #...a menos que incluyamos en el constructor del hijo el constructor del padre.
        self.graduacionyear = year      #Despues del constructor del padre, podemos añadir los atributos del hijo.

    def graduacion(self):       #Los metodos del hijo no interfieren con los del padre y no se pierden.
        print(f"Hola, mi nombre es {self.fname} {self.lname} y me gradue en {self.graduacionyear}")     #Se puede acceder a los atributos tanto del hijo como del padre.


p1 = Student2("Rei", "Hino", 2013)
p1.graduacion()