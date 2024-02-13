from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_contracts():
    response = client.get("/contracts")
    assert response.status_code == 200
    assert response.json() == []
