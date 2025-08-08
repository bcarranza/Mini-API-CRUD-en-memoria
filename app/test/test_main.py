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

def test_obtener_todos_los_items():
    # Crear un item primero
    item_data = {"name": "Item para listar", "price": 5.0}
    client.post("/api/v1/items/", json=item_data)
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(item["name"] == "Item para listar" for item in response.json())

def test_obtener_item_por_id():
    # Crear un item y obtener su ID
    item_data = {"name": "Item por ID", "price": 7.5}
    post_response = client.post("/api/v1/items/", json=item_data)
    item_id = post_response.json().get("id")
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Item por ID"

def test_eliminar_item():
    # Crear un item y luego eliminarlo
    item_data = {"name": "Item a eliminar", "price": 3.0}
    post_response = client.post("/api/v1/items/", json=item_data)
    item_id = post_response.json().get("id")
    delete_response = client.delete(f"/api/v1/items/{item_id}")
    assert delete_response.status_code == 200 or delete_response.status_code == 204
    # Verificar que ya no existe
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404