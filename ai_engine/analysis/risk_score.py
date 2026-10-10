"""Transparent Risk Scoring Engine for Shakuni.

Calculates an explainable risk score (0-100) and risk level (Low, Moderate, High).
The risk score estimates the potential rhetorical intensity and coercive impact of
observed communication patterns.

Important distinction:
- Model confidence reflects the statistical certainty over the learned linguistic pattern.
- Risk score evaluates the potential manipulative severity and coercive force of the detected pattern.
- Uncertainty or lack of evidence NEVER manufactures an elevated risk score.
"""

from typing import Dict, List, Tuple
from ai_engine.classifier.categories import get_category_by_name
from ai_engine.analysis.indicators import DetectedIndicator

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"
NO_MANIPULATION_NAME = "No significant manipulation detected"
INSUFFICIENT_EVIDENCE_NAME = "Insufficient evidence to classify"

NON_MANIPULATIVE_OUTCOMES = {
    NORMAL_CATEGORY_NAME,
    NO_MANIPULATION_NAME,
    INSUFFICIENT_EVIDENCE_NAME
}


def calculate_risk_score(
    predicted_category: str,
    confidence: float,
    probabilities: Dict[str, float],
    indicators: List[DetectedIndicator]
) -> Tuple[int, str]:
    """Calculate transparent risk score (0-100) and risk tier (Low, Moderate, High).
    
    Principles:
    1. Neutral & Uncertain Outcomes:
       Strictly anchored in the Low risk tier (0 - 25).
       A low-confidence or ambiguous prediction does NOT penalize the user with a high risk score.
    2. Confirmed Manipulation Outcomes:
       Combines normalized category severity (W_cat), pattern confidence, and observable
       linguistic indicators.
       If zero observable indicators are matched in the text, risk is tempered (capped at 65).
    """
    # 1. Non-manipulative or uncertain outcomes
    if predicted_category in NON_MANIPULATIVE_OUTCOMES:
        prob_normal = probabilities.get(NORMAL_CATEGORY_NAME, 0.0) if probabilities else 0.5
        residual_manip_mass = max(0.0, 1.0 - prob_normal)

        # Baseline: 5 for normal, 8 for no manipulation detected, 12 for insufficient evidence
        if predicted_category == NORMAL_CATEGORY_NAME:
            base_score = 5.0
        elif predicted_category == NO_MANIPULATION_NAME:
            base_score = 8.0
        else:
            base_score = 12.0

        indicator_bonus = min(float(len(indicators)) * 2.0, 6.0)
        raw_score = base_score + (residual_manip_mass * 8.0) + indicator_bonus
        final_score = int(round(max(0.0, min(25.0, raw_score))))
        return final_score, "Low"

    # 2. Confirmed manipulative categories
    cat_def = get_category_by_name(predicted_category)
    base_weight = cat_def.base_risk_weight if cat_def else 60.0

    # Pattern intensity: product of base category severity and calibrated confidence
    # Normalized so confidence=1.0 scales base_weight directly
    pattern_intensity = (base_weight * 0.55) * max(0.40, min(1.0, float(confidence)))

    # Indicator bonus: reward specifically matched markers
    matching_inds = [ind for ind in indicators if ind.category_relevance == predicted_category]
    other_inds = [ind for ind in indicators if ind.category_relevance != predicted_category]

    indicator_bonus = (len(matching_inds) * 8.0) + (len(other_inds) * 3.0)
    indicator_bonus = min(indicator_bonus, 25.0)

    # Base baseline contribution
    raw_score = 15.0 + pattern_intensity + indicator_bonus

    # If zero indicators matched in the observable text, cap score at 65 (moderate risk)
    # to avoid extreme threat claims based purely on statistical n-gram similarity
    if len(matching_inds) == 0:
        raw_score = min(raw_score, 65.0)

    # Clamp to [0, 100]
    risk_score = int(round(max(0.0, min(100.0, raw_score))))

    # Determine qualitative risk tier
    if risk_score < 40:
        risk_level = "Low"
    elif risk_score < 70:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    return risk_score, risk_level
