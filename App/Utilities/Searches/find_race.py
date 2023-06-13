from App.races import *


def find_race(race_data: (str | list[str])):
    if isinstance(race_data, str):
        race_data = [race_data]

    if race_data[0] == "Dragonborn":
        return Dragonborn(race_data[1])
    elif race_data[0] == "Dwarf":
        return Dwarf()
    elif race_data[0] == "Elf":
        return Elf()
    elif race_data[0] == "Gnome":
        return Gnome()
    elif race_data[0] == "Half-Elf":
        return HalfElf()
    elif race_data[0] == "Halfin":
        return Halfin()
    elif race_data[0] == "Half-Orc":
        return HalfOrc()
    elif race_data[0] == "Human":
        print("Human")
        return Human()
    elif race_data[0] == "Tiefling":
        return Tiefling()
    else:
        assert f"This should never run unless your input: {race_data} is not a valid race for a DnD character"

    del race_data
