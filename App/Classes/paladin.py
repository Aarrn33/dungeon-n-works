import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Paladin(Classes.Class):
    def __init__(self, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = "Paladin"
        self.hd = dices.d10
        self.st = ["Wisdom", "Charisma"]
        self.skills = ["Athletics", "Insight", "Intimidation",
                       "Medicine", "Persuasion", "Religion"]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)

        del chosen_skills
