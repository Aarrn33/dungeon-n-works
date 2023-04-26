# dungeon-n-works

## Introduction

A framework for dungeon masters to help them in their adventures \
Early developement

## A way to create, save and then load a character in python

```python
import App.characters as Characters
import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills
Senku = Characters.Character("Senku Ishigami", Races.Human(), Classes.Fighter(), 4, ["Alchemist's Supplies", "Chain Mail", "Common Clothes", "38 Crossbow Bolts", "Heavy Crossbow", "2 Longswords", "Iron Pot", "Shield", "Shovel", "Bedroll", "Manticore Tail Spikes", "Mess Kit", "Potion of Healing", "Tinderbox", "Waterskin"], Abilities.Strength(11), Abilities.Wisdom(11), Abilities.Charisma(9), Abilities.Dexterity(15), Abilities.Intelligence(14), Abilities.Constitution(14), Skills.Athletics(11), Skills.Acrobatics(15), Skills.Sleight_of_Hand(15), Skills.Stealth(15), Skills.Arcana(14), Skills.History(14), Skills.Investigation(14), Skills.Nature(14), Skills.Religion(14), Skills.Animal_Handling(11), Skills.Insight(11), Skills.Medicine(12), Skills.Perception(11), Skills.Survival(12), Skills.Deception(9), Skills.Intimidation(9), Skills.Performance(9), Skills.Persuasion(9))
Senku.save()
NewSenku = Characters.load(r'App\\Entities\\Characters\\Senku Ishigami.txt')
```

\
A random quote by Evariste Galois (1811-1832) : Nitens lux, horrenda procella, tenebris æternis involuta
