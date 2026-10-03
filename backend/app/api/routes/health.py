"""Health and system status routes."""

from fastapi import APIRouter
from backend.app.schemas.analysis import HealthResponse
from ai_engine.classifier.classifier import get_classifier
from backend.app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def check_health():
    """Health check endpoint to verify backend status and model readiness."""
    classifier = get_classifier()
    return HealthResponse(
        status="healthy",
        service="shakuni-api",
        version=settings.VERSION,
        model_loaded=classifier.is_loaded
    )
