"""Global test configuration and fixtures."""

import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure root workspace is on python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.main import app
from ai_engine.classifier.classifier import get_classifier


@pytest.fixture(scope="session")
def client():
    """Session-scoped FastAPI TestClient."""
    # Pre-load classifier to avoid per-test delay
    classifier = get_classifier()
    classifier.ensure_model_loaded()
    with TestClient(app) as test_client:
        yield test_client
