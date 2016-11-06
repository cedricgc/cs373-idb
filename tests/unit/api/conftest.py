# -*- coding: utf-8 -*-


import pytest

import website.api.models as models


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
def pokedex_model(pokedex):
    return models.Pokedex(**pokedex)


@pytest.fixture
def pokemon_model(pokemon):
    return models.Pokemon(**pokemon)


@pytest.fixture
def move_model(move):
    return models.Move(**move)
