"""Tests for the categories catalog API endpoint."""

from ai_engine.classifier.categories import CATEGORY_NAMES


def test_get_categories_endpoint(client):
    response = client.get("/api/categories")
    assert response.status_code == 200
    data = response.json()
    
    assert data["total_categories"] == 7
    categories = data["categories"]
    assert len(categories) == 7
    
    returned_names = [c["name"] for c in categories]
    assert set(returned_names) == set(CATEGORY_NAMES)
    
    for c in categories:
        assert isinstance(c["id"], str) and len(c["id"]) > 0
        assert isinstance(c["name"], str) and len(c["name"]) > 0
        assert isinstance(c["description"], str) and len(c["description"]) > 10
        assert isinstance(c["examples"], list) and len(c["examples"]) > 0
        assert isinstance(c["typical_linguistic_indicators"], list) and len(c["typical_linguistic_indicators"]) > 0
        assert isinstance(c["risk_interpretation"], str) and len(c["risk_interpretation"]) > 0
        assert 0.0 <= c["base_risk_weight"] <= 100.0
