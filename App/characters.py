import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills
import App.Utilities.units as Units
import App.items as Items
from App.Utilities.find import find_class
from types import FunctionType, MethodType
import sqlite3

# This class is used to create a DnD character from a template


class Character:
    def __init__(self,
                 name: str,
                 race: (Races.Race | list),
                 chr_class: (Classes.Class | list),
                 exp: int = 0,
                 inventory: list[str] = [],
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
                 hp: int = -1,
                 ):

        # Assigns main identifiers
        self.name = name

        if isinstance(race, str):
            self.race = Races.find_race(eval(race))
        elif isinstance(race, Races.Race):
            self.race = race
        else:
            assert f"One shall never come here, pb in race init, input: {race}"

        if isinstance(chr_class, str):
            self.chr_class = find_class(eval(chr_class))
        elif isinstance(chr_class, Classes.Class):
            self.chr_class = chr_class
        else:
            assert f"One shall never come here, pb in class init, input: {chr_class}"

        self.exp = exp
        self.level = self.exp2level()

        if self.level <= 4:
            self.proficiency_bonus = 2
        elif self.level <= 8:
            self.proficiency_bonus = 3
        elif self.level <= 12:
            self.proficiency_bonus = 4
        elif self.level <= 16:
            self.proficiency_bonus = 5
        else:
            self.proficiency_bonus = 6

        if not isinstance(speed, Units.Unit):
            speed = Units.Distance(speed, "ft")
        self.speed = speed

        #  Calculates the abilities using the standard method
        self.strength = Abilities.Strength(strength)  # Physical power
        self.wisdom = Abilities.Wisdom(wisdom)  # Perception and Insight
        self.charisma = Abilities.Charisma(charisma)  # Personnality strength
        self.dexterity = Abilities.Dexterity(dexterity)  # Agility
        self.intelligence = Abilities.Intelligence(
            intelligence)  # Reasoning and Memory
        self.constitution = Abilities.Constitution(constitution)  # Endurance

        # Calculates default armor class
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

        for skill in self.chr_class.chosen_skills:
            formatted_skill = skill.lower()
            formatted_skill = formatted_skill.replace(" ", "_")
            getattr(self, formatted_skill).modify_value(1)

        # TODO Update stats depending on inventory content
        # TODO Add actions coming from inventory
        self.inventory = {}
        for item in eval(inventory):
            item_obj = Items.find(item[1])
            self.inventory[item_obj.name] = (item[0], item_obj)

        # TODO Add alternate system for races such as Bugbears, Centaurs or Goliaths (2*normal carrying capacity)
        self.encumbrance = "Unencumbered"
        inventory_weight = sum(
            [item[1].weight.value for item in self.inventory.values()])
        if inventory_weight > 5*self.strength.value and inventory_weight <= 10*self.strength.value:
            self.speed.value = self.speed.value-10
            self.encumbrance = "Encumbered"
        elif inventory_weight > 10*self.strength.value and inventory_weight <= 15*self.strength.value:
            self.speed.value = self.speed.value-20
            # TODO Implement disadvantages ability checks, attack rolls and STr, Dex and Con saving throws
            self.encumbrance = "Heavily encumbered"
        else:
            self.speed.value = 0
            self.encumbrance = "Overencumbered"
            print("You are unable to move because you are overencumbered")

        self.hp = hp
        if self.hp <= 0:
            self.hp = self.chr_class.hd.roll()

        # TODO Add a way to update stats (maybe through dedicated functions?)
        # TODO Incorporate saving throws
        # TODO Add inspiration
        # TODO Add proficiencies
        # TODO Add languages
        # TODO Add senses
        # TODO Add spells

    def save(self):
        # Generates all of the data to be saved
        self.saved_data = []
        not_to_save = ["saved_data", "ac", "level",
                       "encumbrance", "proficiency_bonus"]
        for elem in dir(self):
            obj = getattr(self, elem)
            if elem[0] != "_" and not isinstance(obj, (FunctionType, MethodType)) and elem not in not_to_save:
                if isinstance(obj, (Skills.Skill, Abilities.Ability)):
                    self.saved_data.append(str(getattr(obj, "value")))

                elif isinstance(obj, (Classes.Class, Races.Race)):
                    self.saved_data.append(str(getattr(obj, "data")))

                elif isinstance(obj, Units.Unit):
                    self.saved_data.append(str(obj.value))

                elif elem == "inventory":
                    self.saved_data.append(
                        str([(item[0], item[1].name) for item in obj.values()]))

                else:
                    self.saved_data.append(str(obj))

        self.saved_data = tuple(self.saved_data)

        conn = sqlite3.connect(r'App\\Entities\\characters.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM characters WHERE name='{self.name}'")
        data = cursor.fetchall()
        # If the character already existed, delete the old save
        if data:
            cursor.execute(f"DELETE FROM characters WHERE name='{self.name}'")

        cursor.execute(
            f"""INSERT INTO characters VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            self.saved_data)
        conn.commit()
        conn.close()

    def exp2level(self) -> int:
        assert self.exp >= 0
        upper_level_bounds = [300, 900, 2700, 6500,
                              14000, 23000, 34000,
                              48000, 64000, 85000, 100000,
                              120000, 140000, 165000,
                              195000, 225000, 265000,
                              305000, 355000]
        for bound in upper_level_bounds:
            if self.exp < bound:
                return upper_level_bounds.index(bound) + 1
        if self.exp >= upper_level_bounds[-1]:
            return 20


def load(chr_name):
    conn = sqlite3.connect(r'App\\Entities\\characters.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM characters WHERE name LIKE "%{chr_name}%" """)
    data = cursor.fetchall()
    cursor.execute("PRAGMA table_info(characters)")
    raw_columns = cursor.fetchall()
    conn.close()
    assert len(data) == 1, f"""Your query return more than one items or no 
    items at all, it returned {[item[0] for item in data]}"""
    columns = []
    for column_data in raw_columns:
        columns.append(column_data[1])
    data_dict = {}
    for index, value in enumerate(data[0]):
        data_dict[columns[index]] = value
    return Character(**data_dict)
