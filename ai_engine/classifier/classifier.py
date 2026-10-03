"""Machine Learning Classifier for Shakuni.

Loads the trained TF-IDF vectorizer and classification model to predict manipulation
categories and probability distributions over all 7 classes.
"""

import os
import re
from typing import Dict, List, Tuple, Optional
import joblib
import numpy as np

from ai_engine.classifier.categories import CATEGORY_NAMES, MANIPULATION_CATEGORIES

DEFAULT_MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models",
    "shakuni_classifier.joblib"
)
DEFAULT_VECTORIZER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models",
    "shakuni_vectorizer.joblib"
)


def clean_text(text: str) -> str:
    """Normalize input text for TF-IDF feature extraction."""
    if not text:
        return ""
    # Standardize whitespace and remove non-printable characters
    cleaned = re.sub(r"[\r\n\t]+", " ", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


class ShakuniClassifier:
    """Classifier wrapper handling model persistence, feature extraction, and inference."""

    def __init__(
        self,
        model_path: Optional[str] = None,
        vectorizer_path: Optional[str] = None
    ):
        self.model_path = model_path or os.getenv("MODEL_PATH", DEFAULT_MODEL_PATH)
        self.vectorizer_path = vectorizer_path or os.getenv("VECTORIZER_PATH", DEFAULT_VECTORIZER_PATH)
        self.model = None
        self.vectorizer = None
        self.is_loaded = False
        self._load_model()

    def _load_model(self) -> bool:
        """Attempt to load pre-trained model and vectorizer from disk."""
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            try:
                self.model = joblib.load(self.model_path)
                self.vectorizer = joblib.load(self.vectorizer_path)
                self.is_loaded = True
                return True
            except Exception as e:
                print(f"[Warning] Failed to load Shakuni model artifacts: {e}")
                self.is_loaded = False
                return False
        return False

    def ensure_model_loaded(self):
        """Ensure the model is loaded; if missing, triggers model training."""
        if not self.is_loaded:
            loaded = self._load_model()
            if not loaded:
                print("[Info] Model artifacts not found. Initiating on-the-fly training...")
                from ai_engine.training.train_model import train_and_save_model
                train_and_save_model()
                self._load_model()

    def predict(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """Predict manipulation category, confidence, and full class probability distribution."""
        self.ensure_model_loaded()
        if not self.is_loaded or self.model is None or self.vectorizer is None:
            raise RuntimeError("Shakuni model is not loaded and could not be trained.")

        cleaned = clean_text(text)
        if not cleaned:
            # Handle empty text with neutral default
            neutral_probs = {cat: 0.0 for cat in CATEGORY_NAMES}
            neutral_probs["Normal / No Significant Manipulation"] = 1.0
            return "Normal / No Significant Manipulation", 1.0, neutral_probs

        features = self.vectorizer.transform([cleaned])
        
        # Get probability estimates
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(features)[0]
            classes = self.model.classes_
            prob_dict = {str(cls_name): round(float(prob), 4) for cls_name, prob in zip(classes, probs)}
            
            # Ensure all 7 categories exist in dictionary
            for cat_name in CATEGORY_NAMES:
                if cat_name not in prob_dict:
                    prob_dict[cat_name] = 0.0
                    
            # Best category is argmax
            best_idx = int(np.argmax(probs))
            predicted_category = str(classes[best_idx])
            confidence = round(float(probs[best_idx]), 4)
        else:
            predicted_category = str(self.model.predict(features)[0])
            confidence = 0.85
            prob_dict = {cat: (0.85 if cat == predicted_category else round(0.15 / (len(CATEGORY_NAMES) - 1), 4)) for cat in CATEGORY_NAMES}

        return predicted_category, confidence, prob_dict

    def batch_predict(self, texts: List[str]) -> List[Tuple[str, float, Dict[str, float]]]:
        """Perform batch prediction over a list of texts."""
        return [self.predict(t) for t in texts]


# Global classifier instance for reuse across requests
_global_classifier: Optional[ShakuniClassifier] = None


def get_classifier() -> ShakuniClassifier:
    """Retrieve or initialize the singleton classifier instance."""
    global _global_classifier
    if _global_classifier is None:
        _global_classifier = ShakuniClassifier()
    return _global_classifier
