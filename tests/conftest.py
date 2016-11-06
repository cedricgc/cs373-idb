# -*- coding: utf-8 -*-


import pytest

from website import create_app
from website.api.models import db as database


@pytest.fixture(scope='session')
def app():
    """Instance of the Flask application available for testing"""
    app = create_app()
    app.config.from_object('config.TestConfig')

    return app


@pytest.fixture(scope='session')
def db(app):
    """Singleton that returns SQLAlchemy object associated with application"""
    database.init_app(app)
    return database


@pytest.fixture(autouse=True)
def transaction(request, db):
    db.session.begin(request.function.__name__)
    yield
    db.session.rollback()
