import App.Utilities.dice as dice
# A class that is used to create character classes


class Class:
    def __init__(self, name: str, hd: dice.Dice, st: list, skills: list, nbskills: int):
        self.name = name  # Name of the class
        self.hd = hd  # Hit dice
        self.st = st  # Skills which have saving throws
        self.skills = skills  # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills  # Number of those skills that the plyer can choose
        # TODO add the ability for users to choose the skills they are proficient in
        # TODO add choosen proficiencies and potentially more
        self.data = [name]


class Fighter(Class):
    def __init__(self):
        self.name = "Fighter"
        self.hd = dice.d10
        self.st = ["Strength", "Constitution"]
        self.skills = ["Acrobatics", "Animal Handling", "Athletics",
                       "History", "Insight", "Intimidation", "Perception"]
        self.nbskills = 2
        super().__init__(self.name, self.hd, self.st, self.skills, self.nbskills)

# TODO Add Python classes for other DnD classes -> append find_class function


def find_class(class_data):
    if isinstance(class_data, str):
        class_data = [class_data]
    if class_data[0] == "Fighter":
        return Fighter()
