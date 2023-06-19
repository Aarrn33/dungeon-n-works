import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Sorcerer(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Sorcerer"
        self.hd = dices.d6
        self.st = [
            "Constitution",
            "Charisma",]
        self.skills = [
            "Arcana",
            "Deception",
            "Insight"
            "Intimidation",
            "Persuasion",
            "Religion",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Light Crossbow"), ["Simple", "Weapon"]],
            [(1, "Component's Pouch"), (1, "Arcane Focus")],
            ["Dungeoneer's Pack", "Explorer's Pack"], 
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
