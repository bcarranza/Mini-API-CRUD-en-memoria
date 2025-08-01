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
    json_response = response.json()
    assert json_response["name"] == data["name"]
    assert json_response["price"] == data["price"]

def test_post_items_datos_invalidos():
    data = {"name": "Pan", "price": -0}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 422

def test_get_item_no_existente():
    response = client.get("/api/v1/items/9999")
    assert response.status_code == 404

def test_post_items_datos_faltantes():
    data = {"price": 10}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 422

def test_borrar_item_existente():
    data = {"name": "Tomate", "price": 5}
    post_response = client.post("/api/v1/items/", json=data)
    item_id = post_response.json()["id"]
    delete_response = client.delete(f"/api/v1/items/{item_id}")
    assert delete_response.status_code in (200, 204)

