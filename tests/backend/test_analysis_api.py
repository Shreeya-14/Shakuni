"""Tests for the analysis and batch analysis endpoints."""

from ai_engine.classifier.categories import CATEGORY_NAMES


def test_analyze_valid_text(client):
    payload = {
        "text": "Everyone else in the department has already agreed to the new policy, don't be the lone dissenter holding us back."
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    assert data["text"] == payload["text"]
    assert data["category"] in CATEGORY_NAMES
    assert 0 <= data["risk_score"] <= 100
    assert data["risk_level"] in ["Low", "Moderate", "High"]
    assert 0.0 <= data["confidence"] <= 1.0
    assert isinstance(data["explanation"], str) and len(data["explanation"]) > 0
    assert isinstance(data["indicators"], list)
    assert isinstance(data["probabilities"], dict)
    
    # Verify all 7 categories exist in probabilities
    for cat in CATEGORY_NAMES:
        assert cat in data["probabilities"]
    
    prob_sum = sum(data["probabilities"].values())
    assert abs(prob_sum - 1.0) < 0.05


def test_analyze_empty_text(client):
    payload = {"text": ""}
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "Validation Error" in data["error"]


def test_analyze_whitespace_text(client):
    payload = {"text": "   \n\t  "}
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "Validation Error" in data["error"]


def test_analyze_missing_field(client):
    payload = {}
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_oversized_text(client):
    payload = {"text": "A" * 10001}
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422


def test_batch_analyze_valid(client):
    payload = {
        "texts": [
            "The laboratory confirmed that the water sample adheres to municipal drinking safety guidelines.",
            "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer.",
            "Our revolutionary battery technology demonstrated a four hundred percent charge retention in lab tests."
        ]
    }
    response = client.post("/api/batch-analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    assert data["total_analyzed"] == 3
    assert len(data["results"]) == 3
    for res in data["results"]:
        assert res["category"] in CATEGORY_NAMES
        assert 0 <= res["risk_score"] <= 100
        assert 0.0 <= res["confidence"] <= 1.0


def test_batch_analyze_empty_list(client):
    payload = {"texts": []}
    response = client.post("/api/batch-analyze", json=payload)
    assert response.status_code == 422


def test_batch_analyze_contains_blank_item(client):
    payload = {
        "texts": [
            "Valid standard sentence here.",
            "   "
        ]
    }
    response = client.post("/api/batch-analyze", json=payload)
    assert response.status_code == 422
