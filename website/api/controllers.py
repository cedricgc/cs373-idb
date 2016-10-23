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
pokdexes_schema = schemas.PokemonSchema(many=True,
                                        exclude=pokedex_exclude)

pokemon_exclude = ['pokedexes', 'moves']
pokemon_schema = schemas.PokemonSchema()
pokemons_excludes = schemas.PokemonSchema(many=True,
                                          exclude=pokemon_exclude)

move_exclude = ['pokemon']
move_schema = schemas.MoveSchema()
moves_exclude = schemas.MoveSchema(many=True,
                                   exclude=move_exclude)


@api_bp.route('/hello/', methods=['GET'])
def hello():
    return "Hello!"
