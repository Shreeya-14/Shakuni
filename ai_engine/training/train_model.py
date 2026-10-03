"""Model Training Script for Shakuni.

Executes end-to-end model training:
1. Loads and validates dataset
2. Normalizes text
3. Performs stratified train/test split
4. Extracts n-gram TF-IDF representations
5. Fits a calibrated Logistic Regression classifier
6. Generates and records evaluation metrics
7. Persists model artifacts to ai_engine/models/
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from ai_engine.classifier.categories import CATEGORY_NAMES
from ai_engine.classifier.classifier import clean_text


def load_dataset(dataset_path: str) -> pd.DataFrame:
    """Load and validate dataset from CSV."""
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at {dataset_path}. Run generate_dataset.py first.")
    
    df = pd.read_csv(dataset_path)
    required_cols = {"id", "text", "category", "source_type"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Dataset missing required columns. Expected {required_cols}, found {df.columns}")
    
    # Drop empty rows
    df = df.dropna(subset=["text", "category"])
    df["cleaned_text"] = df["text"].astype(str).apply(clean_text)
    
    # Validate category presence
    unique_cats = set(df["category"].unique())
    missing_cats = set(CATEGORY_NAMES) - unique_cats
    if missing_cats:
        print(f"[Warning] Dataset is missing definitions for categories: {missing_cats}")
        
    return df


def train_and_save_model(
    dataset_path: str = None,
    model_output_dir: str = None,
    results_output_dir: str = None
):
    """Train the TF-IDF + LogisticRegression pipeline and persist artifacts."""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    if dataset_path is None:
        dataset_path = os.path.join(base_dir, "data", "raw", "manipulation_dataset.csv")
    if model_output_dir is None:
        model_output_dir = os.path.join(base_dir, "ai_engine", "models")
    if results_output_dir is None:
        results_output_dir = os.path.join(base_dir, "evaluation", "results")

    os.makedirs(model_output_dir, exist_ok=True)
    os.makedirs(results_output_dir, exist_ok=True)

    print(f"Loading dataset from: {dataset_path}")
    df = load_dataset(dataset_path)
    print(f"Loaded {len(df)} samples across {df['category'].nunique()} categories.")

    X = df["cleaned_text"].values
    y = df["category"].values

    # Stratified 80/20 train/test split for reproducibility
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print(f"Training set: {len(X_train)} samples | Test set: {len(X_test)} samples")

    # TF-IDF Feature Extraction: unigrams + bigrams, sublinear TF scaling
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        sublinear_tf=True,
        min_df=1,
        max_df=0.95,
        strip_accents="unicode",
        token_pattern=r"(?u)\b\w+\b"
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    print(f"Vocabulary size: {len(vectorizer.vocabulary_)} features")

    # Train Logistic Regression with balanced class weights
    classifier = LogisticRegression(
        C=2.5,
        max_iter=1000,
        random_state=42,
        class_weight="balanced",
        solver="lbfgs"
    )

    classifier.fit(X_train_vec, y_train)

    # Predictions & Evaluation
    y_pred = classifier.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    report_dict = classification_report(
        y_test,
        y_pred,
        labels=CATEGORY_NAMES,
        target_names=CATEGORY_NAMES,
        output_dict=True,
        zero_division=0
    )

    cm = confusion_matrix(y_test, y_pred, labels=CATEGORY_NAMES).tolist()

    metrics_summary = {
        "dataset_total_samples": int(len(df)),
        "train_samples": int(len(X_train)),
        "test_samples": int(len(X_test)),
        "vocabulary_size": int(len(vectorizer.vocabulary_)),
        "accuracy": round(float(accuracy), 4),
        "macro_avg_f1": round(float(report_dict["macro avg"]["f1-score"]), 4),
        "weighted_avg_f1": round(float(report_dict["weighted avg"]["f1-score"]), 4),
        "per_category": {
            cat: {
                "precision": round(float(report_dict[cat]["precision"]), 4),
                "recall": round(float(report_dict[cat]["recall"]), 4),
                "f1_score": round(float(report_dict[cat]["f1-score"]), 4),
                "support": int(report_dict[cat]["support"])
            }
            for cat in CATEGORY_NAMES if cat in report_dict
        },
        "confusion_matrix": cm,
        "labels": CATEGORY_NAMES
    }

    # Save Model Artifacts
    model_path = os.path.join(model_output_dir, "shakuni_classifier.joblib")
    vectorizer_path = os.path.join(model_output_dir, "shakuni_vectorizer.joblib")
    
    joblib.dump(classifier, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    print(f"Saved model to: {model_path}")
    print(f"Saved vectorizer to: {vectorizer_path}")

    # Save Metrics
    metrics_file = os.path.join(results_output_dir, "training_metrics.json")
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(metrics_summary, f, indent=2)
    print(f"Saved training metrics to: {metrics_file}")

    print("\n--- Model Training Summary ---")
    print(f"Test Accuracy: {accuracy:.4f}")
    print(f"Macro F1-Score: {metrics_summary['macro_avg_f1']:.4f}")
    print(f"Weighted F1-Score: {metrics_summary['weighted_avg_f1']:.4f}")

    return metrics_summary


if __name__ == "__main__":
    train_and_save_model()
