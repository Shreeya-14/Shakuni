"""Tests for ML Classifier."""

from ai_engine.classifier.classifier import ShakuniClassifier, clean_text
from ai_engine.classifier.categories import CATEGORY_NAMES


def test_clean_text():
    raw = "  Hello   \n\n\t World!  "
    assert clean_text(raw) == "Hello World!"
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_classifier_loads():
    classifier = ShakuniClassifier()
    classifier.ensure_model_loaded()
    assert classifier.is_loaded is True
    assert classifier.model is not None
    assert classifier.vectorizer is not None


def test_classifier_predict_valid_category():
    classifier = ShakuniClassifier()
    sample = "The weekly staff meeting will be held in the main conference room on Monday."
    cat, conf, probs = classifier.predict(sample)
    
    assert cat in CATEGORY_NAMES
    assert 0.0 <= conf <= 1.0
    assert isinstance(probs, dict)
    assert len(probs) == 7
    
    # Check probability sum
    prob_sum = sum(probs.values())
    assert abs(prob_sum - 1.0) < 0.05


def test_classifier_batch_predict():
    classifier = ShakuniClassifier()
    texts = [
        "Normal operational report on database throughput.",
        "Everyone else has already signed the loyalty agreement."
    ]
    results = classifier.batch_predict(texts)
    assert len(results) == 2
    for cat, conf, probs in results:
        assert cat in CATEGORY_NAMES
        assert 0.0 <= conf <= 1.0
