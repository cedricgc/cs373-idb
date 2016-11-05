# -*- coding: utf-8 -*-


import pytest

import website.api.models as models


@pytest.fixture
def pokedex_model(pokedex):
    return models.Pokedex(**pokedex)


@pytest.fixture
def pokemon_model(pokemon):
    return models.Pokemon(**pokemon)


@pytest.fixture
def move_model(move):
    return models.Move(**move)


def test_pokedex_create(pokedex_model):
    assert pokedex_model.id == 1
    assert pokedex_model.name == 'kanto'


def test_pokedex_repr(pokedex_model):
    assert repr(pokedex_model) == '<Pokedex kanto>'


def test_pokedex_relationship(pokedex_model, pokemon_model):
    pokedex_model.pokemon = [pokemon_model]

    assert pokedex_model.pokemon == [pokemon_model]


def test_pokemon_create(pokemon_model):
    assert pokemon_model.id == 1
    assert pokemon_model.name == 'Bulbasaur'


def test_pokemon_repr(pokemon_model):
    assert repr(pokemon_model) == '<Pokemon Bulbasaur>'


def test_pokemon_relationship(pokemon_model, pokedex_model):
    pokemon_model.pokedexes = [pokedex_model]

    assert pokemon_model.pokedexes == [pokedex_model]


def test_pokemon_relationship_2(pokemon_model, move_model):
    pokemon_model.moves = [move_model]

    assert pokemon_model.moves == [move_model]


def test_move_create(move_model):
    assert move_model.id == 1
    assert move_model.name == 'Razor Wind'


def test_move_repr(move_model):
    assert repr(move_model) == '<Move Razor Wind>'


def test_move_relationship(move, pokemon_model):
    move_model.pokemon = [pokemon_model]

    assert move_model.pokemon == [pokemon_model]
