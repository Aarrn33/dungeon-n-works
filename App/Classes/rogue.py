import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Rogue(Classes.Class):
    def __init__(self, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = "Rogue"
        self.hd = dices.d8
        self.st = ["Dexterity", "Intelligence"]
        self.skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
                       "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
        self.nbskills = 4
        self.chosen_skills = chosen_skills[:]
        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)

        del chosen_skills
