from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_rooms():
    response = client.get("/rooms")
    assert response.status_code == 200
    assert response.json() == []
