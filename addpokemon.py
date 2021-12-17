"""Add or edit a Pokémon in the master list.
"""

import json

def main():
    """I hope this script works.
    """
    dex = {}
    with open("data/dex.json", "rt") as fp:
        data = json.load(fp)
        for (dex_number, value) in data.items():
            try:
                int(dex_number)
            except ValueError:
                break
            entry = {
                "id": int(dex_number),
                "type": value["Types"],
                "health": value["BaseStats"]["HP"],
                "attack": value["BaseStats"]["Attack"],
                "defense": value["BaseStats"]["Defense"],
                "specialAttack": value["BaseStats"]["SpecialAttack"],
                "specialDefense": value["BaseStats"]["SpecialDefense"],
                "speed": value["BaseStats"]["Speed"],
            }
            if value["BreedingData"]["HasGender"]:
                entry["gender_ratio"] = value["BreedingData"]["FemaleChance"]
                pass
            abilities = {
                'basic': [],
                'advanced': [],
                'high': None,
            }
            for ability in value["Abilities"]:
                ability_type = ability["Type"]
                if ability_type == "Basic":
                    abilities['basic'] += ability["Name"]
                elif ability_type == "Advanced":
                    abilities["advanced"] += ability["Name"]
                elif ability_type == "High":
                    abilities["high"] = ability["Name"]
                else:
                    raise ValueError(
                        "Do not recognize {0}".format(ability_type))
            moves = {
                # A map of move name to level learned
                'level': {},
                # A list of Egg Moves.
                'egg': [],
                # A list of moves learned by TMs/HMs.
                'machine': [],
                # A list of Tutor moves. This is a dict because it
                # turns out that there is a special case for certain
                # moves that we should track.
                'tutor': {}
            }
            for move in value['LevelUpMoves']:
                name = move["Name"]
                level = move["LevelLearned"]
                moves['level'][name] = level
            for move in value["TmHmMoves"]:
                moves['machine'] += move['Name']
            for move in value['TutorMoves']:
                moves['tutor'][move['Name']] = move["Natural"]
            for move in value["EggMoves"]:
                moves['egg'] += move['Name']
            #
            species = value["Species"]
            dex[species] = entry
    print(dex["Bulbasaur"] or "Oh come on")

class InFormat(json.JSONDecoder):
    """The format of the file from which I am pulling data from.
    """
    pass

if __name__ == "__main__":
    main()
