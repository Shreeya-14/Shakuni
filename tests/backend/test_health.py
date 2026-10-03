"""Tests for the health check API endpoint."""


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "shakuni-api"
    assert "version" in data
    assert data["model_loaded"] is True


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["framework"] == "Shakuni"
    assert "endpoints" in data
