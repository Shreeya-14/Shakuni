"""Analysis and category introspection routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from backend.app.schemas.analysis import (
    AnalysisRequest,
    AnalysisResponse,
    BatchAnalysisRequest,
    BatchAnalysisResponse,
    CategoriesResponse
)
from backend.app.services.analysis_service import AnalysisService, get_analysis_service

router = APIRouter(tags=["Analysis"])


@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Analyze single text for manipulation patterns",
    description="Classifies text into one of seven manipulation categories, computes transparent risk score, statistical confidence, detected linguistic indicators, and probability distribution."
)
async def analyze_text(
    payload: AnalysisRequest,
    service: AnalysisService = Depends(get_analysis_service)
) -> AnalysisResponse:
    """Analyze a single message for manipulation patterns."""
    try:
        return service.analyze_single(payload.text)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the analysis: {str(e)}"
        )


@router.post(
    "/batch-analyze",
    response_model=BatchAnalysisResponse,
    summary="Batch analyze multiple texts",
    description="Performs manipulation pattern analysis across an array of up to 50 text submissions."
)
async def batch_analyze_texts(
    payload: BatchAnalysisRequest,
    service: AnalysisService = Depends(get_analysis_service)
) -> BatchAnalysisResponse:
    """Analyze a batch of texts for manipulation patterns."""
    try:
        return service.analyze_batch(payload.texts)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the batch: {str(e)}"
        )


@router.get(
    "/categories",
    response_model=CategoriesResponse,
    summary="List supported manipulation categories",
    description="Returns the centralized catalog of the 7 supported communication and manipulation pattern categories, including definitions, examples, typical linguistic indicators, and risk interpretations."
)
async def list_categories(
    service: AnalysisService = Depends(get_analysis_service)
) -> CategoriesResponse:
    """List all seven supported manipulation categories and metadata."""
    try:
        return service.get_supported_categories()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unable to retrieve categories: {str(e)}"
        )
