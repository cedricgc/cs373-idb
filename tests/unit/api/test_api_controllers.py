# -*- coding: utf-8 -*-


import flask


def test_index_pokedexes(client):
    res = client.get(flask.url_for('api.index_pokedexes'))

    assert res.status_code == 200
