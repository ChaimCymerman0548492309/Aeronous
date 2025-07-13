import pytest
from fastapi.testclient import TestClient
from main import app, JSON_FILE
import json
import os

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_json_file():
    """נקה את קובץ ה-JSON לפני כל בדיקה"""
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)
    yield
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)

def test_add_and_get_targets():
    test_targets = [
        {"name": "Target1", "heading": 45.0, "signal_strength": 85, "timestamp": "2023-01-01T12:00:00"},
        {"name": "Target2", "heading": 90.0, "signal_strength": 25, "timestamp": "2023-01-01T12:01:00"}
    ]
    
    response = client.post("/targets", json=test_targets)
    assert response.status_code == 200
    
    response = client.get("/targets")
    assert response.status_code == 200
    targets = response.json()
    assert len(targets) == 2

def test_delete_target():
    test_target = [{"name": "ToDelete", "heading": 0.0, "signal_strength": 50, "timestamp": "2023-01-01T12:00:00"}]
    client.post("/targets", json=test_target)
    targets = client.get("/targets").json()
    target_id = targets[0]["id"]
    
    response = client.delete(f"/targets/{target_id}")
    assert response.status_code == 200
    
    response = client.get("/targets")
    assert len(response.json()) == 0

def test_invalid_target():
    response = client.post("/targets", json=[{"invalid": "data"}])
    assert response.status_code == 422