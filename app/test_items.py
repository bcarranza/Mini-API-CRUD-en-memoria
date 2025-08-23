from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_database():
    """Reset the database before each test"""
    from app.database.memory_db import reset_db
    reset_db()

def test_create_item():
    """Test creating a new item"""
    item_data = {
        "name": "Test Item",
        "price": 25.99
    }
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert "id" in data
    assert data["id"] == 1

def test_read_items_empty():
    """Test reading items when database is empty"""
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_items():
    """Test reading all items"""
    # Create some test items
    test_items = [
        {"name": "Item 1", "price": 10.50},
        {"name": "Item 2", "price": 20.75}
    ]
    
    for item in test_items:
        client.post("/api/v1/items/", json=item)
    
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Item 1"
    assert data[1]["name"] == "Item 2"

def test_read_item_by_id():
    """Test reading a specific item by ID"""
    # Create a test item
    item_data = {"name": "Test Item", "price": 15.99}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Get the item by ID
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]

def test_read_item_not_found():
    """Test reading a non-existent item"""
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_update_item():
    """Test updating an existing item"""
    # Create a test item
    item_data = {"name": "Original Item", "price": 10.00}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Update the item
    update_data = {"name": "Updated Item", "price": 25.50}
    response = client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == update_data["name"]
    assert data["price"] == update_data["price"]

def test_update_item_not_found():
    """Test updating a non-existent item"""
    update_data = {"name": "Updated Item", "price": 25.50}
    response = client.put("/api/v1/items/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_item():
    """Test deleting an existing item"""
    # Create a test item
    item_data = {"name": "Item to Delete", "price": 5.99}
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204
    
    # Verify item is deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404

def test_delete_item_not_found():
    """Test deleting a non-existent item"""
    response = client.delete("/api/v1/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_crud_workflow():
    """Test complete CRUD workflow"""
    # Create
    item_data = {"name": "Workflow Item", "price": 30.00}
    create_response = client.post("/api/v1/items/", json=item_data)
    assert create_response.status_code == 201
    item_id = create_response.json()["id"]
    
    # Read
    read_response = client.get(f"/api/v1/items/{item_id}")
    assert read_response.status_code == 200
    assert read_response.json()["name"] == item_data["name"]
    
    # Update
    update_data = {"name": "Updated Workflow Item", "price": 45.00}
    update_response = client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_data["name"]
    
    # Delete
    delete_response = client.delete(f"/api/v1/items/{item_id}")
    assert delete_response.status_code == 204
    
    # Verify deletion
    final_read = client.get(f"/api/v1/items/{item_id}")
    assert final_read.status_code == 404 