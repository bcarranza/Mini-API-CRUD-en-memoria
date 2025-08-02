import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)
def test_crear_item_con_emoji():
    item = {"name": "Item 🚀", "price": 50.0}
    response = client.post("/api/v1/items/", json=item)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Item 🚀"

def test_crear_item_precio_negativo():
    item = {"name": "Item con Descuento", "price": -10.50}
    response = client.post("/api/v1/items/", json=item)
    assert response.status_code == 422

def test_crear_item_nombre_vacio():
    item = {"name": "", "price": 10.50}
    response = client.post("/api/v1/items/", json=item)
    assert response.status_code == 422