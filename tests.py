import App.abilities as Abilities
import App.characters as Characters
import App.skills as Skills
import App.races as Races
import App.classes as Classes
import App.characters as Characters
import App.Utilities.dice as Dice
import App.Utilities.score2modifier as Score2Modifier

Legolis = Characters.Character("Legolis", Races.human, Classes.fighter)
for attribute in dir(Legolis):
    if attribute[0] != "_":
        print(attribute, ":", Legolis.__getattribute__(attribute))