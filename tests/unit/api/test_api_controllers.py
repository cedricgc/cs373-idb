# -*- coding: utf-8 -*-


import flask


def test_index_pokedexes(client):
    res = client.get(flask.url_for('api.index_pokedexes'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_create_pokedex(client, pokedex_json):
    res = client.post(flask.url_for('api.create_pokedex'),
                      data=pokedex_json,
                      content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 201
    assert res.mimetype == 'application/json'


def test_show_pokedex(client, pokedex_json):
    res = client.post(flask.url_for('api.create_pokedex'),
                      data=pokedex_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.get(flask.url_for('api.show_pokedex', pokedex_id=id))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_update_pokedex(client, pokedex_json, pokedex_json_updated):
    res = client.post(flask.url_for('api.create_pokedex'),
                      data=pokedex_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.put(flask.url_for('api.update_pokedex', pokedex_id=id),
                     data=pokedex_json_updated,
                     content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_delete_pokedex(client, pokedex_json):
    res = client.post(flask.url_for('api.create_pokedex'),
                      data=pokedex_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.delete(flask.url_for('api.delete_pokedex', pokedex_id=id))

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_index_pokemon(client):
    res = client.get(flask.url_for('api.index_pokemon'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_create_pokemon(client, pokemon_json):
    res = client.post(flask.url_for('api.create_pokemon'),
                      data=pokemon_json,
                      content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 201
    assert res.mimetype == 'application/json'


def test_show_pokemon(client, pokemon_json):
    res = client.post(flask.url_for('api.create_pokemon'),
                      data=pokemon_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.get(flask.url_for('api.show_pokemon', pokemon_id=id))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_update_pokemon(client, pokemon_json, pokemon_json_updated):
    res = client.post(flask.url_for('api.create_pokemon'),
                      data=pokemon_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.put(flask.url_for('api.update_pokemon', pokemon_id=id),
                     data=pokemon_json_updated,
                     content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_delete_pokemon(client, pokemon_json):
    res = client.post(flask.url_for('api.create_pokemon'),
                      data=pokemon_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.delete(flask.url_for('api.delete_pokemon', pokemon_id=id))

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_index_moves(client):
    res = client.get(flask.url_for('api.index_moves'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_create_move(client, move_json):
    res = client.post(flask.url_for('api.create_move'),
                      data=move_json,
                      content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 201
    assert res.mimetype == 'application/json'


def test_show_move(client, move_json):
    res = client.post(flask.url_for('api.create_move'),
                      data=move_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.get(flask.url_for('api.show_move', move_id=id))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_update_move(client, move_json, move_json_updated):
    res = client.post(flask.url_for('api.create_move'),
                      data=move_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.put(flask.url_for('api.update_move', move_id=id),
                     data=move_json_updated,
                     content_type='application/json')

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'


def test_delete_move(client, move_json):
    res = client.post(flask.url_for('api.create_move'),
                      data=move_json,
                      content_type='application/json')

    id = res.json['data']['id']
    res = client.delete(flask.url_for('api.delete_move', move_id=id))

    assert 'errors' not in res.json
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
