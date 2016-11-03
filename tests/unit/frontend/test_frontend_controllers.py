# -*- coding: utf-8 -*-


import flask


def test_index(client):
    res = client.get(flask.url_for('frontend.index'))

    assert res.status_code == 200


def test_about(client):
    res = client.get(flask.url_for('frontend.about'))

    assert res.status_code == 200


def test_index_pokedexes(client):
    res = client.get(flask.url_for('frontend.index_pokedexes'))

    assert res.status_code == 200


def test_show_pokedex(client):
    res = client.get(flask.url_for('frontend.show_pokedex', id=1))

    assert res.status_code == 200


def test_index_pokemon(client):
    res = client.get(flask.url_for('frontend.index_pokemon'))

    assert res.status_code == 200


def test_show_pokemon(client):
    res = client.get(flask.url_for('frontend.show_pokemon', id=1))

    assert res.status_code == 200


def test_index_moves(client):
    res = client.get(flask.url_for('frontend.index_moves'))

    assert res.status_code == 200


def test_show_move(client):
    res = client.get(flask.url_for('frontend.show_move', id=1))

    assert res.status_code == 200
