"""Tests for the ShakuniAnalyzer unified facade."""

from ai_engine.analyzer import ShakuniAnalyzer, get_analyzer
from ai_engine.classifier.categories import CATEGORY_NAMES


def test_analyzer_singleton():
    analyzer1 = get_analyzer()
    analyzer2 = get_analyzer()
    assert analyzer1 is analyzer2


def test_analyze_output_contract():
    analyzer = get_analyzer()
    text = "The quarterly financial report will be distributed following the board meeting on Friday."
    result = analyzer.analyze(text)
    
    assert result.text == text
    assert result.category in CATEGORY_NAMES
    assert 0 <= result.risk_score <= 100
    assert result.risk_level in ["Low", "Moderate", "High"]
    assert 0.0 <= result.confidence <= 1.0
    assert len(result.explanation) > 0
    assert isinstance(result.indicators, list)
    assert isinstance(result.probabilities, dict)
    assert len(result.probabilities) == 7
    
    # Verify non-absolute wording in explanation
    assert "lying" not in result.explanation.lower()


def test_analyze_batch():
    analyzer = get_analyzer()
    texts = [
        "First regular sentence regarding server deployment.",
        "Either you sign this right now, or our company faces total devastation."
    ]
    results = analyzer.batch_analyze(texts)
    assert len(results) == 2
    for r in results:
        assert r.category in CATEGORY_NAMES
