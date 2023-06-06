import App.Utilities.units as Units
import App.Utilities.dices as Dices
import App.abilities as Abilities
import App.skills as Skills
import sqlite3
import types


class Entity():
    def __init__(self,
                 name: str,
                 size: str,
                 type: str,
                 alignment: str,
                 hp_str: str,
                 senses: dict[str, Units.Distance],
                 exp: int,
                 strength: int,
                 wisdom: int,
                 charisma: int,
                 dexterity: int,
                 intelligence: int,
                 constitution: int,
                 ac: int = -1,
                 speed: Units.Distance = Units.Distance(30, "ft"),
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
                 vulnerabilities: list[str] = [],
                 resistances: list[str] = [],
                 immunities: list[str] = [],
                 languages: list[str] = [],
                 actions: dict[str] = {},
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

        alignment_list = ["Lawful Good", "Lawful Neutral", "Lawful Evil",
                          "Neutral Good", "True Neutral", "Neutral Evil",
                          "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        assert alignment in alignment_list, f"The only authorized alignments are {alignment_list.join(', ')}"
        self.alignment = alignment

        self.hp = Dices.str2dice_roll(hp_str)

        senses = eval(senses)
        for key, value in senses.items():
            distance, unit = value
            senses[key] = Units.Distance(int(distance), unit)
        self.senses = senses

        self.exp = exp
        self.challenge = self.exp2challenge()

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

        distance, unit = eval(speed)
        speed = Units.Distance(int(distance), unit)
        self.speed = speed

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
        self.vulnerabilities = eval(vulnerabilities)
        self.resistances = eval(resistances)
        self.immunities = eval(immunities)

        self.languages = eval(languages)

        # TODO Make actions work
        self.actions = eval(actions)

        # TODO Add drops

    def save(self):
        # Generates all of the data to be saved
        self.saved_data = []
        for elem in dir(self):
            obj = getattr(self, elem)
            if elem[0] != "_" and not isinstance(obj, (types.FunctionType, types.MethodType)) and elem not in ["challenge", "saved_data", "hp"]:
                if isinstance(obj, (Skills.Skill, Abilities.Ability)):
                    self.saved_data.append(getattr(obj, "value"))

                elif elem in ["senses"]:
                    formated_pairs = {}
                    for key, object in obj.items():
                        formated_pairs[key] = [object.value, object.unit]
                    self.saved_data.append(str(formated_pairs))

                elif isinstance(obj, Units.Unit):
                    self.saved_data.append(str([obj.value, obj.unit]))

                elif isinstance(obj, list):
                    self.saved_data.append(str(obj))

                else:
                    self.saved_data.append(obj)

        self.saved_data = tuple(self.saved_data)

        conn = sqlite3.connect(r'App\\Entities\\entities.db')
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO entities VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            self.saved_data)
        conn.commit()
        conn.close()

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
            if self.exp <= bound:
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


def load(entity_name):
    conn = sqlite3.connect(r'App\\Entities\\entities.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM entities WHERE name LIKE "%{entity_name}%" """)
    data = cursor.fetchall()
    cursor.execute("PRAGMA table_info(entities)")
    raw_columns = cursor.fetchall()
    conn.close()
    columns = []
    for column_data in raw_columns:
        columns.append(column_data[1])
    assert len(data) == 1, f"""Your query return more than one items or no 
    items at all, it returned {data}"""
    data_dict = {}
    for index, value in enumerate(data[0]):
        data_dict[columns[index]] = value
    return Entity(**data_dict)
