"""Model Training Script for Shakuni.

Executes end-to-end model training:
1. Loads validated, leakage-free train and evaluation splits
2. Normalizes text
3. Extracts n-gram TF-IDF representations (fitted on train only)
4. Fits a calibrated, class-weighted classifier
5. Evaluates on validation and held-out test splits
6. Records comprehensive metrics including neutral false-positive rates
7. Persists model artifacts to ai_engine/models/
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_recall_fscore_support

from ai_engine.classifier.categories import CATEGORY_NAMES
from ai_engine.classifier.classifier import clean_text


def load_dataset_splits(base_dir: str):
    """Load train, val, and test splits with fallback to raw dataset."""
    train_path = os.path.join(base_dir, "data", "processed", "train.csv")
    val_path = os.path.join(base_dir, "data", "processed", "val.csv")
    test_path = os.path.join(base_dir, "data", "processed", "test.csv")

    if not (os.path.exists(train_path) and os.path.exists(test_path)):
        # Generate splits if missing
        print("[Info] Processed splits not found. Running dataset generation...")
        from ai_engine.training.generate_dataset import generate_dataset
        generate_dataset()

    train_df = pd.read_csv(train_path)
    val_df = pd.read_csv(val_path) if os.path.exists(val_path) else None
    test_df = pd.read_csv(test_path)

    return train_df, val_df, test_df


def train_and_save_model(
    base_dir: str = None,
    model_output_dir: str = None,
    results_output_dir: str = None
):
    """Train the TF-IDF + LogisticRegression pipeline and persist artifacts."""
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if model_output_dir is None:
        model_output_dir = os.path.join(base_dir, "ai_engine", "models")
    if results_output_dir is None:
        results_output_dir = os.path.join(base_dir, "evaluation", "results")

    os.makedirs(model_output_dir, exist_ok=True)
    os.makedirs(results_output_dir, exist_ok=True)

    print(f"Loading dataset splits from: {os.path.join(base_dir, 'data', 'processed')}")
    train_df, val_df, test_df = load_dataset_splits(base_dir)

    print(f"Train samples: {len(train_df)} | Val samples: {len(val_df) if val_df is not None else 0} | Test samples: {len(test_df)}")

    X_train = train_df["text"].astype(str).apply(clean_text).values
    y_train = train_df["category"].values

    X_test = test_df["text"].astype(str).apply(clean_text).values
    y_test = test_df["category"].values

    # TF-IDF Feature Extraction (learned strictly on training split)
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

    # Fit Logistic Regression with balanced class weights
    classifier = LogisticRegression(
        C=3.0,
        max_iter=1000,
        random_state=42,
        class_weight="balanced",
        solver="lbfgs"
    )
    classifier.fit(X_train_vec, y_train)

    # Predictions & Evaluation on held-out test set
    y_pred = classifier.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)

    p_macro, r_macro, f1_macro, _ = precision_recall_fscore_support(
        y_test, y_pred, labels=CATEGORY_NAMES, average="macro", zero_division=0
    )
    p_wt, r_wt, f1_wt, _ = precision_recall_fscore_support(
        y_test, y_pred, labels=CATEGORY_NAMES, average="weighted", zero_division=0
    )

    report_dict = classification_report(
        y_test,
        y_pred,
        labels=CATEGORY_NAMES,
        target_names=CATEGORY_NAMES,
        output_dict=True,
        zero_division=0
    )

    cm = confusion_matrix(y_test, y_pred, labels=CATEGORY_NAMES).tolist()

    # Neutral class false-positive rate
    norm_idx = CATEGORY_NAMES.index("Normal / No Significant Manipulation")
    norm_true_count = sum(cm[norm_idx])
    norm_correct = cm[norm_idx][norm_idx]
    neutral_fp_count = norm_true_count - norm_correct
    neutral_fp_rate = (neutral_fp_count / norm_true_count) if norm_true_count > 0 else 0.0

    metrics_summary = {
        "model_type": "TF-IDF + Logistic Regression",
        "dataset_train_samples": int(len(train_df)),
        "dataset_val_samples": int(len(val_df)) if val_df is not None else 0,
        "dataset_test_samples": int(len(test_df)),
        "vocabulary_size": int(len(vectorizer.vocabulary_)),
        "accuracy": round(float(accuracy), 4),
        "macro_precision": round(float(p_macro), 4),
        "macro_recall": round(float(r_macro), 4),
        "macro_avg_f1": round(float(f1_macro), 4),
        "weighted_precision": round(float(p_wt), 4),
        "weighted_recall": round(float(r_wt), 4),
        "weighted_avg_f1": round(float(f1_wt), 4),
        "neutral_samples_total": int(norm_true_count),
        "neutral_correct": int(norm_correct),
        "neutral_false_positive_count": int(neutral_fp_count),
        "neutral_false_positive_rate": round(float(neutral_fp_rate), 4),
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
    print(f"Neutral FP Rate: {neutral_fp_count}/{norm_true_count} ({neutral_fp_rate*100:.1f}%)")

    return metrics_summary


if __name__ == "__main__":
    train_and_save_model()
