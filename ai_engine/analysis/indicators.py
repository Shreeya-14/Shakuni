"""Linguistic indicator detection for Shakuni.

Extracts potential communication pattern markers and persuasive rhetoric indicators.
Note: Detected indicators represent rhetorical and linguistic patterns; they are not
definitive proof of subjective intent or objective falsehood.
"""

import re
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class DetectedIndicator(BaseModel):
    name: str = Field(..., description="Name of the detected linguistic indicator")
    matched_phrase: str = Field(..., description="Specific text phrase that matched the pattern")
    category_relevance: str = Field(..., description="Category this indicator typically correlates with")
    description: str = Field(..., description="Explanation of why this indicator is significant")


# Pattern dictionary mapping regex rules to indicator definitions
INDICATOR_RULES = [
    {
        "name": "Social Conformity Demand",
        "pattern": r"\b(everyone else|everyone on the|all the other|all your colleagues|nobody questions|entire team|whole office|breaking ranks|lone dissenter|unanimous)\b",
        "category_relevance": "Social Pressure",
        "description": "Appeals to group consensus or highlights the target's deviation from peer behavior."
    },
    {
        "name": "Fear of Professional Ostracization",
        "pattern": r"\b(alienate|isolate|damage your credibility|ruin your standing|look amateurish|look insubordinate|let the team down|holding us back)\b",
        "category_relevance": "Social Pressure",
        "description": "Warns of reputational damage, social isolation, or peer judgment for non-compliance."
    },
    {
        "name": "Guilt-Inducing Appeal",
        "pattern": r"\b(if you really (cared|loved)|sacrificed (everything|my own)|breaking (my|your mother's) heart|cold indifference|shatter the confidence|betray(ed)? my trust|on your conscience)\b",
        "category_relevance": "Emotional Pressure",
        "description": "Appeals to moral debt, perceived emotional harm, or interpersonal guilt to compel agreement."
    },
    {
        "name": "Urgency and Catastrophic Consequence",
        "pattern": r"\b(right this minute|immediately|before it closes|catastrophic|irreversible tragedy|ruin my life|nowhere else to turn|brink of collapse)\b",
        "category_relevance": "Emotional Pressure",
        "description": "Constructs intense temporal panic and dramatizes potential negative outcomes."
    },
    {
        "name": "False Dichotomy (Either/Or)",
        "pattern": r"\b(either (you|we|choose)|or you (want|are|actively)|between total|or total)\b",
        "category_relevance": "Misleading Framing",
        "description": "Artificially reduces a complex situation to two extreme, mutually exclusive options."
    },
    {
        "name": "Euphemistic Recontextualization",
        "pattern": r"\b(rightsizing|operational synergies|informational hygiene|asset stewardship|value-add investment|ambient intelligence|recalibration)\b",
        "category_relevance": "Misleading Framing",
        "description": "Substitutes sanitized corporate or ideological terms for negative realities like layoffs or price hikes."
    },
    {
        "name": "Selective Statistical Assertion",
        "pattern": r"\b(\b\d{1,3}%\b|hundred percent|four hundred percent|doubled their|record|unprecedented|outperformed|zero adverse)\b",
        "category_relevance": "Selective Information",
        "description": "Cites prominent quantitative metrics or dramatic percentage gains without full methodological context."
    },
    {
        "name": "Isolated Favorable Testimonial",
        "pattern": r"\b(every (single )?customer|all doctors|independent reviews praised|testimonials from|select pilot group|readers of our)\b",
        "category_relevance": "Selective Information",
        "description": "Highlights curated positive anecdotes while systematically omitting broader sample variance."
    },
    {
        "name": "Unconditional Free/Discount Claim",
        "pattern": r"\b(completely free|zero downtime|no upfront|complimentary|instant account|guarantees the lowest|free of charge)\b",
        "category_relevance": "Information Withholding",
        "description": "Emphasizes zero-cost access while obscuring subsequent contractual lock-in, renewal terms, or caveats."
    },
    {
        "name": "Omission of Material Conditions",
        "pattern": r"\b(simply click|just click agree|effortless|fixed low monthly|automatic(ally)? without|pre-selected)\b",
        "category_relevance": "Information Withholding",
        "description": "Downplays procedural gravity and minimizes the appearance of contractual terms or obligations."
    },
    {
        "name": "Fabricated or Unverified Authority",
        "pattern": r"\b(ceo (personally )?instructed|secret(ly)? (approved|voted|promised)|authorized legal investigator|internal confidential|classified directive|supreme court clerk)\b",
        "category_relevance": "Deceptive Persuasion",
        "description": "Invokes unseen high-level authority or privileged sources to deter verification."
    },
    {
        "name": "Unverifiable Guarantee of Risk-Free Benefit",
        "pattern": r"\b(guarantees? (an? )?(annualized|risk-free|100%|one hundred percent)|cured every|completely unbreakable|immune to litigation|flawless precision)\b",
        "category_relevance": "Deceptive Persuasion",
        "description": "Makes absolute promises of risk elimination or infallible performance."
    }
]


def detect_indicators(text: str) -> List[DetectedIndicator]:
    """Scan text for rhetorical and linguistic manipulation markers."""
    detected = []
    seen_names = set()
    text_lower = text.lower()

    for rule in INDICATOR_RULES:
        matches = re.finditer(rule["pattern"], text_lower, re.IGNORECASE)
        for match in matches:
            matched_text = match.group(0)
            if rule["name"] not in seen_names:
                detected.append(DetectedIndicator(
                    name=rule["name"],
                    matched_phrase=matched_text,
                    category_relevance=rule["category_relevance"],
                    description=rule["description"]
                ))
                seen_names.add(rule["name"])
                break  # Record each indicator pattern type once per text

    return detected
