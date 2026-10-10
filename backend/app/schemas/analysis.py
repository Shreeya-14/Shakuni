"""Pydantic schemas for Shakuni API requests and responses."""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field, field_validator


class AnalysisRequest(BaseModel):
    """Payload for analyzing a single message."""
    text: str = Field(..., description="The message or statement to analyze for manipulation patterns.")
    engine: Optional[str] = Field("hybrid", description="Reasoning engine: 'hybrid', 'gemini', 'openai', 'groq', 'ollama', or 'local'")
    api_key: Optional[str] = Field(None, description="Optional user-provided API key for Gemini / OpenAI / Groq")
    model_name: Optional[str] = Field(None, description="Optional specific model identifier")

    @field_validator("text")
    def text_must_not_be_blank(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Input text must contain at least one non-whitespace character.")
        if len(v) > 10000:
            raise ValueError("Input text exceeds the maximum allowed length of 10,000 characters.")
        return v


class BatchAnalysisRequest(BaseModel):
    """Payload for analyzing multiple messages in a single batch."""
    texts: List[str] = Field(..., min_length=1, max_length=50, description="List of messages to analyze (1-50 items).")
    engine: Optional[str] = Field("hybrid", description="Reasoning engine: 'hybrid', 'gemini', 'openai', 'groq', 'ollama', or 'local'")
    api_key: Optional[str] = Field(None, description="Optional user-provided API key")
    model_name: Optional[str] = Field(None, description="Optional specific model identifier")

    @field_validator("texts")
    def validate_texts(cls, v: List[str]) -> List[str]:
        if not v:
            raise ValueError("The texts list cannot be empty.")
        for idx, text in enumerate(v):
            if not text or not text.strip():
                raise ValueError(f"Text item at index {idx} cannot be empty or whitespace only.")
            if len(text) > 10000:
                raise ValueError(f"Text item at index {idx} exceeds 10,000 characters.")
        return v


class DetectedIndicatorSchema(BaseModel):
    """Schema representing an identified linguistic pattern marker."""
    name: str = Field(..., description="Name of the detected linguistic indicator")
    matched_phrase: str = Field(..., description="Matched phrase from the text")
    category_relevance: str = Field(..., description="Category this marker typically signals")
    description: str = Field(..., description="Explanation of rhetorical role")


class LinguisticStyleSchema(BaseModel):
    """Deep style, tone, and discourse analysis."""
    tone: str = Field(..., description="Dominant speaking/writing tone")
    emotional_temperature: str = Field(..., description="Cold, heated, calm, or feigned neutrality")
    directness: str = Field(..., description="Overt, covert, or passive-aggressive")
    formality: str = Field(..., description="Formality register")
    surface_meaning: str = Field(..., description="Literal asserted meaning")
    hidden_subtext: str = Field(..., description="Psychologically implied subtext and leverage")
    rhetorical_devices: List[str] = Field(default_factory=list, description="Detected rhetorical/manipulative devices")
    power_dynamic: str = Field(..., description="Interpersonal power stance")
    recommended_response: str = Field(..., description="Actionable disarming counter-response")
    model_provider: str = Field(..., description="AI model engine that produced the analysis")


class AnalysisResponse(BaseModel):
    """Complete analysis result schema."""
    text: str = Field(..., description="The analyzed input text")
    category: str = Field(..., description="Identified manipulation pattern category")
    risk_score: int = Field(..., ge=0, le=100, description="Estimated pattern intensity score (0-100)")
    risk_level: str = Field(..., description="Risk tier: Low, Moderate, or High")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Model statistical confidence (0.0-1.0)")
    explanation: str = Field(..., description="Human-readable rationale and interpretation")
    indicators: List[DetectedIndicatorSchema] = Field(default_factory=list, description="List of detected linguistic indicators")
    probabilities: Dict[str, float] = Field(..., description="Posterior probability distribution over all 7 categories")
    style_analysis: Optional[LinguisticStyleSchema] = Field(None, description="Deep speaking and writing style discourse breakdown")


class BatchAnalysisResponse(BaseModel):
    """Batch analysis collection response."""
    total_analyzed: int = Field(..., description="Number of texts analyzed")
    results: List[AnalysisResponse] = Field(..., description="Individual analysis results")


class CategoryDetailSchema(BaseModel):
    """Schema describing a centralized manipulation category."""
    id: str
    name: str
    description: str
    examples: List[str]
    typical_linguistic_indicators: List[str]
    risk_interpretation: str
    base_risk_weight: float


class CategoriesResponse(BaseModel):
    """Response containing all supported manipulation categories."""
    total_categories: int
    categories: List[CategoryDetailSchema]


class HealthResponse(BaseModel):
    """API health status response schema."""
    status: str
    service: str
    version: str
    model_loaded: bool
