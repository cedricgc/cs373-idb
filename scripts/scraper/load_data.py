# -*- coding: utf-8 -*-


import json
import os.path
import sys

import flask_sqlalchemy
import sqlalchemy

base_dir = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, base_dir)

from website import create_app
import website.api.models as models
import website.api.schemas as schemas


app = create_app()
db = flask_sqlalchemy.SQLAlchemy(app)

pokedex_schema = schemas.PokedexSchema()
pokemon_schema = schemas.PokemonSchema()
move_schema = schemas.MoveSchema()


def field_extractor(obj, field, field2):
    try:
        item = [p[field]
                for p in obj[field2] if p['language']['name'] == 'en'][0]
    except IndexError:
        return None

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
            'description': field_extractor(pokedex, 'description', 'descriptions')
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


def clean_moves(api_moves):
    cleaned = []
    for move in api_moves:
        damage_class = move.get('damage_class', None)
        if damage_class is not None:
            damage_class = damage_class['name']
        power_points = move.get('pp', None)
        power = move.get('power', None)
        accuracy = move.get('accuracy', None)
        clean_move = {
            'name': field_extractor(move, 'name', 'names'),
            'flavor_text': field_extractor(move, 'flavor_text', 'flavor_text_entries'),
            'short_effect': move['effect_entries'][0]['short_effect'],
            'effect': move['effect_entries'][0]['effect'],
            'damage_class': damage_class,
            'power_points': power_points,
            'power': power,
            'accuracy': accuracy
        }

        cleaned.append(clean_move)

    return cleaned


def main():
    data_files = sys.argv

    print('STARTING POKEDEX INSERTS')
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
    print('FINISHED POKEDEX INSERTS')

    print('STARTING POKEMON INSERTS')
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
    print('FINISHED POKEMON INSERTS')

    print('STARTING MOVE INSERTS')
    with open(data_files[3]) as data:
        moves = json.load(data)
        cleaned = clean_moves(moves)
        for mv in cleaned:
            print(mv)
            move, errors = move_schema.load(mv)
            print(move)
            print(errors)
            try:
                db.session.add(move)
                db.session.commit()
            except sqlalchemy.exc.SQLAlchemyError as e:
                print("Failed to insert move data")
                return 1
    print('FINISHED MOVE INSERTS')

    return 0


if __name__ == '__main__':
    return_code = main()
    sys.exit(return_code)
