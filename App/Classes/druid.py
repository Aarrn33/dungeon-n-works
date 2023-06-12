import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Druid(Classes.Class):
    def __init__(self, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = "Druid"
        self.hd = dices.d8
        self.st = ["Intelligence", "Wisdom"]
        self.skills = ["Arcana", "Animal Handling", "Insight", "Medicine",
                       "Nature", "Perception", "Religion", "Survival"]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)

        del chosen_skills
