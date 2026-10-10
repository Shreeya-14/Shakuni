"""Tests for ML Classifier."""

import os
from ai_engine.classifier.classifier import ShakuniClassifier, clean_text
from ai_engine.classifier.categories import CATEGORY_NAMES, ALL_OUTCOME_NAMES, NORMAL_CATEGORY_NAME, NO_MANIPULATION_DETECTED


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
    if classifier.model_type == "distilbert":
        assert classifier.tokenizer is not None
    else:
        assert classifier.vectorizer is not None


def test_classifier_predict_valid_category():
    classifier = ShakuniClassifier()
    sample = "The weekly staff meeting will be held in the main conference room on Monday."
    cat, conf, probs = classifier.predict(sample)
    
    assert cat in ALL_OUTCOME_NAMES
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
        "Everyone else has already signed the loyalty agreement, don't be the lone holdout."
    ]
    results = classifier.batch_predict(texts)
    assert len(results) == 2
    for cat, conf, probs in results:
        assert cat in ALL_OUTCOME_NAMES
        assert 0.0 <= conf <= 1.0


def test_classifier_regression_cases():
    classifier = ShakuniClassifier()
    # Meeting announcement must be classified as Normal
    cat, conf, _ = classifier.predict("There is a meeting tomorrow.")
    assert cat in [NORMAL_CATEGORY_NAME, NO_MANIPULATION_DETECTED]
    assert conf >= 0.50

    # Coercive threat must be classified as Emotional Pressure
    threat_cat, _, _ = classifier.predict("You must agree with me, or I will make sure you regret it.")
    assert threat_cat == "Emotional Pressure"


def test_tfidf_backend_fallback():
    # Verify TF-IDF backend functions when explicitly requested
    classifier = ShakuniClassifier()
    classifier.model_type = "tfidf"
    import joblib
    classifier.model = joblib.load(classifier.model_path)
    classifier.vectorizer = joblib.load(classifier.vectorizer_path)
    
    cat, conf, probs = classifier.predict("There is a meeting tomorrow.")
    assert cat in ALL_OUTCOME_NAMES
    assert len(probs) == 7
