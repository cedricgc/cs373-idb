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

from website import api_bp, app, db, ma
import website.api.models as models
import website.api.schemas as schemas

app.url_map.strict_slashes = False
"""Disables Werkzeug's strict route interpretation

There are good reasons for enforcing strict slashes for form posts and
indexability, but it is inconvienent when interacting with an API so
it is disabled.

See: http://flask.pocoo.org/docs/latest/quickstart/#variable-rules
"""

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


@api_bp.route('/pokedexes/', methods=['GET'])
def index_pokedexes():
    # Pass the noload option or ORM will do uneccessary queries
    pokedexes = models.Pokedex.query.options(sqlalchemy.orm.noload('*')).all()
    result = pokedexes_schema.dump(pokedexes)

    return flask.jsonify({'data': result.data}), 200


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
            db.session.add(pokedex)
            db.session.commit()
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
            db.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            db_error = {
                'errors': {
                    'database': ['Unable to update pokedex in database']
                }
            }

            return flask.jsonify(db_error), 422

        updated, errors = pokedex_schema.dump(pokedex)

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
        db.session.delete(pokedex)
        db.session.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db_error = {
            'errors': {
                'database': ['Unable to delete pokedex in database']
            }
        }

        return flask.jsonify(db_error), 422

    deleted, errors = pokedex_schema.dump(pokedex)

    return flask.jsonify({'data': deleted}), 200
