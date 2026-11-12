import random

class Die:
    def __init__(self, sides, value):
        self.sides = sides
        self.value = value

    def roll(self):
        self.value = random.randint(1, self.sides)

