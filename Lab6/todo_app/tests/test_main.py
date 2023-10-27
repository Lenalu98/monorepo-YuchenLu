import pytest
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"skip": 0}

def test_read_items_with_query():
    response = client.get("/items_with_query/42?skip=5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "skip": 5}

def test_create_item():
    item = {"name": "Example Item", "description": "This is a test item."}
    response = client.post("/items/", json=item)
    assert response.status_code == 200
    assert response.json() == item

def test_update_item():
    item_id = 42
    updated_item = {"name": "Updated Item", "description": "This is the updated item."}
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "updated_item": updated_item}

def test_delete_item():
    item_id = 42
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Item {item_id} deleted successfully"}