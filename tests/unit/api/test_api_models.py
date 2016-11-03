# -*- coding: utf-8 -*-


import pytest

import website.api.models as models


@pytest.fixture
def pokedex():
    pokedex = {
        'id': 1,
        'name': 'kanto',
        'official_name': 'Original Kanto',
        'region': 'Kanto',
        'description': 'This is a list of Pokémon in the order dictated by the Kanto regional Pokédex'
    }

    return models.Pokedex(**pokedex)


@pytest.fixture
def pokemon():
    pokemon = {
        'id': 1,
        'name': 'Bulbasaur',
        'flavor_text': 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.',
        'habitat': 'grassland',
        'color': 'green',
        'shape': 'quadruped'
    }

    return models.Pokemon(**pokemon)


@pytest.fixture
def move():
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

    return models.Move(**move)


def test_pokedex_create(pokedex):
    assert pokedex.id == 1
    assert pokedex.name == 'kanto'


def test_pokedex_repr(pokedex):
    assert repr(pokedex) == '<Pokedex kanto>'


def test_pokedex_relationship(pokedex, pokemon):
    pokedex.pokemon = [pokemon]

    assert pokedex.pokemon == [pokemon]


def test_pokemon_create(pokemon):
    assert pokemon.id == 1
    assert pokemon.name == 'Bulbasaur'


def test_pokemon_repr(pokemon):
    assert repr(pokemon) == '<Pokemon Bulbasaur>'


def test_pokemon_relationship(pokemon, pokedex):
    pokemon.pokedexes = [pokedex]

    assert pokemon.pokedexes == [pokedex]


def test_pokemon_relationship_2(pokemon, move):
    pokemon.moves = [move]

    assert pokemon.moves == [move]


def test_move_create(move):
    assert move.id == 1
    assert move.name == 'Razor Wind'


def test_move_repr(move):
    assert repr(move) == '<Move Razor Wind>'


def test_move_relationship(move, pokemon):
    move.pokemon = [pokemon]

    assert move.pokemon == [pokemon]
