"""A means to automatically generate a Pokémon.
"""

import random
from random import randrange

# This is meant to be indexed twice to get a nature.
# In particular, they are ordered in such a way that
# the first index is the stat that goes up, and the
# second index is the stat that goes down.
# 0 is Health, 1 is Attack, 2 is Defense, 3 is Special Attack,
# 4 is Special Defense, and 5 is Speed.
NATURES = [
    # Boosts Health
    ["Composed", "Cuddly", "Distracted", "Decisive", "Patient"],
    # Boosts Attack
    ["Desperate", "Hardy", "Lonely", "Adamant", "Naughty", "Brave"],
    # Boosts Defense
    ["Stark", "Bold", "Docile", "Impish", "Lax", "Relaxed"],
    # Boosts Special Attack
    ["Curious", "Modest", "Mild", "Bashful", "Rash", "Quiet"],
    # Boosts Special Defense
    ["Dreamy", "Calm", "Gentle", "Careful", "Quirky", "Sassy"],
    # Boosts Speed
    ["Skittish", "Timid", "Hasty", "Jolly", "Naive", "Serious"]
]

def generate_nature():
    """Randomize a Pokémon's nature.

    A nature is a fancy name to refer to a randomized stat boost.
    In particular, every Pokémon gets one stat boosted and another stat
    reduced. And if you're particularly unlucky, this can in fact be
    the exact same stat, leaving you with no boost at all.

    Returns a tuple to be inserted into pokegen.NATURES for the
    user-facing name to be written in a character sheet, for example.
    """
    higher = randrange(0, 6)
    lower = randrange(0, 6)
    return (higher, lower)
