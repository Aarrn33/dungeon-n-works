import random


class Dice:
    def __init__(self, size: int) -> None:
        self.size = size
    
    # A function that is used to roll dices
    # For instance a 3d2+5 would be writtent roll(2, nb=3, modifier=5)
    def roll(self, nb: int = 1, modifier: int = 0) -> int:
        res = []
        for i in range(nb):
            res.append(random.randint(1, self.size))
        return sum(res)+modifier
    

# Defines commonly used dices for easier calling
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)