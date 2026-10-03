"""Analysis service integrating AI Engine with backend API endpoints."""

from typing import List, Dict, Any
from ai_engine.analyzer import get_analyzer, AnalysisResult
from ai_engine.classifier.categories import get_all_categories, CategoryDefinition
from backend.app.schemas.analysis import (
    AnalysisResponse,
    BatchAnalysisResponse,
    DetectedIndicatorSchema,
    CategoryDetailSchema,
    CategoriesResponse
)


class AnalysisService:
    """Service handling text analysis orchestration and category introspection."""

    def __init__(self):
        self.analyzer = get_analyzer()

    def analyze_single(self, text: str) -> AnalysisResponse:
        """Run manipulation and deception pattern analysis on a single text."""
        result: AnalysisResult = self.analyzer.analyze(text)
        
        return AnalysisResponse(
            text=result.text,
            category=result.category,
            risk_score=result.risk_score,
            risk_level=result.risk_level,
            confidence=result.confidence,
            explanation=result.explanation,
            indicators=[
                DetectedIndicatorSchema(
                    name=ind.name,
                    matched_phrase=ind.matched_phrase,
                    category_relevance=ind.category_relevance,
                    description=ind.description
                )
                for ind in result.indicators
            ],
            probabilities=result.probabilities
        )

    def analyze_batch(self, texts: List[str]) -> BatchAnalysisResponse:
        """Run batch analysis over multiple texts."""
        results = [self.analyze_single(t) for t in texts]
        return BatchAnalysisResponse(
            total_analyzed=len(results),
            results=results
        )

    def get_supported_categories(self) -> CategoriesResponse:
        """Retrieve definitions for all 7 supported manipulation categories."""
        categories: List[CategoryDefinition] = get_all_categories()
        cat_schemas = [
            CategoryDetailSchema(
                id=c.id,
                name=c.name,
                description=c.description,
                examples=c.examples,
                typical_linguistic_indicators=c.typical_linguistic_indicators,
                risk_interpretation=c.risk_interpretation,
                base_risk_weight=c.base_risk_weight
            )
            for c in categories
        ]
        return CategoriesResponse(
            total_categories=len(cat_schemas),
            categories=cat_schemas
        )


_analysis_service_instance = None


def get_analysis_service() -> AnalysisService:
    """Dependency provider for AnalysisService."""
    global _analysis_service_instance
    if _analysis_service_instance is None:
        _analysis_service_instance = AnalysisService()
    return _analysis_service_instance
