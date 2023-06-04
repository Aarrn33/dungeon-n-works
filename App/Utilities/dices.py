import random


class Dice:
    def __init__(self, size: int) -> None:
        self.size = size

    # A function that is used to roll dices
    # For instance a 3d2+5 would be writtent roll(nb=3, modifier=5)
    def roll(self, nb: int = 1, modifier: int = 0) -> int:
        res = 0
        for i in range(nb):
            res += random.randint(1, self.size)
        return res+modifier


# Defines commonly used dices for easier calling
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)

# Formats the dice data to extract the number of faces


def str2dice_roll(string: str) -> int:
    nb_dices, dice_nb_faces = string.split("d")
    nb_dices = int(nb_dices)
    try:
        dice_nb_faces, modifier = dice_nb_faces.split("+")
        dice_nb_faces = int(dice_nb_faces)
        modifier = int(modifier)
    except IndexError:
        dice_nb_faces, modifier = dice_nb_faces.split("-")
        dice_nb_faces = int(dice_nb_faces)
        modifier = -int(modifier)

    return Dice(dice_nb_faces).roll(nb_dices, modifier)
