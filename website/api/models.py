# -*- coding: utf-8 -*-


import flask_sqlalchemy


db = flask_sqlalchemy.SQLAlchemy()
"""SQLAlchemy: SQLAlchemy with Flask integration

The SQLAlchemy object handles interactions with the application's
database. the object provides the db.Model class to create Python
abstractions around resources as well as query execution functions
"""


class Base(db.Model):
    """Abstract Model for defining shared columns between models"""

    __abstract__ = True

    inserted_at = db.Column(db.DateTime,
                            default=db.func.current_timestamp(),
                            nullable=False)
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp(),
                           nullable=False)


pokedex_pokemon = db.Table(
    'pokedex_pokemon',
    Base.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('pokedex_id', db.Integer, db.ForeignKey('pokedexes.id')),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'))
)


pokemon_moves = db.Table(
    'pokemon_moves',
    Base.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
    db.Column('move_id', db.Integer, db.ForeignKey('moves.id')),
)


class Pokedex(Base):

    __tablename__ = 'pokedexes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    official_name = db.Column(db.Text, unique=True, nullable=False)
    region = db.Column(db.Text, nullable=True, default=None)
    description = db.Column(db.Text, nullable=True, default=None)

    pokemon = db.relationship('Pokemon',
                              secondary=pokedex_pokemon,
                              back_populates='pokedexes')

    def __repr__(self):
        return '<Pokedex {}>'.format(self.name)


class Pokemon(Base):

    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    flavor_text = db.Column(db.Text, nullable=False)
    habitat = db.Column(db.Text, nullable=True, default=None)
    color = db.Column(db.Text, nullable=False)
    shape = db.Column(db.Text, nullable=False)

    pokedexes = db.relationship('Pokedex',
                                secondary=pokedex_pokemon,
                                back_populates='pokemon')
    moves = db.relationship('Move',
                            secondary=pokemon_moves,
                            back_populates='pokemon')

    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)


class Move(Base):

    __tablename__ = 'moves'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    flavor_text = db.Column(db.Text, nullable=True, default=None)
    short_effect = db.Column(db.Text, nullable=False)
    effect = db.Column(db.Text, nullable=False)
    damage_class = db.Column(db.Text, nullable=True, default=None)
    power_points = db.Column(db.Integer, nullable=True, default=None)
    power = db.Column(db.Integer, nullable=True, default=None)
    accuracy = db.Column(db.Integer, nullable=True, default=None)

    pokemon = db.relationship('Pokemon',
                              secondary=pokemon_moves,
                              back_populates='moves')

    def __repr__(self):
        return '<Move {}>'.format(self.name)
