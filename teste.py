import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ola":"mundo"}

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"ola":"mundo"}