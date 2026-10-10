"""Analysis service integrating AI Engine with backend API endpoints."""

from typing import List, Dict, Any, Optional
from ai_engine.analyzer import get_analyzer, AnalysisResult
from ai_engine.classifier.categories import get_all_categories, CategoryDefinition
from backend.app.schemas.analysis import (
    AnalysisResponse,
    BatchAnalysisResponse,
    DetectedIndicatorSchema,
    LinguisticStyleSchema,
    CategoryDetailSchema,
    CategoriesResponse
)


class AnalysisService:
    """Service handling text analysis orchestration and category introspection."""

    def __init__(self):
        self.analyzer = get_analyzer()

    def analyze_single(
        self,
        text: str,
        engine: Optional[str] = None,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> AnalysisResponse:
        """Run manipulation and deception pattern analysis on a single text."""
        result: AnalysisResult = self.analyzer.analyze(
            text=text,
            engine=engine,
            api_key=api_key,
            model_name=model_name
        )

        style_schema = None
        if result.style_analysis:
            style_schema = LinguisticStyleSchema(
                tone=result.style_analysis.tone,
                emotional_temperature=result.style_analysis.emotional_temperature,
                directness=result.style_analysis.directness,
                formality=result.style_analysis.formality,
                surface_meaning=result.style_analysis.surface_meaning,
                hidden_subtext=result.style_analysis.hidden_subtext,
                rhetorical_devices=result.style_analysis.rhetorical_devices,
                power_dynamic=result.style_analysis.power_dynamic,
                recommended_response=result.style_analysis.recommended_response,
                model_provider=result.style_analysis.model_provider
            )
        
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
            probabilities=result.probabilities,
            style_analysis=style_schema
        )

    def analyze_batch(
        self,
        texts: List[str],
        engine: Optional[str] = None,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> BatchAnalysisResponse:
        """Run batch analysis over multiple texts using optimized batched inference."""
        raw_results: List[AnalysisResult] = self.analyzer.batch_analyze(
            texts=texts,
            engine=engine,
            api_key=api_key,
            model_name=model_name
        )
        results = []
        for r in raw_results:
            style_schema = None
            if r.style_analysis:
                style_schema = LinguisticStyleSchema(
                    tone=r.style_analysis.tone,
                    emotional_temperature=r.style_analysis.emotional_temperature,
                    directness=r.style_analysis.directness,
                    formality=r.style_analysis.formality,
                    surface_meaning=r.style_analysis.surface_meaning,
                    hidden_subtext=r.style_analysis.hidden_subtext,
                    rhetorical_devices=r.style_analysis.rhetorical_devices,
                    power_dynamic=r.style_analysis.power_dynamic,
                    recommended_response=r.style_analysis.recommended_response,
                    model_provider=r.style_analysis.model_provider
                )
            results.append(
                AnalysisResponse(
                    text=r.text,
                    category=r.category,
                    risk_score=r.risk_score,
                    risk_level=r.risk_level,
                    confidence=r.confidence,
                    explanation=r.explanation,
                    indicators=[
                        DetectedIndicatorSchema(
                            name=ind.name,
                            matched_phrase=ind.matched_phrase,
                            category_relevance=ind.category_relevance,
                            description=ind.description
                        )
                        for ind in r.indicators
                    ],
                    probabilities=r.probabilities,
                    style_analysis=style_schema
                )
            )
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
