import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Monk(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Monk"
        self.hd = dices.d8
        self.st = [
            "Strength",
            "Dexterity",
        ]
        self.skills = [
            "Acrobatics",
            "Athletics",
            "History",
            "Insight",
            "Religion",
            "Stealth",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Shortsword"), ["Simple", "Weapon"]],
            ["Dungeoneer's Pack", "Explorers Pack"],
            ((10, "Dart"), ),
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
