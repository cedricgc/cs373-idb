# -*- coding: utf-8 -*-


import json

import pytest

import website.api.models as models
import website.api.schemas as schemas


@pytest.fixture
def pokedex():
    """Generic pokedex instance"""
    pokedex = {
        'id': 1,
        'name': 'kanto',
        'official_name': 'Original Kanto',
        'region': 'Kanto',
        'description': 'This is a list of Pokémon in the order dictated by the Kanto regional Pokédex'
    }

    return pokedex


@pytest.fixture
def null_pokedex():
    """Pokedex instance with null fields"""
    null_pokedex = {
        'name': None,
        'official_name': None,
        'region': None,
        'description': None
    }

    return null_pokedex


@pytest.fixture
def pokemon():
    """Generic pokemon instance"""
    pokemon = {
        'id': 1,
        'name': 'Bulbasaur',
        'flavor_text': 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.',
        'habitat': 'grassland',
        'color': 'green',
        'shape': 'quadruped'
    }

    return pokemon


@pytest.fixture
def null_pokemon():
    """Pokemon instance with null fields"""
    null_pokemon = {
        'name': None,
        'flavor_text': None,
        'habitat': None,
        'color': None,
        'shape': None
    }

    return null_pokemon


@pytest.fixture
def move():
    """Generic move instance"""
    move = {
        'id': 1,
        'name': 'Razor Wind',
        'flavor_text': 'A two-turn attack. Blades of wind hit opposing Pokémon on the second turn. Critical hits land more easily.',
        'short_effect': 'Requires a turn to charge before attacking.',
        'effect': 'Inflicts regular damage.  User\'s critical hit rate is one level higher when using this move.  User charges for one turn before attacking. This move cannot be selected by sleep talk.',
        'damage_class': 'special',
        'power_points': 10,
        'power': 80,
        'accuracy': 100,
    }

    return move


@pytest.fixture
def null_move():
    """Move instance with null fields"""
    null_move = {
        'name': None,
        'flavor_text': None,
        'short_effect': None,
        'effect': None,
        'damage_class': None,
        'power_points': None,
        'power': None,
        'accuracy': None,
    }

    return null_move


@pytest.fixture
def search():
    """Generic search query"""
    search = {
        'query': 'Pokemon'
    }

    return search


@pytest.fixture
def pokedex_schema():
    """schema for single pokedex"""
    return schemas.PokedexSchema()


@pytest.fixture
def pokemon_schema():
    """schema for single pokemon"""
    return schemas.PokemonSchema()


@pytest.fixture
def move_schema():
    """schema for single move"""
    return schemas.MoveSchema()


@pytest.fixture
def pokedex_json(pokedex):
    """JSON serialized pokedex"""
    pokedex_json = {
        'data': pokedex
    }

    return json.dumps(pokedex_json)


@pytest.fixture
def pokedex_json_updated(pokedex):
    """JSON serialized pokedex"""
    pokedex['name'] = 'Updated pokedex name'
    pokedex_json = {
        'data': pokedex
    }

    return json.dumps(pokedex_json)


@pytest.fixture
def pokemon_json(pokemon):
    """JSON serialized pokemon"""
    pokemon_json = {
        'data': pokemon
    }

    return json.dumps(pokemon_json)


@pytest.fixture
def pokemon_json_updated(pokemon):
    """JSON serialized pokemon"""
    pokemon['name'] = 'Updated pokemon name'
    pokemon_json = {
        'data': pokemon
    }

    return json.dumps(pokemon_json)


@pytest.fixture
def move_json(move):
    """JSON serialized move"""
    move_json = {
        'data': move
    }

    return json.dumps(move_json)


@pytest.fixture
def move_json_updated(move):
    """JSON serialized move"""
    move['name'] = 'Updated move name'
    move_json = {
        'data': move
    }

    return json.dumps(move_json)


@pytest.fixture
def search_single_query_json(search):
    """JSON serialized search query with only one term"""
    search['query'] = 'Bulbasaur'
    search_json = {
        'data': search
    }

    return json.dumps(search_json)


@pytest.fixture
def search_multi_and_json(search):
    """JSON serialized search query with and operator"""
    search['query'] = 'Regular wind'
    search_json = {
        'data': search
    }

    return json.dumps(search_json)


@pytest.fixture
def search_multi_or_json(search):
    """JSON serialized search query with or operator"""
    search['query'] = 'Bulbasaur or Kanto'
    search_json = {
        'data': search
    }

    return json.dumps(search_json)


@pytest.fixture
def search_empty_query_json(search):
    """JSON serialized search query with empty string"""
    search['query'] = ''
    search_json = {
        'data': search
    }

    return json.dumps(search_json)


@pytest.fixture
def search_null_query_json(search):
    """JSON serialized search query with null instead of string"""
    search['query'] = None
    search_json = {
        'data': search
    }

    return json.dumps(search_json)


@pytest.fixture
def pokedex_model(pokedex):
    """Generic SQLAlchemy Pokedex model"""
    return models.Pokedex(**pokedex)


@pytest.fixture
def pokemon_model(pokemon):
    """Generic SQLAlchemy Pokemon model"""
    return models.Pokemon(**pokemon)


@pytest.fixture
def move_model(move):
    """Generic SQLAlchemy Move model"""
    return models.Move(**move)


@pytest.fixture
def seeds(db, pokedex_model, pokemon_model, move_model):
    """Models available to be loaded in the database before test"""
    pokemon_model.pokemon = [pokemon_model]
    pokemon_model.moves = [move_model]

    db.session.begin_nested()
    db.session.add_all([pokedex_model, pokemon_model, move_model])
    db.session.commit()
    yield
    db.session.rollback()
