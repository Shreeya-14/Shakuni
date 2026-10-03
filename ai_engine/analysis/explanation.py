"""Explanation Generator for Shakuni.

Constructs transparent, human-readable explanations synthesizing the ML classification,
detected linguistic markers, and qualitative risk interpretation.
Adheres strictly to research guidelines avoiding absolute truth claims.
"""

from typing import List
from ai_engine.classifier.categories import get_category_by_name
from ai_engine.analysis.indicators import DetectedIndicator

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"


def generate_explanation(
    category: str,
    confidence: float,
    indicators: List[DetectedIndicator]
) -> str:
    """Generate an accessible, ethical, and context-aware explanation."""
    cat_def = get_category_by_name(category)
    cat_desc = cat_def.description if cat_def else "Communication pattern identified by statistical features."
    
    conf_pct = int(round(confidence * 100))

    if category == NORMAL_CATEGORY_NAME:
        if not indicators:
            return (
                f"The text exhibits standard, objective communication patterns (model certainty: {conf_pct}%). "
                "No significant persuasive coercion, deceptive framing, or emotional pressure indicators were identified."
            )
        else:
            ind_names = ", ".join([f"'{ind.name}'" for ind in indicators[:2]])
            return (
                f"The text is predominantly classified as neutral/normal communication ({conf_pct}% certainty). "
                f"While minor stylistic markers ({ind_names}) were observed, they appear consistent with routine expression."
            )

    # For manipulative/persuasive categories
    explanation_parts = []
    
    # 1. Primary statement
    explanation_parts.append(
        f"The communication pattern was classified as '{category}' with an estimated model certainty of {conf_pct}%."
    )
    
    # 2. Category rationale
    explanation_parts.append(
        f"This pattern typically involves: {cat_desc}"
    )

    # 3. Indicator synthesis
    relevant_inds = [ind for ind in indicators if ind.category_relevance == category]
    other_inds = [ind for ind in indicators if ind.category_relevance != category]
    
    if relevant_inds:
        phrases = [f"'{ind.matched_phrase}' ({ind.name})" for ind in relevant_inds[:3]]
        explanation_parts.append(
            f"Key rhetorical markers detected include: {', '.join(phrases)}."
        )
    elif other_inds:
        phrases = [f"'{ind.matched_phrase}' ({ind.name})" for ind in other_inds[:2]]
        explanation_parts.append(
            f"Supplementary rhetorical indicators detected: {', '.join(phrases)}."
        )
    else:
        explanation_parts.append(
            "Classification is driven primarily by lexical and semantic n-gram feature similarity within the trained model."
        )

    # 4. Probabilistic research note
    explanation_parts.append(
        "Note: This reflects an algorithmic pattern assessment and does not constitute a definitive judgment of intent."
    )

    return " ".join(explanation_parts)
