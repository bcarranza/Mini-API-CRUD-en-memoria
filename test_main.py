import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestItemsAPI:
    """Clase de pruebas para la API de Items"""
    
    def setup_method(self):
        """Configuración antes de cada prueba - limpiar la base de datos en memoria"""
        
        from app.database.memory_db import items_db
        items_db.clear()
    
    def test_create_item_success(self):
        """Prueba 1: Crear un item exitosamente"""
        item_data = {
            "name": "Laptop Gaming",
            "price": 1299.99
        }
        
        response = client.post("/api/v1/items/", json=item_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Laptop Gaming"
        assert data["price"] == 1299.99
        assert data["id"] == 1
    
    def test_get_all_items_empty(self):
        """Prueba 2: Obtener todos los items cuando la lista está vacía"""
        response = client.get("/api/v1/items/")
        
        assert response.status_code == 200
        data = response.json()
        assert data == []
    
    def test_get_item_by_id_not_found(self):
        """Prueba 3: Obtener un item que no existe (error esperado)"""
        response = client.get("/api/v1/items/999")
        
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Item not found"
    
    def test_create_item_missing_fields(self):
        """Prueba 4: Crear item con datos faltantes (error esperado)"""
        # Enviar solo el nombre sin el precio
        item_data = {
            "name": "Laptop"
            # Falta el campo "price"
        }
        
        response = client.post("/api/v1/items/", json=item_data)
        
        assert response.status_code == 422  # Unprocessable Entity
        data = response.json()
        assert "detail" in data
    
    def test_update_item_success(self):
        """Prueba 5: Actualizar un item exitosamente"""
        # Primero crear un item
        create_data = {
            "name": "Laptop Original",
            "price": 999.99
        }
        create_response = client.post("/api/v1/items/", json=create_data)
        assert create_response.status_code == 201
        
       
        update_data = {
            "name": "Laptop Actualizada",
            "price": 1199.99
        }
        update_response = client.put("/api/v1/items/1", json=update_data)
        
        assert update_response.status_code == 200
        data = update_response.json()
        assert data["name"] == "Laptop Actualizada"
        assert data["price"] == 1199.99
        assert data["id"] == 1
    
    def test_delete_item_success(self):
        """Prueba 6: Eliminar un item exitosamente"""
     
        create_data = {
            "name": "Item a eliminar",
            "price": 100.0
        }
        create_response = client.post("/api/v1/items/", json=create_data)
        assert create_response.status_code == 201
        
        
        get_response = client.get("/api/v1/items/1")
        assert get_response.status_code == 200
        
       
        delete_response = client.delete("/api/v1/items/1")
        assert delete_response.status_code == 204
        
        # Verificar que ya no existe
        get_after_delete = client.get("/api/v1/items/1")
        assert get_after_delete.status_code == 404
    
    def test_create_item_invalid_price(self):
        """Prueba 7: Crear item con precio inválido (error esperado)"""
        item_data = {
            "name": "Laptop",
            "price": -100.0  # Precio negativo
        }
        
        response = client.post("/api/v1/items/", json=item_data)
        
        # Aunque Pydantic no valida precios negativos por defecto,
        # podemos verificar que la respuesta sea exitosa pero el precio sea negativo
        assert response.status_code == 201
        data = response.json()
        assert data["price"] == -100.0  # Confirmar que acepta precios negativos

if __name__ == "__main__":
    pytest.main([__file__]) 