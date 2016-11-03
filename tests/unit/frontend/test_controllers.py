# -*- coding: utf-8 -*-


import flask


def test_index_get(client):
    res = client.get(flask.url_for('frontend.index'))

    assert res.status_code == 200


def test_about_get(client):
    res = client.get(flask.url_for('frontend.about'))

    assert res.status_code == 200


def test_index_pokedexes_get(client):
    res = client.get(flask.url_for('frontend.index_pokedexes'))

    assert res.status_code == 200


def test_show_pokedex_get(client):
    res = client.get(flask.url_for('frontend.show_pokedex', id=1))

    assert res.status_code == 200


def test_index_pokemon_get(client):
    res = client.get(flask.url_for('frontend.index_pokemon'))

    assert res.status_code == 200


def test_show_pokemon_get(client):
    res = client.get(flask.url_for('frontend.show_pokemon', id=1))

    assert res.status_code == 200


def test_index_moves_get(client):
    res = client.get(flask.url_for('frontend.index_moves'))

    assert res.status_code == 200


def test_show_move_get(client):
    res = client.get(flask.url_for('frontend.show_move', id=1))

    assert res.status_code == 200
