from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_generate_narasi():
    response = client.post("/narasi", json={"nama": "Ryu", "tipe": "perintis"})
    assert response.status_code == 200
    assert "menapaki jalan sunyi" in response.json()["narasi"]
