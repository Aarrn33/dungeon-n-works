# dungeon-n-works

## Introduction

A framework for dungeon masters to help them in their adventures \
Early developement \
All contributions are welcome

## Quick snippets of code

### Characters

#### Creating, saving and loading

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

### Entities

#### Creating, saving, loading

```python
import App.entities as Entities
import App.Utilities.units as Units
test_entity = Entities.Entity("Test entity", "Medium", "Humanoid", "True Neutral", 10, {"Darkvision": Units.Distance(60, "ft")}, 100, 16, 12, 16, 7, 11, 10)
test_entity.save()
new_test_entity = Entities.load("Test entity")
```

\
A random quote by Evariste Galois (1811-1832) : Nitens lux, horrenda procella, tenebris æternis involuta
