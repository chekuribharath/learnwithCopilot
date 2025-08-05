import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data

def test_index_post_greet(client):
    response = client.post("/", data={"name": "Bob"})
    assert response.status_code == 200
    assert b"Hello, Bob" in response.data
