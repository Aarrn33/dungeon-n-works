import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills
import types
from typeguard import typechecked

# This class is used to create a DnD character from a template


class Character:
    @typechecked
    def __init__(self,
                 name: str,
                 race: list,
                 chr_class: list,
                 exp: int = 0,
                 inventory: list = [],
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
        self.race = Races.find_race(race)
        self.chr_class = Classes.find_class(chr_class)
        self.exp = exp
        self.level = self.exp2level()
        self.inventory = inventory

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

        self.hp = hp
        if self.hp <= 0:
            self.hp = self.chr_class.hd.roll()

        # TODO Incorporate saving throws
        # TODO Add movement speed
        # TODO Add inspiration
        # TODO Add proficiency bonus

        self.update()

    def update(self):
        self.level = self.exp2level()
        self.ac = 10 + self.dexterity.modifier

    def save(self):
        # Generates all of the data to be saved
        self.saved_data = []
        for elem in dir(self):
            obj = getattr(self, elem)
            if elem[0] != "_" and not isinstance(obj, (types.FunctionType, types.MethodType)) and elem not in ["saved_data", "ac", "level"]:
                if isinstance(obj, (Skills.Skill, Abilities.Ability)):
                    data = str(elem) + ": " + str(getattr(obj, "value"))
                    self.saved_data.append(data)
                elif isinstance(obj, (Classes.Class, Races.Race)):
                    data = str(elem) + ": " + str(getattr(obj, "data"))
                    self.saved_data.append(data)
                else:
                    data = str(elem) + ": " + str(obj)
                    self.saved_data.append(data)

        # Adds a new line between every element for saving
        formated_saved_data = ["\n"] * (len(self.saved_data) * 2 - 1)
        formated_saved_data[0::2] = self.saved_data
        file_name = r'App\\Entities\\Characters\\' + self.name + ".txt"

        with open(file_name, "w") as file:
            file.writelines(formated_saved_data)

    def exp2level(self) -> int:
        assert self.exp >= 0
        upper_level_bounds = [300, 900, 2700, 6500,
                              14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]
        for bound in upper_level_bounds:
            if self.exp < bound:
                return upper_level_bounds.index(bound) + 1
        if self.exp > upper_level_bounds[-1]:
            return 20


def load(file_path):
    with open(file_path, "r")as file:
        raw_data = file.read()
    raw_data = raw_data.split("\n")
    raw_data = [elem.split(": ") for elem in raw_data]
    typed_data = []
    for element in raw_data:
        try:
            element[1] = int(element[1])
        except ValueError:
            pass
        if isinstance(element[1], str):
            try:
                element[1] = eval(element[1])
            except (SyntaxError, NameError):
                pass
        typed_data.append(element)
    data_dict = {key: value for key, value in typed_data}
    character = Character(**data_dict)
    return character
