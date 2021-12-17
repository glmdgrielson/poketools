"""Create a basic data structure for a Pokémon's stats.
"""

from pokegen import NATURES, generate_nature
import json

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
        pass

    def apply_damage(self, damage, typing, category):
        """Apply damage, for GMing purposes.
        """
        pass

