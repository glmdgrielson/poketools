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
        with open('data/pokemon.json', mode="rt") as f:
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
                # This contains: a dict of moves to level learned, as
                # well as lists of egg moves, TMs and HMs, and tutor moves
                self.movelist = base["moves"]
                self.moves = self.generate_moves(base["moves"]["level"])
                self.ability = random.choice(base["abilities"]["basic"])
                if base["legendary"] is True:
                    self.legendary = True
                (higher, lower) = generate_nature()
                self.nature = NATURES[higher][lower]
                stats = [
                    self.health, self.attack, self.defense,
                    self.sp_attack, self.sp_defense, self.speed]
                if higher == 0:
                    self.health += 1
                else:
                    # TODO: Is there a less ugly way to do this?
                    stats.index(higher).__add__(2)
                if lower == 0:
                    self.health -= 1
                else:
                    stats.index(lower).__sub__(2)
                self.hit_points = level + 3 * self.health + 10

    def apply_damage(self, damage, typing, category):
        """Apply damage, for GMing purposes.
        """
        pass

    def generate_moves(self, egg=False, machine=False, tutor=False):
        """Create a movelist for this Pokémon.

        ``egg``, ``machine``, and ``tutor`` should be set to true
        to include egg moves, TMs and HMs, and tutor moves,
        respectively.

        Should return four randomly selected moves that can be
        learned in the scenarios provided.
        """
        moves = []
        learned_moves = []
        for (move, level) in self.movelist["level"].items():
            if level <= self.level:
                moves += [move]
        if egg:
            moves += self.movelist["egg"]
        if machine:
            learned_moves += self.movelist["machine"]
        if tutor:
            learned_moves += self.movelist["tutor"]
        if learned_moves:
            moves += random.sample(learned_moves, k=3)
        return random.sample(moves, k=6)
