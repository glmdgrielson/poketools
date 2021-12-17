"""Create a basic data structure for a Pokémon's stats.
"""

from pokegen import NATURES, generate_nature
import json
import random

class MonsterData(object):
    """A simple thing to hold JSON data.
    """
    pass

class PocketMonster(object):
    """A Pokémon.
    """
    health = 1
    attack = 1
    defense = 1
    sp_attack = 1
    sp_defense = 1
    speed = 1
    gender = None # type: Union[str, None]
    # TODO: figure out what sort of data I should pass in.
    def __init__(self, species, level, *args):
        """Create a Pokémon.

        Arguments:
            species: What species this is. This is expecting a string,
            not a dex number.
            level: the current level of this Pokémon.
        """
        self.level = level
        with open('./pokemon.json', mode="rt") as f:
            with json.dump(f) as data:
                base = data[species]
                self.health = base["health"]
                self.attack = base["attack"]
                self.defense = base["defense"]
                self.sp_attack = base["sp_attack"]
                self.sp_defense = base["sp_defense"]
                self.speed = base["speed"]
                if base["gender_ratio"]:
                    gender = random.random()
                    if gender < base["gender_ratio"]:
                        self.gender = "female"
                    else:
                        self.gender = "male"
                self.movelist = self.generate_moves(base["moves"]["level"])
                self.ability = random.choice(base["abilities"]["basic"])

    def apply_damage(self, damage, typing, category):
        """Apply damage, for GMing purposes.
        """
        pass

    def generate_moves(self, moves, egg=None, machine=None, tutor=None):
        """Create a movelist for this Pokémon.

        Arguments:
            moves: a map of moves to levels. This should be as it appears in the
            rulebook *exactly* because this is going to be used later.
            egg: If egg moves are desired, pass in a list to be used.
        """
        moves = []
        for (move, level) in moves.items():
            if level <= self.level:
                moves += [move]
        if egg is not None:
            moves += egg
        if machine is not None:
            moves += machine
        if tutor is not None:
            moves += tutor
        return moves[0:4]
