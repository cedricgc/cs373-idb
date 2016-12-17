# -*- coding: utf-8 -*-


import flask


def test_index_pokedexes(client, seeds):
    res = client.get(flask.url_for('api.index_pokedexes'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


# def test_create_pokedex(client, pokedex_json):
#     res = client.post(flask.url_for('api.create_pokedex'),
#                       data=pokedex_json,
#                       content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 201


# def test_create_pokedex_bad_request(client):
#     res = client.post(flask.url_for('api.create_pokedex'),
#                       data='',
#                       content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400


def test_show_pokedex(client, seeds):
    res = client.get(flask.url_for('api.show_pokedex', pokedex_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_show_pokedex_index_error(client):
    res = client.get(flask.url_for('api.show_pokedex', pokedex_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' in res.json
    assert res.status_code == 404


# def test_update_pokedex(client, seeds, pokedex_json_updated):
#     res = client.put(flask.url_for('api.update_pokedex', pokedex_id=1),
#                      data=pokedex_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200


# def test_update_pokedex_index_error(client, pokedex_json_updated):
#     res = client.put(flask.url_for('api.update_pokedex', pokedex_id=1),
#                      data=pokedex_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404
#
#
# def test_update_pokedex_bad_request(client, seeds):
#     res = client.put(flask.url_for('api.update_pokedex', pokedex_id=1),
#                      data='',
#                      content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400
#
#
# def test_delete_pokedex(client, seeds):
#     res = client.delete(flask.url_for('api.delete_pokedex', pokedex_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200
#
#
# def test_delete_pokedex_index_error(client):
#     res = client.delete(flask.url_for('api.delete_pokedex', pokedex_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404


def test_index_pokemon(client, seeds):
    res = client.get(flask.url_for('api.index_pokemon'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


# def test_create_pokemon(client, pokemon_json):
#     res = client.post(flask.url_for('api.create_pokemon'),
#                       data=pokemon_json,
#                       content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 201


# def test_create_pokemon_bad_request(client):
#     res = client.post(flask.url_for('api.create_pokemon'),
#                       data='',
#                       content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400


def test_show_pokemon(client, seeds):
    res = client.get(flask.url_for('api.show_pokemon', pokemon_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_show_pokemon_index_error(client):
    res = client.get(flask.url_for('api.show_pokemon', pokemon_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' in res.json
    assert res.status_code == 404


# def test_update_pokemon(client, seeds, pokemon_json_updated):
#     res = client.put(flask.url_for('api.update_pokemon', pokemon_id=1),
#                      data=pokemon_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200
#
#
# def test_update_pokemon_index_error(client, pokemon_json_updated):
#     res = client.put(flask.url_for('api.update_pokemon', pokemon_id=1),
#                      data=pokemon_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404
#
#
# def test_update_pokemon_bad_request(client, seeds):
#     res = client.put(flask.url_for('api.update_pokemon', pokemon_id=1),
#                      data='',
#                      content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400


# def test_delete_pokemon(client, seeds):
#     res = client.delete(flask.url_for('api.delete_pokemon', pokemon_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200
#
#
# def test_delete_pokemon_index_error(client):
#     res = client.delete(flask.url_for('api.delete_pokemon', pokemon_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404


def test_index_moves(client, seeds):
    res = client.get(flask.url_for('api.index_moves'))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


# def test_create_move(client, move_json):
#     res = client.post(flask.url_for('api.create_move'),
#                       data=move_json,
#                       content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 201
#
#
# def test_create_move_bad_request(client):
#     res = client.post(flask.url_for('api.create_move'),
#                       data='',
#                       content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400


def test_show_move(client, seeds):
    res = client.get(flask.url_for('api.show_move', move_id=1))

    assert res.mimetype == 'application/json'
    assert res.status_code == 200


def test_show_move_index_error(client):
    res = client.get(flask.url_for('api.show_move', move_id=1))

    assert res.mimetype == 'application/json'
    assert 'errors' in res.json
    assert res.status_code == 404


# def test_update_move(client, seeds, move_json_updated):
#     res = client.put(flask.url_for('api.update_move', move_id=1),
#                      data=move_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200
#
#
# def test_update_move_index_error(client, move_json_updated):
#     res = client.put(flask.url_for('api.update_move', move_id=1),
#                      data=move_json_updated,
#                      content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404
#
#
# def test_update_move_bad_request(client, seeds):
#     res = client.put(flask.url_for('api.update_move', move_id=1),
#                      data='',
#                      content_type='text/plain')
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 400


# def test_delete_move(client, seeds):
#     res = client.delete(flask.url_for('api.delete_move', move_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' not in res.json
#     assert res.status_code == 200
#
#
# def test_delete_move_index_error(client):
#     res = client.delete(flask.url_for('api.delete_move', move_id=1))
#
#     assert res.mimetype == 'application/json'
#     assert 'errors' in res.json
#     assert res.status_code == 404
#
#
# def test_search_single(client, seeds, search_single_query_json):
#     res = client.post(flask.url_for('api.search'),
#                       data=search_single_query_json,
#                       content_type='application/json')
#
#     assert res.mimetype == 'application/json'
#     assert len(res.json['data']['pokedexes']) == 0
#     assert len(res.json['data']['pokemon']) == 1
#     assert len(res.json['data']['moves']) == 0
#     assert res.status_code == 200


def test_search_multi_and(client, seeds, search_multi_and_json):
    res = client.post(flask.url_for('api.search'),
                      data=search_multi_and_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert len(res.json['data']['pokedexes']) == 0
    assert len(res.json['data']['pokemon']) == 0
    assert len(res.json['data']['moves']) == 1
    assert res.status_code == 200


def test_search_multi_or(client, seeds, search_multi_or_json):
    res = client.post(flask.url_for('api.search'),
                      data=search_multi_or_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert len(res.json['data']['pokedexes']) == 1
    assert len(res.json['data']['pokemon']) == 1
    assert len(res.json['data']['moves']) == 0
    assert res.status_code == 200


def test_search_empty_query(client, seeds, search_empty_query_json):
    res = client.post(flask.url_for('api.search'),
                      data=search_empty_query_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert len(res.json['data']['pokedexes']) == 1
    assert len(res.json['data']['pokemon']) == 1
    assert len(res.json['data']['moves']) == 1
    assert res.status_code == 200


def test_search_null_query_error(client, seeds, search_null_query_json):
    res = client.post(flask.url_for('api.search'),
                      data=search_null_query_json,
                      content_type='application/json')

    assert res.mimetype == 'application/json'
    assert 'errors' in res.json
    assert res.status_code == 422


def test_search_empty_body_error(client, seeds, search_single_query_json):
    res = client.post(flask.url_for('api.search'),
                      data='',
                      content_type='application/json')

    assert res.mimetype == 'text/html'
    assert res.status_code == 400
