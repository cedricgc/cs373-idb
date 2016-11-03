# -*- coding: utf-8 -*-


import pytest

from website import create_app


@pytest.fixture
def app():
    """Instance of the Flask application available for testing"""
    app = create_app()

    return app
