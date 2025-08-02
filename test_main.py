# test_main.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestItemsAPI:
    def setup_method(self):
        from app.database.memory_db import items_db
        items_db.clear()
    
    def test_create_item_success(self):
        response = client.post("/api/v1/items/", json={"name": "Laptop", "price": 999.99})
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Laptop" and data["price"] == 999.99 and data["id"] == 1
    
    def test_get_all_items_empty(self):
        assert client.get("/api/v1/items/").json() == []
    
    def test_get_item_by_id_not_found(self):
        response = client.get("/api/v1/items/999")
        assert response.status_code == 404 and response.json()["detail"] == "Item not found"
    
    def test_create_item_missing_fields(self):
        response = client.post("/api/v1/items/", json={"name": "Laptop"})
        assert response.status_code == 422
    
    def test_update_item_success(self):
        client.post("/api/v1/items/", json={"name": "Original", "price": 100})
        response = client.put("/api/v1/items/1", json={"name": "Updated", "price": 200})
        assert response.status_code == 200 and response.json()["name"] == "Updated"
    
    def test_delete_item_success(self):
        client.post("/api/v1/items/", json={"name": "Delete", "price": 100})
        assert client.delete("/api/v1/items/1").status_code == 204
        assert client.get("/api/v1/items/1").status_code == 404
    
    def test_create_item_invalid_price(self):
        response = client.post("/api/v1/items/", json={"name": "Laptop", "price": -100})
        assert response.status_code == 201 and response.json()["price"] == -100

if __name__ == "__main__":
    pytest.main([__file__]) 