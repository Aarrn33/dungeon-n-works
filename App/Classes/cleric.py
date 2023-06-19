import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Cleric(Classes.Class):
    def __init__(
        self,
        chosen_skills: list = [],
        ask_starting_equipment: bool = True,
    ):
        self.name = "Cleric"
        self.hd = dices.d8
        self.st = [
            "Wisdom",
            "Charisma",
        ]
        self.skills = [
            "History",
            "Insight",
            "Medicine",
            "Persuasion",
            "Religion",
        ]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]
        # TODO Add a way to check if the character is proficient before askin him to make choices (cleric and warhammer)
        # TODO Add a way to make a bundle choice (Crossbow + 20 bolts) -> Maybe using custom packs
        self.starting_equipment = [
            [(1, "Mace"), (1, "Warhammer")],
            [(1, "Scale Mail"), (1, "Leather Armor"), (1, "Chain Mail")],
            [(1, "Light Crossbow"), ["Simple", "Weapon"]],
            ["Priest's Pack", "Explorer's Pack"],
            ((1, "Shield"), ),
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
