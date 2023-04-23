import App.characters as Characters
import App.races as Races
import App.classes as Classes

Legolis = Characters.Character("Legolis", Races.human, Classes.fighter)
# Shows every attribute of Legolis
for attribute in dir(Legolis):
    if attribute[0] != "_":
        print(attribute, ":", Legolis.__getattribute__(attribute))