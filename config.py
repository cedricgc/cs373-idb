# -*- coding: utf-8 -*-


import os

# Determine code location in file system
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FILES = os.path.join(BASE_DIR, 'static')
TEMPLATES = os.path.join(BASE_DIR, 'templates')

# Database configuration used by SQLAlchemy and flask_sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask configuration: see http://flask.pocoo.org/docs/latest/config/

# By default Flask serializes objects to ascii-encoded JSON.
# If this is set to False Flask will not encode to ASCII and output strings
# as-is and return unicode strings.
JSON_AS_ASCII = False
