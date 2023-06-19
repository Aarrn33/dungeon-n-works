import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Druid(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Druid"
        self.hd = dices.d8
        self.st = [
            "Intelligence",
            "Wisdom",
        ]
        self.skills = [
            "Arcana",
            "Animal Handling",
            "Insight",
            "Medicine",
            "Nature",
            "Perception",
            "Religion",
            "Survival",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Wooden Shield"), ["Simple", "Weapon"]],
            [(1, "Scimitar"), ["Simple", "Melee", "Weapon"]],
            ((1, "Leather Armor"), ),
            ("Explorer's Pack", ),
            ((1, "Druidic Focus"), ), 
        ]

        super().__init__(
            self.name,
            self.hd,
            self.st,
            self.skills,
            self.nbskills,
            self.starting_equipment,
            self.chosen_skills,
            ask_starting_equipment,
        )

        del chosen_skills
