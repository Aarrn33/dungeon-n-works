import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Fighter(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Fighter"
        self.hd = dices.d10
        self.st = [
            "Strength",
            "Constitution",
        ]
        self.skills = [
            "Acrobatics",
            "Animal Handling",
            "Athletics",
            "History",
            "Insight",
            "Intimidation",
            "Perception",
            "Survival",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Chain Mail"), (1, "Leather armor")],
            (["Martial", "Weapon"], ),
            [(1, "Shield"),  ["Martial", "Weapon"]],
            [(1, "Light Crossbow"), (2, "Handaxe")],
            ["Dungeoneer's Pack", "Explorer's Pack"],
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
