from fastapi.testclient import TestClient

from app.main import app


def test_health_check():
    """Health endpoint returns 200 with expected payload."""
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "spiritual-ai-backend"
