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
    cleaned = {}
    for pokedex in api_pokedexes:
        region = pokedex.get('region', None)
        if region is not None:
            region = region['name']
        id = pokedex['id']
        clean_pokedex = {
            'id': id,
            'name': pokedex['name'],
            'official_name': field_extractor(pokedex, 'name', 'names'),
            'region': region,
            'description': field_extractor(pokedex, 'description', 'descriptions'),
            'pokemon': []
        }
        cleaned[id] = clean_pokedex
    return cleaned


def clean_pokemon(api_pokemon):
    cleaned = {}
    for pokeman in api_pokemon:
        habitat = pokeman.get('habitat', None)
        if habitat is not None:
            habitat = habitat['name']
        id = pokeman['id']
        clean_pokeman = {
            'id': id,
            'name': field_extractor(pokeman, 'name', 'names'),
            'flavor_text': field_extractor(pokeman, 'flavor_text', 'flavor_text_entries'),
            'habitat': habitat,
            'color': pokeman['color']['name'],
            'shape': pokeman['shape']['name'],
            'pokedexes': [],
            'moves': []
        }
        cleaned[id] = clean_pokeman

    return cleaned


def clean_moves(api_moves):
    cleaned = {}
    for move in api_moves:
        damage_class    = move.get('damage_class', None)
        if damage_class is not None:
            damage_class = damage_class['name']
        id = move['id']
        power_points    = move.get('pp', None)
        power           = move.get('power', None)
        accuracy        = move.get('accuracy', None)
        clean_move = {
            'id': id,
            'name': field_extractor(move, 'name', 'names'),
            'flavor_text': field_extractor(move, 'flavor_text', 'flavor_text_entries'),
            'short_effect': move['effect_entries'][0]['short_effect'],
            'effect': move['effect_entries'][0]['effect'],
            'damage_class': damage_class,
            'power_points': power_points,
            'power': power,
            'accuracy': accuracy,
            'pokemon': []
        }
        cleaned[id] = clean_move

    return cleaned


def assoc_pokedexes_pokemon(
    pokedex_dict, pokemon_dict,  pokemon_api):
    
    pokedex_lookup = { pdex['name']: pdex['id'] 
        for pdex in pokedex_dict.values() }
    
    for pmon in pokemon_api:
        id = pmon['id']
        for entry in pmon['pokedex_numbers']:
            pdex_name = entry['pokedex']['name']
            num = pokedex_lookup[ pdex_name ]
            
            pokemon_list = pokedex_dict[num]['pokemon']
            pokedex_list = pokemon_dict[id]['pokedexes']

            pokemon_list.append(id)
            pokedex_list.append(num)
    
def main():
    data_files = sys.argv  

    pokedexes = {}
    pokemon = {}
    moves = {}

    print('READING POKEDEX JSON')
    with open(data_files[1]) as data:
        pokedex_api = json.load(data)
        pokedexes = clean_pokedexes(pokedex_api)

    print('READING POKEMON JSON')
    with open(data_files[2]) as data:
        pokemon_api = json.load(data)
        pokemon = clean_pokemon(pokemon_api)

    print('READING MOVE JSON')
    with open(data_files[3]) as data:
        move_api = json.load(data)
        moves = clean_moves(move_api)

    print('ASSOCIATING POKEDEXES AND POKEMON')
    with open(data_files[2]) as data:
        pokemon_api = json.load(data)
        assoc_pokedexes_pokemon( pokedexes, pokemon, pokemon_api )

    print('STARTING POKEDEX INSERTS')
    for pd in pokedexes.values():
        pokedex, errors = pokedex_schema.load(pd)
        #print(pokedex)
        #print(errors)
        try:
            db.session.add(pokedex)
            db.session.commit()
            print()
        except sqlalchemy.exc.SQLAlchemyError as e:
            print("Failed to insert pokedex data")
            return 1
    print('FINISHED POKEDEX INSERTS')

    print('STARTING POKEMON INSERTS')
    for po in pokemon.values():
        pokeman, errors = pokemon_schema.load(po)
        #print(pokeman)
        #print(errors)
        try:
            db.session.add(pokeman)
            db.session.commit()
            print()
        except sqlalchemy.exc.SQLAlchemyError as e:
            print("Failed to insert pokemon data")
            return 1
    print('FINISHED POKEMON INSERTS')

    print('STARTING MOVE INSERTS')
    for mv in moves.values():
        move, errors = move_schema.load(mv)
        #print(move)
        #print(errors)
        try:
            db.session.add(move)
            db.session.commit()
            print()
        except sqlalchemy.exc.SQLAlchemyError as e:
            print("Failed to insert move data")
            return 1
    print('FINISHED MOVE INSERTS')
    
    for pdex in pokedexes.values():
        print(pdex, end='\n\n')

    return 0

if __name__ == '__main__':
    return_code = main()
    sys.exit(return_code)
