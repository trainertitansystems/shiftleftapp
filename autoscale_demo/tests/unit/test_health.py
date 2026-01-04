from fastapi.testclient import TestClient
from autoscale_demo.app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
# we are doing the right tests
