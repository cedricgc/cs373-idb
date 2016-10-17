# -*- coding: utf-8 -*-


import flask
import flask_marshmallow
import flask_sqlalchemy


app = flask.Flask(__name__)
app.config.from_object('config')
app.static_folder = app.config['STATIC_FILES']
app.template_folder = app.config['TEMPLATES']
"""Flask: project application instance

The Flask object handles the application routing, configuration, and HTTP
Middleware through WSGI.
"""

api_bp = flask.Blueprint('api', 'website.pokemon_api', url_prefix='/api/v1')
"""Flask.Blueprint: Web API

Initilize API as flask.Blueprint to keep it a modular part of the application
"""

frontend_bp = flask.Blueprint('frontend', 'website.frontend')
"""Flask.Blueprint: Client facing website

Client facing pages scoped to flask.Blueprint with a configurable asset location
"""

db = flask_sqlalchemy.SQLAlchemy(app)
"""SQLAlchemy: SQLAlchemy with Flask integration

The SQLAlchemy object handles interactions with the application's
database. the object provides the db.Model class to create Python
abstractions around resources as well as query execution functions
"""

# Initialize after SQLAlchemy object
ma = flask_marshmallow.Marshmallow(app)
"""Marshmallow: Python Object (de)serialization

flask_marshmallow integrates with Flask and SQLAlchemy to allow for
generation of validators for API inputs directly from a SQLAlchemy model
"""

# We import controllers after top level object or interpreter would crash
# due to circular dependencies
# Ensure route controllers are executed by interpreter
import website.api.controllers


app.register_blueprint(api_bp)
app.register_blueprint(frontend_bp)
