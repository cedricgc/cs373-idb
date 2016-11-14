# -*- coding: utf-8 -*-
"""Handles validation and (de)serialization for API resources

The validation library provides schemas to validate inputs received by clients,
generating human readable errors that can be returned to the client. Since
what we want to validate is closely aligned to the API models we use an
integration library to generate schemas directly from the ORM models as well
as load inputs directly into models during deserialization.

The schemas also handle loading and dumping data from simple python types to
complex models and vice versa, which is important when creating a REST JSON API.
"""


import flask_marshmallow
import marshmallow

import website.api.models as models


# Initialize after SQLAlchemy object
ma = flask_marshmallow.Marshmallow()
"""Marshmallow: Python Object (de)serialization

flask_marshmallow integrates with Flask and SQLAlchemy to allow for
generation of validators for API inputs directly from a SQLAlchemy model
"""


class BaseSchema(ma.ModelSchema):

    class Meta:
        # prevent accounting columns showing up in JSON
        exclude = ['inserted_at', 'updated_at', 'search_vector']


class PokedexSchema(BaseSchema):

    # id values are ignored during deserialization as they are generated
    # by database
    id = marshmallow.fields.Integer(dump_only=True)

    # Refer to other schemas with strings; this will prevent circular references
    # library will use reflection to find class after interpretation
    pokemon = marshmallow.fields.Nested('PokemonSchema',
                                        many=True,
                                        dump_only=True,
                                        exclude=['pokedexes', 'moves'])

    class Meta(BaseSchema.Meta):
        model = models.Pokedex
        # Include foreign keys in output
        include_fk = True


class PokemonSchema(BaseSchema):

    id = marshmallow.fields.Integer(dump_only=True)

    pokedexes = marshmallow.fields.Nested('PokedexSchema',
                                          many=True,
                                          dump_only=True,
                                          exclude=['pokemon'])
    moves = marshmallow.fields.Nested('MoveSchema',
                                      many=True,
                                      dump_only=True,
                                      exclude=['pokemon'])

    class Meta(BaseSchema.Meta):
        model = models.Pokemon
        include_fk = True


class MoveSchema(BaseSchema):

    id = marshmallow.fields.Integer(dump_only=True)

    pokemon = marshmallow.fields.Nested('PokemonSchema',
                                        many=True,
                                        dump_only=True,
                                        exclude=['pokedexes', 'moves'])

    class Meta(BaseSchema.Meta):
        model = models.Move
        include_fk = True


class PokedexPokemonSchema(marshmallow.Schema):

    pokedex_id = marshmallow.fields.Integer(load_only=True)
    pokemon_id = marshmallow.fields.Integer(load_only=True)


class PokemonMovesSchema(marshmallow.Schema):

    pokemon_id = marshmallow.fields.Integer(load_only=True)
    move_id = marshmallow.fields.Integer(load_only=True)
