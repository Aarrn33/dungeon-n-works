import App.Utilities.units as Units
import App.abilities as Abilities
import App.skills as Skills
import sqlite3


class Entity():
    def __init__(self,
                 name: str,
                 size: str,
                 type: str,
                 aligmnement: str,
                 hp: int,
                 senses: dict[Units.Distance],
                 exp: int,
                 ac: int = -1,
                 speed: Units.Distance = Units.Distance(30, "ft"),
                 strength: int = -1,
                 wisdom: int = -1,
                 charisma: int = -1,
                 dexterity: int = -1,
                 intelligence: int = -1,
                 constitution: int = -1,
                 athletics: int = -1,
                 acrobatics: int = -1,
                 sleight_of_hand: int = -1,
                 stealth: int = -1,
                 arcana: int = -1,
                 history: int = -1,
                 investigation: int = -1,
                 nature: int = -1,
                 religion: int = -1,
                 animal_handling: int = -1,
                 insight: int = -1,
                 medicine: int = -1,
                 perception: int = -1,
                 survival: int = -1,
                 deception: int = -1,
                 intimidation: int = -1,
                 performance: int = -1,
                 persuasion: int = -1,
                 vulnerabilities: list = [],
                 resistances: list = [],
                 immunities: list = [],
                 languages: list[str] = [],
                 actions: list = [],
                 ):
        self.name = name

        auth_sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
        assert size in auth_sizes, f"The only authorized sizes are {auth_sizes.join(', ')}"
        self.size = size

        auth_types = ["Aberration", "Beast", "Celestial",
                      "Construct", "Dragon", "Elemental",
                      "Fey", "Fiend", "Giant", "Humanoid",
                      "Monstrosity", "Ooze", "Plant", "Undead"]
        assert type in auth_types, f"The only authorized siztypeses are {auth_types.join(', ')}"
        self.type = type

        aligmnment_list = ["Lawful Good", "Lawful Neutral", "Lawful Evil",
                           "Neutral Good", "True Neutral", "Neutral Evil",
                           "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        assert aligmnement in aligmnment_list, f"The only authorized alignments are {aligmnment_list.join(', ')}"
        self.aligmnement = aligmnement

        self.hp = hp
        self.senses = senses

        self.exp = exp
        self.challenge = self.exp2challenge()

        self.speed = speed

        self.strength = Abilities.Strength(strength)  # Physical power
        self.wisdom = Abilities.Wisdom(wisdom)  # Perception and Insight
        self.charisma = Abilities.Charisma(charisma)  # Personnality strength
        self.dexterity = Abilities.Dexterity(dexterity)  # Agility
        self.intelligence = Abilities.Intelligence(
            intelligence)  # Reasoning and Memory
        self.constitution = Abilities.Constitution(constitution)  # Endurance

        self.ac = ac
        if self.ac <= 0:
            # Calculates default armor class if none provided
            # AC = 10 + dexterity
            self.ac = 10 + self.dexterity.modifier

        # Calculates skills
        # Strength dependants
        self.athletics = Skills.Athletics(athletics, self.strength)
        # Dexterity dependants
        self.acrobatics = Skills.Acrobatics(acrobatics, self.dexterity)
        self.sleight_of_hand = Skills.Sleight_of_Hand(
            sleight_of_hand, self.dexterity)
        self.stealth = Skills.Stealth(stealth, self.dexterity)
        # Intelligence dependants
        self.arcana = Skills.Arcana(arcana, self.intelligence)
        self.history = Skills.History(history, self.intelligence)
        self.investigation = Skills.Investigation(
            investigation, self.intelligence)
        self.nature = Skills.Nature(nature, self.intelligence)
        self.religion = Skills.Religion(religion, self.intelligence)
        # Wisdom dependants
        self.animal_handling = Skills.Animal_Handling(
            animal_handling, self.wisdom)
        self.insight = Skills.Insight(insight, self.wisdom)
        self.medicine = Skills.Medicine(medicine, self.wisdom)
        self.perception = Skills.Perception(perception, self.wisdom)
        self.survival = Skills.Survival(survival, self.wisdom)
        # Charisma dependants
        self.deception = Skills.Deception(deception, self.charisma)
        self.intimidation = Skills.Intimidation(intimidation, self.charisma)
        self.performance = Skills.Performance(performance, self.charisma)
        self.persuasion = Skills.Persuasion(persuasion, self.charisma)

        # TODO Make the three following attributes work
        self.vulnerabilities = vulnerabilities
        self.resistances = resistances
        self.immunities = immunities

        self.languages = languages

        self.actions = actions

    def exp2challenge(self) -> float:
        assert self.exp >= 0
        upper_level_bounds = [10, 25, 50, 100, 200,
                              450, 700, 1100, 1800,
                              2300, 2900, 3900, 5000,
                              5900, 7200, 8400, 10000,
                              11500, 13000, 15000,
                              18000, 20000, 22000,
                              25000, 33000, 41000,
                              50000, 62000, 75000,
                              90000, 105000, 120000,
                              135000, 155000]
        for bound in upper_level_bounds:
            if self.exp < bound:
                if upper_level_bounds.index(bound) >= 4:
                    return upper_level_bounds.index(bound) - 3
                elif upper_level_bounds.index(bound) == 0:
                    return 0
                elif upper_level_bounds.index(bound) == 1:
                    return 0.125
                elif upper_level_bounds.index(bound) == 2:
                    return 0.25
                elif upper_level_bounds.index(bound) == 3:
                    return 0.5

        if self.exp > upper_level_bounds[-1]:
            return 30
