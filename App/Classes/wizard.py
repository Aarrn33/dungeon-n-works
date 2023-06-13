import App.classes as Classes
import App.Utilities.dices as dices


class Wizard(Classes.Class):
    def __init__(self, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = "Wizard"
        self.hd = dices.d6
        self.st = [
            "Intelligence",
            "Wisdom",
        ]
        self.skills = [
            "Arcana",
            "History",
            "Insight",
            "Investigation",
            "Medicine",
            "Religion",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Quarterstaff"), (1, "Dagger")],
            [(1, "Component Pouch"), (1, "Arcane Focus")],
            ["Scholar's Pack", "Explorer's Pack"],
            ((1, "Spellbook"), ),
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
