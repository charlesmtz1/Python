import random

class Dice:
    def __init__(self):
        self.faces = (1, 2, 3, 4, 5, 6)

    def roll(self):
        return random.choice(self.faces), random.choice(self.faces)


dado = Dice()

print(dado.roll())