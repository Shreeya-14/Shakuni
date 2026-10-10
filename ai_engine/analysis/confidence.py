"""Confidence score calculation for Shakuni.

Calculates the statistical confidence associated with the model's pattern classification.
Importantly, model confidence reflects the classifier's posterior certainty over its
learned feature distributions; it does NOT represent factual truthfulness or the moral
character of the text's author.
"""

from typing import Dict

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"
NO_MANIPULATION_NAME = "No significant manipulation detected"
INSUFFICIENT_EVIDENCE_NAME = "Insufficient evidence to classify"


def calculate_confidence(probabilities: Dict[str, float], predicted_category: str) -> float:
    """Calculate and normalize classification confidence.
    
    Args:
        probabilities: Dictionary of category names to probability floats (0.0 - 1.0).
        predicted_category: The predicted category or uncertainty outcome.
        
    Returns:
        Confidence score rounded to 4 decimal places (0.0 to 1.0).
    """
    if not probabilities:
        return 0.0

    if predicted_category in probabilities:
        raw_confidence = probabilities[predicted_category]
    elif predicted_category == NO_MANIPULATION_NAME:
        prob_norm = probabilities.get(NORMAL_CATEGORY_NAME, 0.0)
        max_other = max([p for cat, p in probabilities.items() if cat != NORMAL_CATEGORY_NAME], default=0.0)
        raw_confidence = max(prob_norm, round(1.0 - max_other, 4))
    elif predicted_category == INSUFFICIENT_EVIDENCE_NAME:
        raw_confidence = max(probabilities.values(), default=0.0)
    else:
        raw_confidence = max(probabilities.values(), default=0.0)

    # Ensure confidence stays strictly within [0.0, 1.0]
    normalized_conf = max(0.0, min(1.0, float(raw_confidence)))
    return round(normalized_conf, 4)
