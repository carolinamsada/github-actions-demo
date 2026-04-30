from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_square():
    response = client.get("/square/4")
    assert response.status_code == 200
    assert response.json() == {"result": 16}
