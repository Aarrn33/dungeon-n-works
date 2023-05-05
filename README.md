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
Senku = Characters.Character("Senku Ishigami", ["Human"], ["Fighter"], 3578, ["Alchemist's Supplies", "Chain Mail", "Common Clothes", "38 Crossbow Bolts", "Heavy Crossbow", "2 Longswords", "Iron Pot", "Shield", "Shovel", "Bedroll", "Manticore Tail Spikes", "Mess Kit", "Potion of Healing", "Tinderbox", "Waterskin"], 11, 11, 9, 15, 14, 14, 11, 15, 15, 15, 14, 14, 14, 14, 14, 12, 11, 12, 11, 11, 9, 9, 9, 9)
Senku.save()
NewSenku = Characters.load(r'App\\Entities\\Characters\\Senku Ishigami.txt')
```

## A quick way to save a character

```python
import App.characters as Characters
import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills
Me = Characters.Character("Me", ["Human"], ["Fighter", ["Acrobatics", "Insight"]])
Me.save()
Me = Characters.load(r'App\\Entities\\Characters\\Me.txt')
```

\
A random quote by Evariste Galois (1811-1832) : Nitens lux, horrenda procella, tenebris æternis involuta
