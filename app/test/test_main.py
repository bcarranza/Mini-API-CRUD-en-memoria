from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_retorna_codigo_200():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la Mini API CRUD en memoria"}

def test_items_con_datos_validos():
    item_data = {"name": "Item de prueba", "price": 10.5}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201 or response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"] == "Item de prueba"

def test_items_con_datos_invalidos():
    item_data = {}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 422 