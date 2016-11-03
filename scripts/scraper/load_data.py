# -*- coding: utf-8 -*-


import json
import os.path
import sys

import sqlalchemy

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, base_dir)

from website import db
import website.api.models as models
import website.api.schemas as schemas


pokedex_schema = schemas.PokedexSchema()
pokemon_schema = schemas.PokemonSchema()
move_schema = schemas.MoveSchema()


def field_extractor(obj, field, field2):
    item = [p[field] for p in obj[field2] if p['language']['name'] == 'en'][0]

    return item


def clean_pokedexes(api_pokedexes):
    cleaned = []
    for pokedex in api_pokedexes:
        region = pokedex.get('region', None)
        if region is not None:
            region = region['name']
        clean_pokedex = {
            'name': pokedex['name'],
            'official_name': field_extractor(pokedex, 'name', 'names'),
            'region': region,
            'description': [p['description'] for p in pokedex['descriptions'] if p['language']['name'] == 'en'][0]
        }

        cleaned.append(clean_pokedex)

    return cleaned


def clean_pokemon(api_pokemon):
    cleaned = []
    for pokeman in api_pokemon:
        habitat = pokeman.get('habitat', None)
        if habitat is not None:
            habitat = habitat['name']
        clean_pokeman = {
            'name': field_extractor(pokeman, 'name', 'names'),
            'flavor_text': field_extractor(pokeman, 'flavor_text', 'flavor_text_entries'),
            'habitat': habitat,
            'color': pokeman['color']['name'],
            'shape': pokeman['shape']['name']
        }

        cleaned.append(clean_pokeman)

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

    with open(data_files[2]) as data:
        pokemon = json.load(data)
        cleaned = clean_pokemon(pokemon)
        for po in cleaned:
            pokeman, errors = pokemon_schema.load(po)
            print(pokeman)
            print(errors)
            try:
                db.session.add(pokeman)
                db.session.commit()
            except sqlalchemy.exc.SQLAlchemyError as e:
                print("Failed to insert pokemon data")
                return 1

    return 0


if __name__ == '__main__':
    return_code = main()
    sys.exit(return_code)
