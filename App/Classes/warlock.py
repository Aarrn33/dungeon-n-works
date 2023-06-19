import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Warlock(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Warlock"
        self.hd = dices.d8
        self.st = [
            "Wisdom",
            "Charisma",
        ]
        self.skills = [
            "Arcana",
            "Deception",
            "History",
            "Intimidation",
            "Investigation",
            "Nature",
            "Religion",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Light Crossbow"), ["Simple", "Weapon"]],
            [(1, "Component's Pouch"), (1, "Arcane Focus")],
            ["Scholar's Pack", "Dungeoneer's Pack"],
            ((1, "Leather Amor"), ),
            (["Simple", "Weapon"], ),
            ((2, "Dagger"), ),
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
