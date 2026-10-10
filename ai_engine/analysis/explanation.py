"""Explanation Generator for Shakuni.

Constructs transparent, human-readable explanations synthesizing the ML classification,
detected linguistic markers, contextual limitations, and qualitative risk interpretation.
Adheres strictly to research guidelines avoiding subjective intent or absolute truth claims.
"""

from typing import List, Optional
from ai_engine.classifier.categories import (
    get_category_by_name,
    INSUFFICIENT_EVIDENCE,
    NO_MANIPULATION_DETECTED
)
from ai_engine.analysis.indicators import DetectedIndicator

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"


def generate_explanation(
    category: str,
    confidence: float,
    indicators: List[DetectedIndicator],
    text: Optional[str] = None
) -> str:
    """Generate an accessible, ethical, and context-aware explanation."""
    conf_pct = int(round(confidence * 100))
    cat_def = get_category_by_name(category)

    # 1. Normal Communication
    if category == NORMAL_CATEGORY_NAME:
        if not indicators:
            return (
                f"The text exhibits standard, objective communication patterns (model certainty: {conf_pct}%). "
                "No significant persuasive coercion, deceptive framing, or emotional pressure indicators were identified. "
                "The statement appears consistent with routine informational discourse."
            )
        else:
            ind_names = ", ".join([f"'{ind.name}'" for ind in indicators[:2]])
            return (
                f"The text is predominantly classified as normal/neutral communication ({conf_pct}% certainty). "
                f"While minor stylistic markers ({ind_names}) were observed, they reflect routine expression rather than strategic manipulation."
            )

    # 2. No Significant Manipulation Detected (Calibrated Rejection of Weak Signals)
    if category == NO_MANIPULATION_DETECTED:
        return (
            f"No significant manipulation detected (model certainty: {conf_pct}%). "
            "Although minor rhetorical phrasing may be present, the overall text does not meet the statistical threshold "
            "for deceptive, coercive, or manipulative communication patterns. This statement is interpreted as ordinary informational dialogue."
        )

    # 3. Insufficient Evidence to Classify (High Entropy / Ambiguity Rejection)
    if category == INSUFFICIENT_EVIDENCE:
        return (
            f"Insufficient evidence to classify (statistical certainty: {conf_pct}%). "
            "The linguistic patterns in the submitted text are diffuse or ambiguous across multiple categories. "
            "The system rejects assigning a specific manipulation label to prevent false accusations when evidence is inconclusive."
        )

    # 4. Confirmed Manipulative Categories
    explanation_parts = []

    # Category descriptor
    cat_desc = cat_def.description if cat_def else "Communication pattern identified by statistical features."
    explanation_parts.append(
        f"The communication pattern was classified as '{category}' with an estimated model certainty of {conf_pct}%."
    )
    explanation_parts.append(f"Pattern characteristics: {cat_desc}")

    # Indicator synthesis
    relevant_inds = [ind for ind in indicators if ind.category_relevance == category]
    other_inds = [ind for ind in indicators if ind.category_relevance != category]

    if relevant_inds:
        phrases = [f"'{ind.matched_phrase}' ({ind.name})" for ind in relevant_inds[:3]]
        explanation_parts.append(
            f"Observable rhetorical indicators detected in the text include: {', '.join(phrases)}."
        )
    elif other_inds:
        phrases = [f"'{ind.matched_phrase}' ({ind.name})" for ind in other_inds[:2]]
        explanation_parts.append(
            f"Supplementary rhetorical markers detected: {', '.join(phrases)}."
        )
    else:
        explanation_parts.append(
            "Classification is driven by semantic and contextual representation within the language model, without overt single-word trigger matches."
        )

    # 5. Context caveats for Selective Information and Information Withholding
    if category in ["Selective Information", "Information Withholding"] and not relevant_inds:
        explanation_parts.append(
            "Contextual limitation: Evaluating whether material facts were selectively omitted or withheld in an isolated single statement "
            "inherently requires extrinsic comparative context (e.g., source documents, disclosure requirements, or full conversational history). "
            "This assessment reflects lexical similarity to known omission patterns rather than proof of missing data."
        )

    # 6. Ethical research reminder
    explanation_parts.append(
        "Note: This analysis reflects an algorithmic evaluation of observable language patterns. "
        "It does not evaluate hidden personal intentions, moral character, or factual truthfulness."
    )

    return " ".join(explanation_parts)
