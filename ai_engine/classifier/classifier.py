"""Machine Learning Classifier for Shakuni.

Supports contextual language models (fine-tuned DistilBERT) with seamless fallback
to calibrated TF-IDF + Logistic Regression classifiers.
Implements evidence-based uncertainty handling, calibrated rejection, and context-aware
pattern classification.
"""

import os
import re
from typing import Dict, List, Tuple, Optional
import numpy as np

from ai_engine.classifier.categories import (
    CATEGORY_NAMES,
    INSUFFICIENT_EVIDENCE,
    NO_MANIPULATION_DETECTED
)

NORMAL_CATEGORY_NAME = "Normal / No Significant Manipulation"

DEFAULT_DISTILBERT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models",
    "distilbert_fine_tuned"
)
DEFAULT_TFIDF_MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models",
    "shakuni_classifier.joblib"
)
DEFAULT_TFIDF_VECTORIZER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models",
    "shakuni_vectorizer.joblib"
)

# Calibrated decision threshold tuned on validation split
CALIBRATED_UNCERTAINTY_THRESHOLD = 0.57


def clean_text(text: str) -> str:
    """Normalize input text for classification."""
    if not text:
        return ""
    cleaned = re.sub(r"[\r\n\t]+", " ", str(text))
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


class ShakuniClassifier:
    """Classifier wrapper handling model persistence, feature extraction, and inference."""

    def __init__(
        self,
        distilbert_dir: Optional[str] = None,
        tfidf_model_path: Optional[str] = None,
        tfidf_vectorizer_path: Optional[str] = None
    ):
        self.distilbert_dir = distilbert_dir or os.getenv("DISTILBERT_DIR", DEFAULT_DISTILBERT_DIR)
        self.model_path = tfidf_model_path or os.getenv("MODEL_PATH", DEFAULT_TFIDF_MODEL_PATH)
        self.vectorizer_path = tfidf_vectorizer_path or os.getenv("VECTORIZER_PATH", DEFAULT_TFIDF_VECTORIZER_PATH)

        self.model_type: Optional[str] = None
        self.model = None
        self.tokenizer = None
        self.vectorizer = None
        self.is_loaded = False

        self._load_model()

    def _load_model(self) -> bool:
        """Attempt to load the fine-tuned contextual model, falling back to TF-IDF."""
        preferred_type = os.getenv("SHAKUNI_MODEL_TYPE", "distilbert").lower()

        # 1. Try DistilBERT if preferred or present
        if preferred_type != "tfidf":
            safetensors_path = os.path.join(self.distilbert_dir, "model.safetensors")
            config_path = os.path.join(self.distilbert_dir, "config.json")
            if os.path.exists(safetensors_path) and os.path.exists(config_path):
                try:
                    import torch
                    from transformers import AutoTokenizer, AutoModelForSequenceClassification

                    self.tokenizer = AutoTokenizer.from_pretrained(self.distilbert_dir)
                    self.model = AutoModelForSequenceClassification.from_pretrained(self.distilbert_dir)
                    self.model.eval()
                    self.model_type = "distilbert"
                    self.is_loaded = True
                    print(f"[Info] Loaded fine-tuned DistilBERT contextual model from {self.distilbert_dir}")
                    return True
                except Exception as e:
                    print(f"[Warning] Failed loading DistilBERT model ({e}). Attempting TF-IDF fallback...")

        # 2. Fallback to TF-IDF + Logistic Regression
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            try:
                import joblib
                self.model = joblib.load(self.model_path)
                self.vectorizer = joblib.load(self.vectorizer_path)
                self.model_type = "tfidf"
                self.is_loaded = True
                print(f"[Info] Loaded calibrated TF-IDF classifier from {self.model_path}")
                return True
            except Exception as e:
                print(f"[Warning] Failed to load TF-IDF model artifacts: {e}")
                self.is_loaded = False
                return False

        return False

    def ensure_model_loaded(self):
        """Ensure the model is loaded; if missing, triggers baseline model training."""
        if not self.is_loaded:
            loaded = self._load_model()
            if not loaded:
                print("[Info] Model artifacts not found. Initiating model training...")
                from ai_engine.training.train_model import train_and_save_model
                train_and_save_model()
                self._load_model()

    def _apply_decision_rule(
        self,
        probs: np.ndarray,
        classes: List[str]
    ) -> Tuple[str, float, Dict[str, float]]:
        """Apply calibrated uncertainty rejection rules based on validation tuning."""
        prob_dict = {str(cls_name): round(float(prob), 4) for cls_name, prob in zip(classes, probs)}

        # Guarantee all 7 categories exist in dictionary
        for cat_name in CATEGORY_NAMES:
            if cat_name not in prob_dict:
                prob_dict[cat_name] = 0.0

        top_idx = int(np.argmax(probs))
        top_cat = str(classes[top_idx])
        top_conf = round(float(probs[top_idx]), 4)
        prob_normal = prob_dict.get(NORMAL_CATEGORY_NAME, 0.0)

        # Evidence-based decision rule:
        if top_cat == NORMAL_CATEGORY_NAME:
            predicted_category = NORMAL_CATEGORY_NAME
            confidence = top_conf
        else:
            # For non-normal predictions, check statistical confidence
            if top_conf < CALIBRATED_UNCERTAINTY_THRESHOLD:
                # If Normal probability is non-trivial or evidence is diffuse
                if prob_normal >= 0.20 or top_conf <= 0.32:
                    predicted_category = NO_MANIPULATION_DETECTED
                    confidence = round(float(max(prob_normal, 1.0 - top_conf)), 4)
                else:
                    predicted_category = INSUFFICIENT_EVIDENCE
                    confidence = top_conf
            else:
                predicted_category = top_cat
                confidence = top_conf

        return predicted_category, confidence, prob_dict

    def predict(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """Predict manipulation category, confidence, and full probability distribution."""
        self.ensure_model_loaded()
        if not self.is_loaded or self.model is None:
            raise RuntimeError("Shakuni model is not loaded and could not be initialized.")

        cleaned = clean_text(text)
        if not cleaned:
            neutral_probs = {cat: 0.0 for cat in CATEGORY_NAMES}
            neutral_probs[NORMAL_CATEGORY_NAME] = 1.0
            return NORMAL_CATEGORY_NAME, 1.0, neutral_probs

        if self.model_type == "distilbert":
            import torch
            inputs = self.tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                outputs = self.model(**inputs)
                probs = torch.softmax(outputs.logits, dim=1).cpu().numpy()[0]
            classes = [self.model.config.id2label[i] for i in range(len(CATEGORY_NAMES))]
            return self._apply_decision_rule(probs, classes)

        elif self.model_type == "tfidf":
            features = self.vectorizer.transform([cleaned])
            if hasattr(self.model, "predict_proba"):
                probs = self.model.predict_proba(features)[0]
                classes = list(self.model.classes_)
                return self._apply_decision_rule(probs, classes)
            else:
                pred = str(self.model.predict(features)[0])
                prob_dict = {cat: (0.85 if cat == pred else round(0.15 / 6, 4)) for cat in CATEGORY_NAMES}
                return pred, 0.85, prob_dict
        else:
            raise RuntimeError(f"Unknown model type: {self.model_type}")

    def batch_predict(self, texts: List[str]) -> List[Tuple[str, float, Dict[str, float]]]:
        """Perform optimized batch prediction over a list of texts."""
        self.ensure_model_loaded()
        if not self.is_loaded or self.model is None:
            raise RuntimeError("Shakuni model is not loaded and could not be initialized.")

        if not texts:
            return []

        cleaned_texts = [clean_text(t) for t in texts]

        # Handle edge cases where all texts are empty
        if self.model_type == "distilbert":
            import torch
            # Filter non-empty for batch pass
            valid_indices = [i for i, t in enumerate(cleaned_texts) if t]
            results = [None] * len(texts)

            # Default for empty strings
            for i, t in enumerate(cleaned_texts):
                if not t:
                    np_dict = {c: 0.0 for c in CATEGORY_NAMES}
                    np_dict[NORMAL_CATEGORY_NAME] = 1.0
                    results[i] = (NORMAL_CATEGORY_NAME, 1.0, np_dict)

            if valid_indices:
                valid_texts = [cleaned_texts[i] for i in valid_indices]
                inputs = self.tokenizer(valid_texts, return_tensors="pt", truncation=True, padding=True)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                    batch_probs = torch.softmax(outputs.logits, dim=1).cpu().numpy()

                classes = [self.model.config.id2label[i] for i in range(len(CATEGORY_NAMES))]
                for orig_idx, probs in zip(valid_indices, batch_probs):
                    results[orig_idx] = self._apply_decision_rule(probs, classes)

            return results

        elif self.model_type == "tfidf":
            features = self.vectorizer.transform(cleaned_texts)
            if hasattr(self.model, "predict_proba"):
                batch_probs = self.model.predict_proba(features)
                classes = list(self.model.classes_)
                return [self._apply_decision_rule(probs, classes) for probs in batch_probs]
            else:
                return [self.predict(t) for t in texts]
        else:
            return [self.predict(t) for t in texts]


# Global singleton instance
_global_classifier: Optional[ShakuniClassifier] = None


def get_classifier() -> ShakuniClassifier:
    """Retrieve or initialize the singleton ShakuniClassifier."""
    global _global_classifier
    if _global_classifier is None:
        _global_classifier = ShakuniClassifier()
    return _global_classifier
