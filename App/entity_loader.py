import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills

# This class is used to create a DnD character from a template


class Character:
    def __init__(self, name: str,
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

    def save(self):
        self.saved_data = [self.name,
                           self.race.data,
                           self.chr_class,
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

        file_name = self.name+".txt"
        with open(file_name, "w") as file:
            file.writelines(self.saved_data)
