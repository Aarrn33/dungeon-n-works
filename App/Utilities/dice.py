import random


# A function that is used to roll dices
# For instance a 3d2+5 would be writtent roll(2, nb=3, modifier=5)
def roll(size, nb=1, modifier=0):
    res = []
    for i in range(nb):
        res.append(random.randint(1, size))
    return sum(res)+modifier