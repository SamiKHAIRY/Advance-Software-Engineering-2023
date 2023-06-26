import pytest
from exam import app

@pytest.fixture
def client():
    c = app.create_app()
    c.config['TESTING'] = True
    test_client = c.test_client()

    yield test_client
