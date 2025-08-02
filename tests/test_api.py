import pytest
from fastapi.testclient import TestClient
from app.main import app

cliente = TestClient(app)

class TestAPI:
    
    def test_obtener_raiz_retorna_200(self):
        respuesta = cliente.get("/")
        assert respuesta.status_code == 200
        assert respuesta.json() == {"message": "Bienvenido a la Mini API CRUD en memoria"}
    
    def test_crear_item_con_datos_validos(self):
        datos = {"name": "Laptop", "price": 1000.0}
        respuesta = cliente.post("/api/v1/items/", json=datos)
        assert respuesta.status_code == 201
        datos_respuesta = respuesta.json()
        assert datos_respuesta["name"] == datos["name"]
        assert datos_respuesta["price"] == datos["price"]
        assert "id" in datos_respuesta
    
    def test_crear_item_con_datos_invalidos_falla(self):
        datos_invalidos = {"name": "Producto sin precio"}
        respuesta = cliente.post("/api/v1/items/", json=datos_invalidos)   
        assert respuesta.status_code == 422
        assert "detail" in respuesta.json()
    
    def test_obtener_lista_items(self):
        respuesta = cliente.get("/api/v1/items/")
        assert respuesta.status_code == 200
        assert isinstance(respuesta.json(), list)
    
    def test_obtener_item_inexistente_retorna_404(self):
        respuesta = cliente.get("/api/v1/items/999")     
        assert respuesta.status_code == 404
        assert respuesta.json()["detail"] == "Item not found"
    
    def test_crear_y_obtener_item(self):
        datos = {"name": "Mouse", "price": 50.0}      
        respuesta_crear = cliente.post("/api/v1/items/", json=datos)
        assert respuesta_crear.status_code == 201     
        item_creado = respuesta_crear.json()
        id_item = item_creado["id"]       
        respuesta_obtener = cliente.get(f"/api/v1/items/{id_item}")
        assert respuesta_obtener.status_code == 200 
        item_obtenido = respuesta_obtener.json()
        assert item_obtenido["id"] == id_item
        assert item_obtenido["name"] == datos["name"]
        assert item_obtenido["price"] == datos["price"] 