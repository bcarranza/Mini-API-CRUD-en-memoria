import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

#code 200:  indica que una solicitud se ha realizado correctamente.
def test_get_root_returns_200():
    response = client.get("/")
    assert response.status_code == 200

#code 201: indica que una solicitud POST se ha procesado correctamente y se ha creado un nuevo recurso.
def test_post_item_con_datos_validos():
    data = {"name": "Pen", "price": 1.5}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["name"] == data["name"]
    assert json_response["price"] == data["price"]
    assert "id" in json_response

#code: 422: indica que la solicitud no se ha podido procesar debido a errores de validación.
def test_post_item_con_datos_invalidos():
    data = {"name": "", "price": -10}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 422

 #Se agregaron 3 pruebas adicionales para verificar el manejo de errores

#PRUEBA 01
#se utilizo 400 indica que la solicitud no se ha podido procesar debido a errores de validación (el cliente dio un error).
def test_item_con_formato_incorrecto():
    data = {"name" "SinPrecio"}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 400

#PRUEBA 02
#se utilizo 409 indica que el recurso ya existe y no se puede crear de nuevo.
def test_post_item_con_id_existente():
    data = {"name": "Pen", "price": 1.5}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 201
    # Intentar crear el mismo item de nuevo, pero como la app no admite duplicados, debe fallar
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 409

# PRUEBA 03
#se utilizo 410 indica que el recurso solicitado existia pero ya no está disponible y no se puede acceder.
def test_item_no_encontrado():
    response = client.get("/api/v1/items/967")
    assert response.status_code == 410