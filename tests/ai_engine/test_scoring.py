"""Tests for risk scoring, confidence, and linguistic indicators."""

from ai_engine.analysis.indicators import detect_indicators, DetectedIndicator
from ai_engine.analysis.confidence import calculate_confidence
from ai_engine.analysis.risk_score import calculate_risk_score
from ai_engine.classifier.categories import CATEGORY_NAMES


def test_detect_indicators_empty():
    indicators = detect_indicators("")
    assert indicators == []


def test_detect_indicators_social_pressure():
    text = "Everyone else has already signed the pledge, don't be the lone dissenter holding us back."
    indicators = detect_indicators(text)
    assert len(indicators) > 0
    indicator_names = [ind.name for ind in indicators]
    assert any("Conformity" in name or "Ostracization" in name for name in indicator_names)


def test_detect_indicators_guilt_and_urgency():
    text = "If you really loved our family you would do this right this minute or catastrophic failure will occur."
    indicators = detect_indicators(text)
    assert len(indicators) >= 2


def test_calculate_confidence_bounds():
    probs = {"Normal / No Significant Manipulation": 0.8251, "Social Pressure": 0.1749}
    conf = calculate_confidence(probs, "Normal / No Significant Manipulation")
    assert 0.0 <= conf <= 1.0
    assert conf == 0.8251

    # Edge cases
    assert calculate_confidence({}, "Any") == 0.0


def test_risk_score_normal_text():
    probs = {cat: 0.02 for cat in CATEGORY_NAMES}
    probs["Normal / No Significant Manipulation"] = 0.88
    
    score, level = calculate_risk_score(
        predicted_category="Normal / No Significant Manipulation",
        confidence=0.88,
        probabilities=probs,
        indicators=[]
    )
    assert 0 <= score <= 39
    assert level == "Low"


def test_risk_score_severe_manipulation():
    probs = {cat: 0.01 for cat in CATEGORY_NAMES}
    probs["Deceptive Persuasion"] = 0.94
    
    indicators = [
        DetectedIndicator(
            name="Fabricated Authority",
            matched_phrase="CEO personally instructed",
            category_relevance="Deceptive Persuasion",
            description="Fabricated authority marker"
        ),
        DetectedIndicator(
            name="Unverifiable Guarantee",
            matched_phrase="100% risk-free",
            category_relevance="Deceptive Persuasion",
            description="Absolute promise"
        )
    ]
    
    score, level = calculate_risk_score(
        predicted_category="Deceptive Persuasion",
        confidence=0.94,
        probabilities=probs,
        indicators=indicators
    )
    assert 70 <= score <= 100
    assert level == "High"
