import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Barbarian(Classes.Class):
    def __init__(
            self,
            chosen_skills: list = [],
            ask_starting_equipment: bool = True,
    ):
        self.name = "Barbarian"
        self.hd = dices.d12
        self.st = [
            "Strength",
            "Constitution",
        ]
        self.skills = [
            "Animal Handling",
            "Athletics",
            "Intimidation",
            "Nature",
            "Perception",
            "Survival",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Greataxe"), ["Martial", "Melee", "Weapon"]],
            [(2, "Handaxe"), ["Simple", "Weapon"]],
            ("Explorer's Pack", ),
            ((4, "Javelin"), ),
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
