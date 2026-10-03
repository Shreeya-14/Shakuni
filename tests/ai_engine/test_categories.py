"""Tests for centralized category definitions."""

from ai_engine.classifier.categories import (
    MANIPULATION_CATEGORIES,
    CATEGORY_NAMES,
    get_all_categories,
    get_category_by_name,
    get_category_by_id
)


def test_category_definitions_count():
    assert len(MANIPULATION_CATEGORIES) == 7
    assert len(CATEGORY_NAMES) == 7


def test_required_category_presence():
    expected_categories = [
        "Normal / No Significant Manipulation",
        "Social Pressure",
        "Emotional Pressure",
        "Misleading Framing",
        "Selective Information",
        "Information Withholding",
        "Deceptive Persuasion"
    ]
    for expected in expected_categories:
        assert expected in MANIPULATION_CATEGORIES
        cat = get_category_by_name(expected)
        assert cat is not None
        assert cat.name == expected
        assert len(cat.description) > 0
        assert len(cat.examples) >= 2
        assert len(cat.typical_linguistic_indicators) >= 2
        assert 0.0 <= cat.base_risk_weight <= 100.0


def test_get_category_by_id():
    cat = get_category_by_id("deceptive_persuasion")
    assert cat is not None
    assert cat.name == "Deceptive Persuasion"

    non_existent = get_category_by_id("non_existent_category")
    assert non_existent is None
