# -*- coding: utf-8 -*-


import flask


def test_index_pokedexes(client, seeds):
    res = client.get(flask.url_for('api.index_pokedexes'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_create_pokedex(client, pokedex_json):
    res = client.post(flask.url_for('api.create_pokedex'),
                      data=pokedex_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 201


def test_show_pokedex(client, seeds):
    res = client.get(flask.url_for('api.show_pokedex', pokedex_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_update_pokedex(client, seeds, pokedex_json_updated):
    res = client.put(flask.url_for('api.update_pokedex', pokedex_id=1),
                     data=pokedex_json_updated,
                     content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200


def test_delete_pokedex(client, seeds):
    res = client.delete(flask.url_for('api.delete_pokedex', pokedex_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200


def test_index_pokemon(client, seeds):
    res = client.get(flask.url_for('api.index_pokemon'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_create_pokemon(client, pokemon_json):
    res = client.post(flask.url_for('api.create_pokemon'),
                      data=pokemon_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 201


def test_show_pokemon(client, seeds):
    res = client.get(flask.url_for('api.show_pokemon', pokemon_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_update_pokemon(client, seeds, pokemon_json_updated):
    res = client.put(flask.url_for('api.update_pokemon', pokemon_id=1),
                     data=pokemon_json_updated,
                     content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200


def test_delete_pokemon(client, seeds):
    res = client.delete(flask.url_for('api.delete_pokemon', pokemon_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200


def test_index_moves(client, seeds):
    res = client.get(flask.url_for('api.index_moves'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_create_move(client, move_json):
    res = client.post(flask.url_for('api.create_move'),
                      data=move_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 201


def test_show_move(client, seeds):
    res = client.get(flask.url_for('api.show_move', move_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_update_move(client, seeds, move_json_updated):
    res = client.put(flask.url_for('api.update_move', move_id=1),
                     data=move_json_updated,
                     content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200


def test_delete_move(client, seeds):
    res = client.delete(flask.url_for('api.delete_move', move_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' not in res.json
    assert res.status_code == 200
