import random

class Die:
    """A simple attempt to randomly roll a die"""
    
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        return random.randint(1, sides)
        
d6 = Die()
print(d6)
