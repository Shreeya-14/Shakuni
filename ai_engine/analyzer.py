"""Unified Analysis Engine for Shakuni.

Acts as the primary orchestrator connecting ML inference, linguistic indicator detection,
confidence estimation, transparent risk scoring, and narrative explanation generation.
"""

from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field

from ai_engine.classifier.classifier import get_classifier, clean_text
from ai_engine.analysis.indicators import detect_indicators, DetectedIndicator
from ai_engine.analysis.confidence import calculate_confidence
from ai_engine.analysis.risk_score import calculate_risk_score
from ai_engine.analysis.explanation import generate_explanation
from ai_engine.analysis.linguistic_engine import LinguisticStyle, get_linguistic_engine


class AnalysisResult(BaseModel):
    """Structured response model for text manipulation analysis."""
    text: str = Field(..., description="The original submitted text")
    category: str = Field(..., description="Identified manipulation pattern category or uncertainty outcome")
    risk_score: int = Field(..., ge=0, le=100, description="Estimated pattern intensity score (0-100)")
    risk_level: str = Field(..., description="Qualitative risk tier: Low, Moderate, or High")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Model statistical confidence (0.0-1.0)")
    explanation: str = Field(..., description="Human-readable rationale and interpretation")
    indicators: List[DetectedIndicator] = Field(default_factory=list, description="List of detected linguistic markers")
    probabilities: Dict[str, float] = Field(..., description="Posterior probability distribution across all 7 categories")
    style_analysis: Optional[LinguisticStyle] = Field(None, description="Deep speaking and writing style discourse breakdown")


class ShakuniAnalyzer:
    """Core analysis facade coordinating NLP inference, discourse reasoning, and contextual intelligence."""

    def __init__(self):
        self.classifier = get_classifier()
        self.linguistic_engine = get_linguistic_engine()

    def analyze(
        self,
        text: str,
        engine: Optional[str] = None,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> AnalysisResult:
        """Perform end-to-end analysis on a single text string."""
        raw_text = text or ""
        cleaned = clean_text(raw_text)

        # 1. Linguistic indicator extraction
        indicators = detect_indicators(cleaned)

        # 2. Machine Learning category and probability prediction
        predicted_category, raw_conf, probabilities = self.classifier.predict(cleaned)

        # 3. Model confidence normalization
        confidence = calculate_confidence(probabilities, predicted_category)

        # 4. Transparent composite risk scoring
        risk_score, risk_level = calculate_risk_score(
            predicted_category=predicted_category,
            confidence=confidence,
            probabilities=probabilities,
            indicators=indicators
        )

        # 5. Narrative explanation generation
        explanation = generate_explanation(
            category=predicted_category,
            confidence=confidence,
            indicators=indicators,
            text=raw_text
        )

        # 6. Deep linguistic and style discourse analysis (ChatGPT/Gemini or Local Reasoner)
        style_analysis = self.linguistic_engine.analyze(
            text=raw_text,
            category=predicted_category,
            engine=engine,
            api_key=api_key,
            model_name=model_name
        )

        return AnalysisResult(
            text=raw_text,
            category=predicted_category,
            risk_score=risk_score,
            risk_level=risk_level,
            confidence=confidence,
            explanation=explanation,
            indicators=indicators,
            probabilities=probabilities,
            style_analysis=style_analysis
        )

    def batch_analyze(
        self,
        texts: List[str],
        engine: Optional[str] = None,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> List[AnalysisResult]:
        """Analyze a collection of text inputs using batched ML inference."""
        if not texts:
            return []

        raw_texts = [t or "" for t in texts]
        cleaned_texts = [clean_text(t) for t in raw_texts]

        # 1. Batch extract indicators
        all_indicators = [detect_indicators(c) for c in cleaned_texts]

        # 2. Optimized batch ML prediction
        predictions = self.classifier.batch_predict(cleaned_texts)

        results = []
        for raw_t, indicators, (predicted_category, raw_conf, probabilities) in zip(
            raw_texts, all_indicators, predictions
        ):
            confidence = calculate_confidence(probabilities, predicted_category)
            risk_score, risk_level = calculate_risk_score(
                predicted_category=predicted_category,
                confidence=confidence,
                probabilities=probabilities,
                indicators=indicators
            )
            explanation = generate_explanation(
                category=predicted_category,
                confidence=confidence,
                indicators=indicators,
                text=raw_t
            )
            style_analysis = self.linguistic_engine.analyze(
                text=raw_t,
                category=predicted_category,
                engine=engine,
                api_key=api_key,
                model_name=model_name
            )
            results.append(
                AnalysisResult(
                    text=raw_t,
                    category=predicted_category,
                    risk_score=risk_score,
                    risk_level=risk_level,
                    confidence=confidence,
                    explanation=explanation,
                    indicators=indicators,
                    probabilities=probabilities,
                    style_analysis=style_analysis
                )
            )
        return results


# Module-level helper
_global_analyzer: Optional[ShakuniAnalyzer] = None


def get_analyzer() -> ShakuniAnalyzer:
    """Retrieve or initialize the singleton ShakuniAnalyzer."""
    global _global_analyzer
    if _global_analyzer is None:
        _global_analyzer = ShakuniAnalyzer()
    return _global_analyzer
