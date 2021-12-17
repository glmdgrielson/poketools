"""A set of tools to make typing less... annoying to deal with.
"""

import enum
import json

class Typing(enum.Enum):
    pass

DAMAGE_CHART = {}

with open("data/typing.json") as f:
    with json.load(f) as data:
        for typing in data:
            DAMAGE_CHART[typing] = data[typing]
