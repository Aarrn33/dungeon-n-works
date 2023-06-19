import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Ranger(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Ranger"
        self.hd = dices.d10
        self.st = [
            "Strength",
            "Dexterity",
        ]
        self.skills = [
            "Animal Handling",
            "Athletics",
            "Insight",
            "Investigation",
            "Nature",
            "Perception",
            "Stealth",
            "Survival",
        ]
        self.nbskills = 3
        self.chosen_skills = chosen_skills[:]
        self.starting_equipment = [
            [(1, "Scale Mail"), (1, "Leather Armor")],
            ((2, "Shortsword"), ["Simple", "Melee", "Weapon"]),
            ("Dungeoneer's Pack", "Explorer's Pack"),
            ((1, "Longbow"), ),
            ((1, "Quiver"), ),
            ((20, "Arrow"), ),
        ]

        super().__init__(
            self.name,
            self.hd,
            self.st,
            self.skills,
            self.nbskills,
            self.starting_equipment,
            self.chosen_skills,
            ask_starting_equipment,)

        del chosen_skills
