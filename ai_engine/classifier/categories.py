"""Centralized Category Definitions for Shakuni.

Defines the 7 manipulation and persuasion pattern categories to prevent duplication
across the AI engine, backend API, schemas, and documentation.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class CategoryDefinition(BaseModel):
    id: str = Field(..., description="Machine-readable identifier")
    name: str = Field(..., description="Canonical category name")
    description: str = Field(..., description="Formal description of the communication pattern")
    examples: List[str] = Field(..., description="Representative examples of the pattern")
    typical_linguistic_indicators: List[str] = Field(..., description="Key linguistic markers associated with the pattern")
    risk_interpretation: str = Field(..., description="Qualitative interpretation of potential risk")
    base_risk_weight: float = Field(..., ge=0.0, le=100.0, description="Baseline risk score weight (0-100)")


MANIPULATION_CATEGORIES: Dict[str, CategoryDefinition] = {
    "Normal / No Significant Manipulation": CategoryDefinition(
        id="normal",
        name="Normal / No Significant Manipulation",
        description="Standard, neutral, objective, or transparent communication exhibiting no significant coercive, deceptive, or manipulative tactics.",
        examples=[
            "The project status report will be sent to the team on Friday after final code review.",
            "Our quarterly earnings grew by 4.2% driven by international hardware sales.",
            "Please review the attached meeting minutes and let me know if any points require clarification."
        ],
        typical_linguistic_indicators=[
            "objective tone",
            "factual assertions",
            "unforced conditional statements",
            "balanced presentation",
            "clear attribution"
        ],
        risk_interpretation="Minimal risk of undue influence. Text presents information neutrally without emotional or social coercion.",
        base_risk_weight=10.0
    ),
    "Social Pressure": CategoryDefinition(
        id="social_pressure",
        name="Social Pressure",
        description="Communication that leverages bandwagon appeals, peer conformity, social shaming, consensus coercion, or fear of ostracization.",
        examples=[
            "Everyone else in the department has already agreed to the new policy, don't be the only one holding us back.",
            "Any reasonable team member would support this without questioning management.",
            "All the top industry leaders have adopted this standard; you risk looking incompetent if you do not."
        ],
        typical_linguistic_indicators=[
            "bandwagon appeals",
            "consensus claims",
            "conformity enforcement",
            "fear of exclusion",
            "in-group vs out-group framing"
        ],
        risk_interpretation="Moderate to high risk. Pressures recipient to yield to perceived group norms rather than rational evaluation.",
        base_risk_weight=65.0
    ),
    "Emotional Pressure": CategoryDefinition(
        id="emotional_pressure",
        name="Emotional Pressure",
        description="Communication relying on guilt trips, fear appeals, affective blackmail, urgency panic, or sympathy exploitation to force compliance.",
        examples=[
            "If you truly cared about the future of our team, you would sacrifice your weekend to finish this.",
            "I've sacrificed everything for this project, and if it fails, it will completely ruin my life.",
            "Act right now or catastrophic consequences will occur before tomorrow morning."
        ],
        typical_linguistic_indicators=[
            "guilt-inducing wording",
            "emotional consequence",
            "urgency panic",
            "fear appeals",
            "affective obligation"
        ],
        risk_interpretation="High risk. Bypasses critical evaluation by provoking acute distress, guilt, or fear.",
        base_risk_weight=72.0
    ),
    "Misleading Framing": CategoryDefinition(
        id="misleading_framing",
        name="Misleading Framing",
        description="Presents information with biased context, false dichotomies, loaded terminology, or slanted narrative structures to skew perception.",
        examples=[
            "You are either with our aggressive modernization plan, or you want this organization to crumble into obsolescence.",
            "This minor procedural adjustment simply harmonizes operational synergies (hiding mass layoffs).",
            "Our competitors' reckless experimentation proves our traditional lock-in model is the only safe harbor."
        ],
        typical_linguistic_indicators=[
            "false dichotomy",
            "loaded terminology",
            "euphemistic recontextualization",
            "presupposition traps",
            "biased perspective anchoring"
        ],
        risk_interpretation="Moderate to high risk. Distorts decision space by artificially constraining choices and slanting reality.",
        base_risk_weight=60.0
    ),
    "Selective Information": CategoryDefinition(
        id="selective_information",
        name="Selective Information",
        description="Cherry-picks favorable facts, isolated statistics, or one-sided testimonies while systematically ignoring counter-evidence.",
        examples=[
            "Our product delivered a 300% performance surge in benchmark tests (ignoring battery drain and crashes).",
            "Customer satisfaction reached 99% among respondents who opted into our loyalty survey.",
            "Only positive case studies were highlighted in the investment prospectus while omitting failed trials."
        ],
        typical_linguistic_indicators=[
            "cherry-picked statistics",
            "omission of counter-evidence",
            "one-sided testimonials",
            "unqualified superlative claims",
            "favorable segment isolation"
        ],
        risk_interpretation="Moderate risk. Misguides judgment by presenting genuine but incomplete facts that paint a deceptive overall picture.",
        base_risk_weight=52.0
    ),
    "Information Withholding": CategoryDefinition(
        id="information_withholding",
        name="Information Withholding",
        description="Strategically conceals crucial caveats, hidden costs, adverse consequences, conflict of interest, or relevant context to prevent informed consent.",
        examples=[
            "The subscription is completely free for the initial trial period (without mentioning the non-cancellable auto-renewal clause).",
            "The system update is ready to install; restart now to continue (hiding that it deprecates core user features).",
            "We finalized the contractual terms yesterday (omitting that regulatory penalties apply to delays)."
        ],
        typical_linguistic_indicators=[
            "conspicuous vagueness",
            "buried caveats",
            "absence of terms/conditions",
            "incomplete disclosures",
            "silence on material drawbacks"
        ],
        risk_interpretation="High risk. Undermines autonomy by preventing the recipient from knowing critical decision-altering facts.",
        base_risk_weight=75.0
    ),
    "Deceptive Persuasion": CategoryDefinition(
        id="deceptive_persuasion",
        name="Deceptive Persuasion",
        description="Active construction of false narratives, fabricated authority, deliberate deception techniques, disingenuous promises, or multi-layered pretexting.",
        examples=[
            "Internal auditors have already pre-approved this entire transaction, so you can execute the transfer immediately without waiting.",
            "Our patent-pending quantum algorithm guarantees 100% risk-free returns under all market conditions.",
            "I spoke directly with the CEO this morning and she instructed us to bypass normal compliance checks for this deal."
        ],
        typical_linguistic_indicators=[
            "fabricated authority",
            "unverifiable guarantees",
            "pretextual urgency",
            "fraudulent assurance",
            "calculated misrepresentation"
        ],
        risk_interpretation="Severe risk. Employs sophisticated, multi-layered stratagems designed to actively mislead the target.",
        base_risk_weight=88.0
    )
}

CATEGORY_NAMES: List[str] = list(MANIPULATION_CATEGORIES.keys())


def get_all_categories() -> List[CategoryDefinition]:
    """Return all defined manipulation categories."""
    return list(MANIPULATION_CATEGORIES.values())


def get_category_by_name(name: str) -> Optional[CategoryDefinition]:
    """Retrieve category definition by canonical name."""
    return MANIPULATION_CATEGORIES.get(name)


def get_category_by_id(cat_id: str) -> Optional[CategoryDefinition]:
    """Retrieve category definition by machine-readable ID."""
    for cat in MANIPULATION_CATEGORIES.values():
        if cat.id == cat_id:
            return cat
    return None
