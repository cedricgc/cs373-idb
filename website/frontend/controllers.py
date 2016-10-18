# -*- coding: utf-8 -*-
"""Routing and request handler for client facing part of website

The flask Blueprint object provides the route decorator to dispatch requests
to the function as described in the decorator argument as well as controlling
the valid HTTP verbs that can be requested to that endpoint. The decorated
handler expects a flask.Response object as the return value.

See http://flask.pocoo.org/docs/latest/quickstart/#about-responses for how
flask converts return values to Response objects.

Flask uses Jinja2 as the templating engine to safely interpolate python objects
and embed control flow in HTML templates.

See http://flask.pocoo.org/docs/latest/quickstart/#rendering-templates for how
to render data from the controller to the template
"""


import flask

from website import frontend_bp


@frontend_bp.route('/', methods=['GET'])
def index():
    return flask.render_template('home.html')


@frontend_bp.route('/about', methods=['GET'])
def about():
    return flask.render_template('about.html')


@frontend_bp.route('/pokedexes', methods=['GET'])
def pokedexes():
    return flask.render_template('pokedexes.html')


@frontend_bp.route('/pokemon', methods=['GET'])
def pokemon():
    return flask.render_template('pokemon.html')

@frontend_bp.route('/pokemon_info/<id>', methods=['GET'])
def pokemon_info(id=None):
    return flask.render_template('pokemon_info.html', id=id)

@frontend_bp.route('/moves', methods=['GET'])
def moves():
    return flask.render_template('moves.html')
