from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_root_regresa_200():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_post_items_validos():
    data = {"name": "Pepino", "price": 12}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "Pepino"
    assert response.json()["price"] == 12

def test_post_items_datos_invalidos():
    data = {"name": "Pan", "price": -0}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 422