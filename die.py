#Creating a die class that has 1 main function called roll_die() which rolls your time.

import random

#create class
class Die:
    def __init__(self, sides: int = 6):
        #initializes the sides, default is 6
        self.sides: int = sides

    def roll_die(self):
        #returns the number value of roll
        print(random.randint(1, self.sides))
    
