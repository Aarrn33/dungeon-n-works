# dungeon-n-works

## Introduction

A framework for dungeon masters to help them in their adventures \
Early developement \
All contributions are welcome

## A way to create, save and then load a character in python

```python
import App.characters as Characters
import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills
test_char = Characters.Character("Testing Character", ["Human"], ["Fighter"])
test_char.save()
new_test_char = Characters.load(r'App\\Entities\\Characters\\Testing Character.txt')
```

\
A random quote by Evariste Galois (1811-1832) : Nitens lux, horrenda procella, tenebris æternis involuta
