"""Main FastAPI Application Entrypoint for Shakuni."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from backend.app.core.config import settings
from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.analysis import router as analysis_router
from ai_engine.classifier.classifier import get_classifier


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle manager: loads ML models on startup."""
    print("[Startup] Initializing Shakuni AI Engine...")
    classifier = get_classifier()
    classifier.ensure_model_loaded()
    print(f"[Startup] Model loaded successfully: {classifier.is_loaded}")
    yield
    print("[Shutdown] Cleaning up Shakuni resources...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=(
        "Shakuni is an academic research and project framework for identifying strategic deception, "
        "persuasive rhetoric, and information manipulation patterns. "
        "Predictions are probabilistic pattern analyses, not lie detection."
    ),
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS if settings.ALLOWED_ORIGINS else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from fastapi.encoders import jsonable_encoder


# Global validation error handler for friendly errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    first_msg = errors[0].get("msg") if errors else "Invalid request data"
    first_loc = " -> ".join([str(x) for x in errors[0].get("loc", [])]) if errors else ""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "message": str(first_msg),
            "field": first_loc,
            "details": jsonable_encoder(errors)
        }
    )



# General exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected server error occurred.",
            "detail": str(exc) if settings.DEBUG else None
        }
    )


# Root landing endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "framework": "Shakuni",
        "description": "AI Framework for Strategic Deception and Information Manipulation Analysis",
        "version": settings.VERSION,
        "docs": "/docs",
        "endpoints": {
            "health": "/api/health",
            "analyze": "/api/analyze",
            "batch_analyze": "/api/batch-analyze",
            "categories": "/api/categories"
        }
    }


# Include Routers under /api
app.include_router(health_router, prefix="/api")
app.include_router(analysis_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
