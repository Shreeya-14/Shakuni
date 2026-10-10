"""Tests for Deep Linguistic & Style Reasoning Engine."""

from ai_engine.analysis.linguistic_engine import (
    get_linguistic_engine,
    LinguisticStyle,
    LocalLinguisticReasoner
)
from ai_engine.analyzer import get_analyzer


def test_local_linguistic_reasoner_neutral():
    reasoner = LocalLinguisticReasoner()
    result = reasoner.analyze("There is a meeting tomorrow at 10 AM.", category="Normal")
    
    assert isinstance(result, LinguisticStyle)
    assert "Objective" in result.tone or "Neutral" in result.tone
    assert result.emotional_temperature in ["Calm / Neutral"]
    assert "No covert psychological leverage" in result.hidden_subtext or "no apparent psychological pressure" in result.hidden_subtext.lower() or "no manipulation" in str(result.rhetorical_devices).lower()
    assert result.model_provider is not None


def test_local_linguistic_reasoner_guilt():
    reasoner = LocalLinguisticReasoner()
    result = reasoner.analyze(
        "If you really loved our family and cared about our happiness, you wouldn't take that job.",
        category="Emotional Pressure"
    )
    
    assert isinstance(result, LinguisticStyle)
    assert "Guilt" in result.tone or "Emotional" in result.tone
    assert result.emotional_temperature in ["Heated / Manipulative"]
    assert "guilt" in result.hidden_subtext.lower() or "emotional" in result.hidden_subtext.lower()
    assert len(result.rhetorical_devices) > 0
    assert len(result.recommended_response) > 0


def test_analyzer_returns_style_analysis():
    analyzer = get_analyzer()
    result = analyzer.analyze("Everyone on the team agreed; don't be the lone dissenter holding us back.")
    
    assert result.style_analysis is not None
    assert isinstance(result.style_analysis.tone, str)
    assert isinstance(result.style_analysis.surface_meaning, str)
    assert isinstance(result.style_analysis.hidden_subtext, str)
    assert isinstance(result.style_analysis.rhetorical_devices, list)
    assert isinstance(result.style_analysis.recommended_response, str)
