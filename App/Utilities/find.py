from App.Classes.barbarian import Barbarian
from App.Classes.bard import Bard
from App.Classes.cleric import Cleric
from App.Classes.druid import Druid
from App.Classes.fighter import Fighter
from App.Classes.monk import Monk
from App.Classes.paladin import Paladin
from App.Classes.ranger import Ranger
from App.Classes.rogue import Rogue
from App.Classes.sorcerer import Sorcerer
from App.Classes.warlock import Warlock
from App.Classes.wizard import Wizard


def find_class(class_data):
    # Changes the string provided to a 1 item list to better treat it
    if isinstance(class_data, str):
        class_data = [class_data]
    # Checks for all classes
    if class_data[0] == "Barbarian":
        if len(class_data) > 1:
            return Barbarian(class_data[1])
        else:
            return Barbarian()
    elif class_data[0] == "Bard":
        if len(class_data) > 1:
            return Bard(class_data[1])
        else:
            return Bard()
    elif class_data[0] == "Cleric":
        if len(class_data) > 1:
            return Cleric(class_data[1])
        else:
            return Cleric()
    elif class_data[0] == "Druid":
        if len(class_data) > 1:
            return Druid(class_data[1])
        else:
            return Druid()
    elif class_data[0] == "Fighter":
        if len(class_data) > 1:
            return Fighter(class_data[1])
        else:
            return Fighter()
    elif class_data[0] == "Monk":
        if len(class_data) > 1:
            return Monk(class_data[1])
        else:
            return Monk()
    elif class_data[0] == "Paladin":
        if len(class_data) > 1:
            return Paladin(class_data[1])
        else:
            return Paladin()
    elif class_data[0] == "Ranger":
        if len(class_data) > 1:
            return Ranger(class_data[1])
        else:
            return Ranger()
    elif class_data[0] == "Rogue":
        if len(class_data) > 1:
            return Rogue(class_data[1])
        else:
            return Rogue()
    elif class_data[0] == "Sorcerer":
        if len(class_data) > 1:
            return Sorcerer(class_data[1])
        else:
            return Sorcerer()
    elif class_data[0] == "Warlock":
        if len(class_data) > 1:
            return Warlock(class_data[1])
        else:
            return Warlock()
    elif class_data[0] == "Wizard":
        if len(class_data) > 1:
            return Wizard(class_data[1])
        else:
            return Wizard()
    else:
        assert f"One should never reach this point unless the provided class is not valid. You provided this input: {class_data}"
