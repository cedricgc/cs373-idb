# -*- coding: utf-8 -*-


import pytest

from website import create_app
import website.api.models as models


@pytest.fixture(scope='session')
def app():
    """Instance of the Flask application available for testing"""
    app = create_app()
    app.config.from_object('config.TestConfig')

    return app


@pytest.fixture(scope='session')
def db(app):
    """Singleton that returns SQLAlchemy object associated with application"""
    models.db.init_app(app)
    return models.db


@pytest.fixture(autouse=True)
def transaction(request, db):
    """All tests are run in a transaction; database changes are rolled back"""
    db.session.begin(request.function.__name__)
    yield
    db.session.rollback()
