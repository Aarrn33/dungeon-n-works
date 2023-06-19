import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Rogue(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Rogue"
        self.hd = dices.d8
        self.st = [
            "Dexterity",
            "Intelligence",
        ]
        self.skills = [
            "Acrobatics",
            "Athletics",
            "Deception",
            "Insight",
            "Intimidation",
            "Investigation",
            "Perception",
            "Performance",
            "Persuasion",
            "Sleight of Hand",
            "Stealth",
        ]
        self.nbskills = 4
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Rapier"), (1, "Shortsword")],
            [(1, "Shortbow"), (1, "Shortsword")],
            ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"],
            ((1, "Leather Armor"), ),
            ((2, "Dagger"), ),
            ((1, "Thieve's Tools"), ),
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
