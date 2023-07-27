import pytest

from helpers.flask_app import create_app


@pytest.fixture(scope="session")
def app():
    application = create_app()

    return application
