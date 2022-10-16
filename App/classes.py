import Utilities.dice as dice
# A class that is used to create character classes
class Classes:
    def __init__(self, name: str, hd: dice.Dice, st: list, skills: list, nbskills: int):
        self.name = name # Name of the class
        self.hd = hd # Hit dice
        self.st = st # Skills which have saving throws
        self.skills = skills # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills # Number of those skills that the plyer can choose

fighter = Classes("Fighter", dice.d10, ["Strength", "Constitution"], ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception"], 2)