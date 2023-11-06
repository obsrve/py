from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

kub = Die(20)
kub.roll_die()
kub.roll_die()
kub.roll_die()
kub.roll_die()
kub.roll_die()
