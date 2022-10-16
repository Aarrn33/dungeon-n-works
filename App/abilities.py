import Utilities.score2modifier as score2modifier
import Utilities.dice as dice

# A class that is used to define the abilities of a character
class Ability:
    def __init__(self, name: str):
        self.name = name
        self.value = dice.d6.roll(3)
        self.modifier = score2modifier.score2modifier(self.value)