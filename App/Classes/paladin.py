import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Paladin(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Paladin"
        self.hd = dices.d10
        self.st = [
            "Wisdom",
            "Charisma",
        ]
        self.skills = [
            "Athletics",
            "Insight",
            "Intimidation",
            "Medicine",
            "Persuasion",
            "Religion",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            (["Martial", "Weapon"], ),
            [(1, "Shield"), ["Martial", "Weapon"]],
            [(5, "Javelin"), ["Simple", "Melee", "Weapon"]],
            ["Priest's Pack", "Explorer's Pack"],
            ((1, "Chain Mail"), ),
            ((1, "Holy Symbol"), ),
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
