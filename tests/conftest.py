import pytest

from rest_api_app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True
    })

    yield app


@pytest.fixture(autouse=True)
def client(app):
    return app.test_client()
