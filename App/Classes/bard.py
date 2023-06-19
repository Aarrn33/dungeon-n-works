import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Bard(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Bard"
        self.hd = dices.d8
        self.st = [
            "Dexterity",
            "Charisma",
        ]
        self.skills = [
            "Acrobatics",
            "Animal Handling",
            "Arcana",
            "Athletics",
            "Deception",
            "History",
            "Insight",
            "Intimidation",
            "Investigation",
            "Medicine",
            "Nature",
            "Perception",
            "Performance",
            "Persuasion",
            "Religion",
            "Sleight of Hand",
            "Stealth",
            "Survival",
        ]
        self.nbskills = 3
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Rapier"), (1, "Longsword"), ["Simple", "Weapon"]],
            ["Diplomat's Pack", "Entertainer's Pack"],
            [(1, "Lute"), ["Musical Instrument"]],
            ((1, "Leather Armor"), ),
            ((1, "Dagger"), ),
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
