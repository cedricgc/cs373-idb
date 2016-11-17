# -*- coding: utf-8 -*-
"""Routing and request handler for REST API

The flask app object provides the route decorator to dispatch requests
to the function as described in the decorator argument as well as controlling
the valid HTTP verbs that can be requested to that endpoint. The decorated
handler expects a flask.Response object as the return value.

See http://flask.pocoo.org/docs/latest/quickstart/#about-responses for how
flask converts return values to Response objects.
"""


import flask
import sqlalchemy
import requests
import json

import website.api.models as models
import website.api.schemas as schemas


api_bp = flask.Blueprint('api', __name__, url_prefix='/api/v1')
"""Flask.Blueprint: Web API

Initilize API as flask.Blueprint to keep it a modular part of the application
"""


ITEMS_PER_PAGE = 20

pokedex_exclude = ['pokemon']
pokedex_schema = schemas.PokedexSchema()
pokedexes_schema = schemas.PokedexSchema(many=True,
                                         exclude=pokedex_exclude)

pokemon_exclude = ['pokedexes', 'moves']
pokemon_schema = schemas.PokemonSchema()
# ¯\_(ツ)_/¯
pokemons_schema = schemas.PokemonSchema(many=True,
                                        exclude=pokemon_exclude)

move_exclude = ['pokemon']
move_schema = schemas.MoveSchema()
moves_schema = schemas.MoveSchema(many=True,
                                  exclude=move_exclude)

pokedex_pokemon_schema = schemas.PokedexPokemonSchema()
pokemon_moves_schema = schemas.PokemonMovesSchema()
search_schema = schemas.SearchSchema()





@api_bp.route('/search/', methods=['POST'])
def search():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        search, errors = search_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        query = search['query']
        pokedexes_result = models.Pokedex.query.search(query).limit(5).all()
        pokemon_result = models.Pokemon.query.search(query).limit(5).all()
        moves_result = models.Move.query.search(query).limit(5).all()

        pokedexes, errors = pokedexes_schema.dump(pokedexes_result)
        pokemon, errors = pokemons_schema.dump(pokemon_result)
        moves, errors = moves_schema.dump(moves_result)

        response = {
            'data': {
                'pokedexes': pokedexes,
                'pokemon': pokemon,
                'moves': moves
            }
        }

        return flask.jsonify(response), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422

@api_bp.route('/otherGroup')
def otherGroup():
    authors = requests.get("http://test.litdb.me/authors")

    return flask.jsonify(authors.text), 200

@api_bp.route('/pokedexes/', methods=['GET'])
def index_pokedexes():
    # Retrieve page requested, defaults to the first if none given
    page = flask.request.args.get('page', 1, type=int)
    # Pass the noload option or ORM will do uneccessary queries
    pokedexes_page = models.Pokedex.query.options(
        sqlalchemy.orm.noload('*')).paginate(page=page, per_page=ITEMS_PER_PAGE)
    data, errors = pokedexes_schema.dump(pokedexes_page.items)

    response = {
        'page': pokedexes_page.page,
        'total_pages': pokedexes_page.pages,
        'total_items': pokedexes_page.total,
        'has_next': pokedexes_page.has_next,
        'has_previous': pokedexes_page.has_prev,
        'data': data
    }

    return flask.jsonify(response), 200


@api_bp.route('/pokedexes/', methods=['POST'])
def create_pokedex():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        pokedex, errors = pokedex_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.add(pokedex)
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to add pokedex to database']
                }
            }

            return flask.jsonify(db_error), 422

        created, errors = pokedex_schema.dump(pokedex)

        return flask.jsonify({'data': created}), 201

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/pokedexes/<int:pokedex_id>', methods=['GET'])
def show_pokedex(pokedex_id):
    pokedex = models.Pokedex.query.get(pokedex_id)
    if not pokedex:
        index_error = {
            'errors': {
                'pokedex': ['pokedex with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    data, errors = pokedex_schema.dump(pokedex)

    return flask.jsonify({'data': data}), 200


@api_bp.route('/pokedexes/<int:pokedex_id>', methods=['PUT', 'PATCH'])
def update_pokedex(pokedex_id):
    pokedex = models.Pokedex.query.get(pokedex_id)
    if not pokedex:
        index_error = {
            'errors': {
                'pokedex': ['pokedex with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        # instance keyword arg loads data into existing model
        # all that needs to be done is to commit the change
        # partial keyword allows for updating only part of the model
        updated_pokedex, errors = pokedex_schema.load(json_data['data'],
                                                      instance=pokedex,
                                                      partial=True)
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to update pokedex in database']
                }
            }

            return flask.jsonify(db_error), 422

        updated, errors = pokedex_schema.dump(updated_pokedex)

        return flask.jsonify({'data': updated}), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/pokedexes/<int:pokedex_id>', methods=['DELETE'])
def delete_pokedex(pokedex_id):
    pokedex = models.Pokedex.query.get(pokedex_id)
    if not pokedex:
        index_error = {
            'errors': {
                'pokedex': ['pokedex with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    try:
        models.db.session.delete(pokedex)
        models.db.session.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db_error = {
            'errors': {
                'database': ['Unable to delete pokedex in database']
            }
        }

        return flask.jsonify(db_error), 422

    deleted, errors = pokedex_schema.dump(pokedex)

    return flask.jsonify({'data': deleted}), 200


@api_bp.route('/pokemon/', methods=['GET'])
def index_pokemon():
    page = flask.request.args.get('page', 1, type=int)
    pokemon_page = models.Pokemon.query.options(
        sqlalchemy.orm.noload('*')).paginate(page=page, per_page=ITEMS_PER_PAGE)
    data, errors = pokemons_schema.dump(pokemon_page.items)

    response = {
        'page': pokemon_page.page,
        'total_pages': pokemon_page.pages,
        'total_items': pokemon_page.total,
        'has_next': pokemon_page.has_next,
        'has_previous': pokemon_page.has_prev,
        'data': data
    }

    return flask.jsonify(response), 200


@api_bp.route('/pokemon/', methods=['POST'])
def create_pokemon():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        pokemon, errors = pokemon_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.add(pokemon)
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to add pokemon to database']
                }
            }

            return flask.jsonify(db_error), 422

        created, errors = pokemon_schema.dump(pokemon)

        return flask.jsonify({'data': created}), 201

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def show_pokemon(pokemon_id):
    pokemon = models.Pokemon.query.get(pokemon_id)
    if not pokemon:
        index_error = {
            'errors': {
                'pokemon': ['pokemon with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    data, errors = pokemon_schema.dump(pokemon)

    return flask.jsonify({'data': data}), 200


@api_bp.route('/pokemon/<int:pokemon_id>', methods=['PUT', 'PATCH'])
def update_pokemon(pokemon_id):
    pokemon = models.Pokemon.query.get(pokemon_id)
    if not pokemon:
        index_error = {
            'errors': {
                'pokemon': ['pokemon with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        updated_pokemon, errors = pokemon_schema.load(json_data['data'],
                                                      instance=pokemon,
                                                      partial=True)
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to update pokemon in database']
                }
            }

            return flask.jsonify(db_error), 422

        updated, errors = pokemon_schema.dump(updated_pokemon)

        return flask.jsonify({'data': updated}), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/pokemon/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    pokemon = models.Pokemon.query.get(pokemon_id)
    if not pokemon:
        index_error = {
            'errors': {
                'pokemon': ['pokemon with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    try:
        models.db.session.delete(pokemon)
        models.db.session.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db_error = {
            'errors': {
                'database': ['Unable to delete pokemon in database']
            }
        }

        return flask.jsonify(db_error), 422

    deleted, errors = pokemon_schema.dump(pokemon)

    return flask.jsonify({'data': deleted}), 200


@api_bp.route('/moves/', methods=['GET'])
def index_moves():
    page = flask.request.args.get('page', 1, type=int)
    moves_page = models.Move.query.options(
        sqlalchemy.orm.noload('*')).paginate(page=page, per_page=ITEMS_PER_PAGE)
    data, errors = moves_schema.dump(moves_page.items)

    response = {
        'page': moves_page.page,
        'total_pages': moves_page.pages,
        'total_items': moves_page.total,
        'has_next': moves_page.has_next,
        'has_previous': moves_page.has_prev,
        'data': data
    }

    return flask.jsonify(response), 200


@api_bp.route('/moves/', methods=['POST'])
def create_move():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        move, errors = move_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.add(move)
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to add move to database']
                }
            }

            return flask.jsonify(db_error), 422

        created, errors = move_schema.dump(move)

        return flask.jsonify({'data': created}), 201

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/moves/<int:move_id>', methods=['GET'])
def show_move(move_id):
    move = models.Move.query.get(move_id)
    if not move:
        index_error = {
            'errors': {
                'move': ['move with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    data, errors = move_schema.dump(move)

    return flask.jsonify({'data': data}), 200


@api_bp.route('/moves/<int:move_id>', methods=['PUT', 'PATCH'])
def update_move(move_id):
    move = models.Move.query.get(move_id)
    if not move:
        index_error = {
            'errors': {
                'move': ['move with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        updated_move, errors = move_schema.load(json_data['data'],
                                                instance=move,
                                                partial=True)
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        try:
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to update move in database']
                }
            }

            return flask.jsonify(db_error), 422

        updated, errors = move_schema.dump(updated_move)

        return flask.jsonify({'data': updated}), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/moves/<int:move_id>', methods=['DELETE'])
def delete_move(move_id):
    move = models.Move.query.get(move_id)
    if not move:
        index_error = {
            'errors': {
                'move': ['move with id does not exist']
            }
        }

        return flask.jsonify(index_error), 404

    try:
        models.db.session.delete(move)
        models.db.session.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db_error = {
            'errors': {
                'database': ['Unable to delete move in database']
            }
        }

        return flask.jsonify(db_error), 422

    deleted, errors = move_schema.dump(move)

    return flask.jsonify({'data': deleted}), 200


@api_bp.route('/pokedex_pokemon/', methods=['POST'])
def associate_pokedex_pokemon():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        relationship, errors = pokedex_pokemon_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        pokedex = models.Pokedex.query.get(relationship['pokedex_id'])
        if not pokedex:
            index_error = {
                'errors': {
                    'pokedex': ['pokedex with id does not exist']
                }
            }

            return flask.jsonify(index_error), 404

        pokemon = models.Pokemon.query.get(relationship['pokemon_id'])
        if not pokemon:
            index_error = {
                'errors': {
                    'pokemon': ['pokemon with id does not exist']
                }
            }

            return flask.jsonify(index_error), 404

        try:
            # Row created in association table implicitly
            pokedex.pokemon.append(pokemon)
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to associate pokedex and pokemon']
                }
            }

            return flask.jsonify(db_error), 422

        response = {
            'data': {
                'success': True
            }
        }
        return flask.jsonify(response), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422


@api_bp.route('/pokemon_moves/', methods=['POST'])
def associate_pokemon_moves():
    json_data = flask.request.get_json()
    if not json_data:
        bad_request = {
            'errors': {
                'input': ['the server could not read the input as JSON']
            }
        }

        return flask.jsonify(bad_request), 400

    if 'data' in json_data:
        relationship, errors = pokemon_moves_schema.load(json_data['data'])
        if errors:
            bad_request = {
                'errors': errors
            }

            return flask.jsonify(bad_request), 422

        pokemon = models.Pokemon.query.get(relationship['pokemon_id'])
        if not pokemon:
            index_error = {
                'errors': {
                    'pokemon': ['pokemon with id does not exist']
                }
            }

            return flask.jsonify(index_error), 404

        move = models.Move.query.get(relationship['move_id'])
        if not move:
            index_error = {
                'errors': {
                    'move': ['move with id does not exist']
                }
            }

            return flask.jsonify(index_error), 404

        try:
            # Row created in association table implicitly
            pokemon.moves.append(move)
            models.db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to associate pokemon and move']
                }
            }

            return flask.jsonify(db_error), 422

        response = {
            'data': {
                'success': True
            }
        }
        return flask.jsonify(response), 200

    else:
        bad_request = {
            'errors': {
                'input': ['missing required "data" key at top level']
            }
        }

        return flask.jsonify(bad_request), 422
