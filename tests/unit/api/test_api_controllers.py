# -*- coding: utf-8 -*-


import flask


def test_index_pokedexes(client):
    res = client.get(flask.url_for('api.index_pokedexes'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_index_pokemon(client):
    res = client.get(flask.url_for('api.index_pokemon'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_index_moves(client):
    res = client.get(flask.url_for('api.index_moves'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
