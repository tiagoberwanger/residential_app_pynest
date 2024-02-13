from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
