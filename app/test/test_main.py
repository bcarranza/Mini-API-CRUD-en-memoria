from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_create_item():
    data = {"name": "Pen", "price": 1.5}
    response = client.post("/api/v1/items/", json=data)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["name"] == data["name"]
    assert json_response["price"] == data["price"]
    assert "id" in json_response
