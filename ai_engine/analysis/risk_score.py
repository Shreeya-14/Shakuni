"""Transparent Risk Scoring Engine for Shakuni.

Calculates an explainable risk score (0-100) and risk level (Low, Moderate, High).
The risk score estimates the potential presence and intensity of strategic deception
or manipulative communication patterns in the analyzed text.

It is NOT an index of personal dishonesty or a lie detection score.
"""

from typing import Dict, List, Tuple
from ai_engine.classifier.categories import get_category_by_name
from ai_engine.analysis.indicators import DetectedIndicator

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"


def calculate_risk_score(
    predicted_category: str,
    confidence: float,
    probabilities: Dict[str, float],
    indicators: List[DetectedIndicator]
) -> Tuple[int, str]:
    """Calculate the explainable risk score (0-100) and corresponding risk level.
    
    Formula components:
    1. Base Category Risk (W_cat):
       Retrieved from centralized category definitions (0 to 100).
    2. Manipulation Mass Probability (P_manip):
       Sum of probabilities of all non-Normal categories:
       P_manip = 1.0 - P(Normal)
    3. Indicator Density Modifier (I_mod):
       +4 points for each detected indicator matching the predicted category,
       +2 points for each other detected indicator (capped at 20 points).
    4. Composite Score:
       If predicted category is Normal:
         Risk is anchored low: Score = (W_cat * 0.5) + (P_manip * 25) + min(I_mod, 10)
       If predicted category is Manipulative:
         Score = (W_cat * 0.45) + (P_manip * 35) + (confidence * 10) + I_mod
         
    Scale:
      0 - 39: Low
      40 - 69: Moderate
      70 - 100: High
    """
    cat_def = get_category_by_name(predicted_category)
    base_weight = cat_def.base_risk_weight if cat_def else 30.0

    # Calculate probability mass assigned to non-normal categories
    prob_normal = probabilities.get(NORMAL_CATEGORY_NAME, 0.0)
    p_manip = max(0.0, 1.0 - prob_normal)

    # Indicator bonus
    indicator_score = 0.0
    for ind in indicators:
        if ind.category_relevance == predicted_category:
            indicator_score += 4.0
        else:
            indicator_score += 2.0
    indicator_score = min(indicator_score, 20.0)

    # Score calculation
    if predicted_category == NORMAL_CATEGORY_NAME:
        raw_score = (base_weight * 0.5) + (p_manip * 20.0) + min(indicator_score, 8.0)
    else:
        raw_score = (base_weight * 0.45) + (p_manip * 30.0) + (confidence * 12.0) + indicator_score

    # Clamp to [0, 100] and round to integer
    risk_score = int(round(max(0.0, min(100.0, raw_score))))

    # Determine risk level
    if risk_score < 40:
        risk_level = "Low"
    elif risk_score < 70:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return risk_score, risk_level
