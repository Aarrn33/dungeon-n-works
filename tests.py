import App.entity_loader as Entities
import App.races as Races
import App.classes as Classes

Legolis = Entities.Character("Legolis", Races.human, Classes.fighter)
# Shows every attribute of Legolis
for attribute in dir(Legolis):
    if attribute[0] != "_":
        print(attribute, ":", Legolis.__getattribute__(attribute))
