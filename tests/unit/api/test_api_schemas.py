# -*- coding: utf-8 -*-


import pytest

import website.api.schemas as schemas


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


def test_pokedex_schema(pokedex, pokedex_schema):
    pd, errors = pokedex_schema.load(pokedex)

    assert errors == {}


def test_pokedex_null_schema_fields(null_pokedex, pokedex_schema):
    pd, errors = pokedex_schema.load(null_pokedex)

    expected = {
        'name': ['Field may not be null.'],
        'official_name': ['Field may not be null.']
    }

    assert errors == expected


def test_pokemon_schema(pokemon, pokemon_schema):
    po, errors = pokemon_schema.load(pokemon)

    assert errors == {}


def test_pokemon_null_schema_fields(null_pokemon, pokemon_schema):
    po, errors = pokemon_schema.load(null_pokemon)

    expected = {
        'name': ['Field may not be null.'],
        'flavor_text': ['Field may not be null.'],
        'color': ['Field may not be null.'],
        'shape': ['Field may not be null.']
    }

    assert errors == expected


def test_move_schema(move, move_schema):
    mv, errors = move_schema.load(move)

    assert errors == {}


def test_move_null_schema_fields(null_move, move_schema):
    mv, errors = move_schema.load(null_move)

    expected = {
        'name': ['Field may not be null.'],
        'short_effect': ['Field may not be null.'],
        'effect': ['Field may not be null.']
    }

    assert errors == expected