class Person:
    def __init__(self, nombre, wife):
        self.nombre = nombre
        self.wife = wife

    def talk(self):
        print(f"Hi, my name is {self.nombre} and my wife is {self.wife}")


person = Person("Carlos", "")
person.wife = "Rei"

person.talk()
