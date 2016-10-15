# -*- coding: utf-8 -*-


import os

# Determine code location in file system
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database URI used by SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
DATABASE_CONNECT_OPTIONS = {}

# Flask configuration: see http://flask.pocoo.org/docs/latest/config/

# By default Flask serializes objects to ascii-encoded JSON.
# If this is set to False Flask will not encode to ASCII and output strings
# as-is and return unicode strings.
JSON_AS_ASCII = False
