"""Confidence score calculation for Shakuni.

Calculates the statistical confidence associated with the model's pattern classification.
Importantly, model confidence reflects the classifier's posterior certainty over its
learned feature distributions; it does NOT represent factual truthfulness or the moral
character of the text's author.
"""

from typing import Dict


def calculate_confidence(probabilities: Dict[str, float], predicted_category: str) -> float:
    """Calculate and normalize classification confidence.
    
    Args:
        probabilities: Dictionary of category names to probability floats (0.0 - 1.0).
        predicted_category: The top predicted category name.
        
    Returns:
        Confidence score rounded to 4 decimal places (0.0 to 1.0).
    """
    if not probabilities:
        return 0.0
    
    raw_confidence = probabilities.get(predicted_category, 0.0)
    
    # Ensure confidence stays strictly within [0.0, 1.0]
    normalized_conf = max(0.0, min(1.0, float(raw_confidence)))
    return round(normalized_conf, 4)
