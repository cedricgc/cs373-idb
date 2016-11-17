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


import subprocess

import flask


frontend_bp = flask.Blueprint('frontend', __name__)
"""Flask.Blueprint: Client facing website

Client facing pages scoped to flask.Blueprint with a configurable asset location
"""


@frontend_bp.route('/', methods=['GET'])
def index():
    return flask.render_template('home.html')


@frontend_bp.route('/about', methods=['GET'])
def about():
    return flask.render_template('about.html')


@frontend_bp.route('/pokedexes', methods=['GET'])
def index_pokedexes():
    return flask.render_template('index_pokedexes.html')


@frontend_bp.route('/pokedexes/<id>', methods=['GET'])
def show_pokedex(id=None):
    return flask.render_template('show_pokedex.html', id=id)


@frontend_bp.route('/pokemon', methods=['GET'])
def index_pokemon():
    return flask.render_template('index_pokemon.html')


@frontend_bp.route('/pokemon/<id>', methods=['GET'])
def show_pokemon(id=None):
    return flask.render_template('show_pokemon.html', id=id)


@frontend_bp.route('/moves', methods=['GET'])
def index_moves():
    return flask.render_template('index_moves.html')


@frontend_bp.route('/moves/<id>', methods=['GET'])
def show_move(id=None):
    return flask.render_template('show_move.html', id=id)

@frontend_bp.route('/otherGroup', methods=['GET'])
def otherGroup():
        return flask.render_template('otherGroup.html')
        


@frontend_bp.route('/test/', methods=['GET'])
def run_tests():
    proc = subprocess.run(['make', 'test'], stdout=subprocess.PIPE)
    stdout = proc.stdout.decode('utf-8')

    return flask.Response(stdout, mimetype='text/plain'), 200
