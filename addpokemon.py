"""Add or edit a Pokémon in the master list.
"""

import json

def main():
    """I hope this script works.

    Note that this script does have one issue: branched evolutions.
    I simply figured that trying to work out the logic for these special
    cases wasn't worth it right now. So if this script is run, there
    will still be some manual input required, but nowhere near as much
    as without this script.

    It also leaves the Dex number for alternate forms blank, so that
    the program doesn't bork when it gets to a dex number that can't
    be turned into a string.
    """
    dex = {}
    with open("data/dex.json", "rt") as fp:
        data = json.load(fp)
        for (dex_number, value) in data.items():
            species = value["Species"]
            species_name = species # type: str
            dex_id = None
            try:
                int(dex_number)
            except ValueError:
                species_name = '{0} ({1})'.format(
                        species, value["Form"])
            else:
                dex_id = int(dex_number)
            entry = {
                "id": dex_id,
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
                moves['machine'].append(move['Name'])
            for move in value['TutorMoves']:
                moves['tutor'][move['Name']] = move["Natural"]
            for move in value["EggMoves"]:
                moves['egg'].append(move['Name'])
            entry["moves"] = moves
            # How do I want to do evolutions?
            evolutions = {}
            stage = 0
            cur_stage = 0
            stages = value["EvolutionStages"]
            for evolution in stages:
                if stage == cur_stage:
                    if evolution["Species"] != species:
                        cur_stage += 1
                else:
                    evolutions[evolution["Species"]] = evolution["Criteria"]
                stage += 1
            entry["stage"] = len(stages) - len(evolutions)
            if evolutions:
                entry["evolutions"] = evolutions
                entry["stages_left"] = len(evolutions)
            dex[species_name] = entry
    print(dex["Ivysaur"] or "Oh come on")
    with open('data/pokemon2.json', 'wt') as out:
        json.dump(dex, out, indent=4)

class InFormat(json.JSONDecoder):
    """The format of the file from which I am pulling data from.
    """
    pass

if __name__ == "__main__":
    main()
