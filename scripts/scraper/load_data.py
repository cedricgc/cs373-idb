# -*- coding: utf-8 -*-


import json
import sys

import sqlalchemy

from website import db
import website.api.models as models
import website.api.schemas as schemas


pokedex_schema = schemas.PokedexSchema()
pokemon_schema = schemas.PokemonSchema()
move_schema = schemas.MoveSchema()


def clean_pokedexes(api_pokedexes):
    cleaned = []
    for pokedex in api_pokedexes:
        region = pokedex.get('region', None)
        if region is not None:
            region = region['name']
        clean_pokedex = {
            'name': pokedex['name'],
            'official_name': [p['name'] for p in pokedex['names'] if p['language']['name'] == 'en'][0],
            'region': region,
            'description': [p['description'] for p in pokedex['descriptions'] if p['language']['name'] == 'en'][0]
        }

        cleaned.append(clean_pokedex)

    return cleaned


def main():
    data_files = sys.argv

    with open(data_files[1]) as data:
        pokedexes = json.load(data)
        cleaned = clean_pokedexes(pokedexes)
        for pd in cleaned:
            pokedex, errors = pokedex_schema.load(pd)
            print(pokedex)
            print(errors)
            try:
                db.session.add(pokedex)
                db.session.commit()
            except sqlalchemy.exc.SQLAlchemyError as e:
                print("Failed to insert pokedex data")
                return 1

    return 0


if __name__ == '__main__':
    return_code = main()
    sys.exit(return_code)
