import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills

# This class is used to create a DnD character from a template


class Character:
    def __init__(self,
                 name: str,
                 race: Races.Race,
                 chr_class: Classes.Class,
                 level: int = 0,
                 inventory: list = [],
                 strength: Abilities.Strength = Abilities.Strength(),
                 wisdom: Abilities.Wisdom = Abilities.Wisdom(),
                 charisma: Abilities.Charisma = Abilities.Charisma(),
                 dexterity: Abilities.Dexterity = Abilities.Dexterity(),
                 intelligence: Abilities.Intelligence = Abilities.Intelligence(),
                 constitution: Abilities.Constitution = Abilities.Constitution(),
                 athletics: Skills.Athletics = Skills.Athletics(),
                 acrobatics: Skills.Acrobatics = Skills.Acrobatics(),
                 sleight_of_hand: Skills.Sleight_of_Hand = Skills.Sleight_of_Hand(),
                 stealth: Skills.Stealth = Skills.Stealth(),
                 arcana: Skills.Arcana = Skills.Arcana(),
                 history: Skills.History = Skills.History(),
                 investigation: Skills.Investigation = Skills.Investigation(),
                 nature: Skills.Nature = Skills.Nature(),
                 religion: Skills.Religion = Skills.Religion(),
                 animal_handling: Skills.Animal_Handling = Skills.Animal_Handling(),
                 insight: Skills.Insight = Skills.Insight(),
                 medicine: Skills.Medicine = Skills.Medicine(),
                 perception: Skills.Perception = Skills.Perception(),
                 survival: Skills.Survival = Skills.Survival(),
                 deception: Skills.Deception = Skills.Deception(),
                 intimidation: Skills.Intimidation = Skills.Intimidation(),
                 performance: Skills.Performance = Skills.Performance(),
                 persuasion: Skills.Persuasion = Skills.Persuasion(),
                 ):

        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = level
        self.inventory = inventory

        #  Calculates the abilities using the standard method
        self.strength = strength  # Physical power
        self.wisdom = wisdom  # Perception and Insight
        self.charisma = charisma  # Personnality strength
        self.dexterity = dexterity  # Agility
        self.intelligence = intelligence  # Reasoning and Memory
        self.constitution = constitution  # Endurance

        # Calculates default armor class
        # AC = 10 + dexterity
        self.ac = 10 + self.dexterity.modifier

        # Calculates skills
        # Strength dependants
        self.athletics = athletics
        # Dexterity dependants
        self.acrobatics = acrobatics
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth
        # Intelligence dependants
        self.arcana = arcana
        self.history = history
        self.investigation = investigation
        self.nature = nature
        self.religion = religion
        # Wisdom dependants
        self.animal_handling = animal_handling
        self.insight = insight
        self.medicine = medicine
        self.perception = perception
        self.survival = survival
        # Charisma dependants
        self.deception = deception
        self.intimidation = intimidation
        self.performance = performance
        self.persuasion = persuasion

        # TODO Incorporate saving throws
        # TODO Add movement speed
        # TODO Add inspiration
        # TODO Add proficiency bonus

        self.saved_data = [self.name,
                           self.race.data,
                           self.chr_class.name,
                           self.level,
                           self.inventory,
                           self.strength.value,
                           self.wisdom.value,
                           self.charisma.value,
                           self.dexterity.value,
                           self.intelligence.value,
                           self.constitution.value,
                           self.ac,
                           self.athletics.value,
                           self.acrobatics.value,
                           self.sleight_of_hand.value,
                           self.stealth.value,
                           self.arcana.value,
                           self.history.value,
                           self.investigation.value,
                           self.nature.value,
                           self.religion.value,
                           self.animal_handling.value,
                           self.insight.value,
                           self.medicine.value,
                           self.perception.value,
                           self.survival.value,
                           self.deception.value,
                           self.intimidation.value,
                           self.performance.value,
                           self.persuasion.value]
        self.saved_data = [str(element) for element in self.saved_data]

    def save(self):
        # Adds a new line between every element for saving
        formated_saved_data = ["\n"] * (len(self.saved_data) * 2 - 1)
        formated_saved_data[0::2] = self.saved_data
        file_name = self.name+".txt"
        with open(file_name, "w") as file:
            file.writelines(formated_saved_data)


def character_loader(file_path):
    with open(file_path, "r")as file:
        raw_data = file.read()
    raw_data = raw_data.split("\n")
    typed_data = []
    for element in raw_data:
        if isinstance(element, str):
            try:
                element = int(element)
            except ValueError:
                pass
        if isinstance(element, str):
            try:
                element = eval(element)
            except NameError:
                pass
        typed_data.append(element)
    name = typed_data[0]
    race = typed_data[1]
    chr_class = typed_data[2]
    level = typed_data[3]
    inventory = typed_data[4]
    strength = typed_data[5]
    wisdom = typed_data[6]
    charisma = typed_data[7]
    dexterity = typed_data[8]
    intelligence = typed_data[9]
    constitution = typed_data[10]
    athletics = typed_data[11]
    acrobatics = typed_data[12]
    sleight_of_hand = typed_data[13]
    stealth = typed_data[14]
    arcana = typed_data[15]
    history = typed_data[16]
    investigation = typed_data[17]
    nature = typed_data[18]
    religion = typed_data[19]
    animal_handling = typed_data[20]
    insight = typed_data[21]
    medicine = typed_data[22]
    perception = typed_data[23]
    survival = typed_data[24]
    deception = typed_data[25]
    intimidation = typed_data[26]
    performance = typed_data[27]
    persuasion = typed_data[28]
    character = Character(name,
                          race,
                          chr_class,
                          level,
                          inventory,
                          strength,
                          wisdom,
                          charisma,
                          dexterity,
                          intelligence,
                          constitution,
                          athletics,
                          acrobatics,
                          sleight_of_hand,
                          stealth, arcana,
                          history,
                          investigation,
                          nature,
                          religion,
                          animal_handling,
                          insight, medicine,
                          perception,
                          survival,
                          deception,
                          intimidation,
                          performance,
                          persuasion, )
    return character
