"""Evaluation metrics utilities for Shakuni."""

from typing import Dict, List, Any
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report
)


def compute_metrics(
    y_true: List[str],
    y_pred: List[str],
    labels: List[str]
) -> Dict[str, Any]:
    """Compute comprehensive classification metrics."""
    acc = accuracy_score(y_true, y_pred)
    
    macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="macro", zero_division=0
    )
    weighted_p, weighted_r, weighted_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="weighted", zero_division=0
    )
    
    per_class_p, per_class_r, per_class_f1, per_class_supp = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average=None, zero_division=0
    )
    
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    per_category = {}
    for idx, label in enumerate(labels):
        per_category[label] = {
            "precision": round(float(per_class_p[idx]), 4),
            "recall": round(float(per_class_r[idx]), 4),
            "f1_score": round(float(per_class_f1[idx]), 4),
            "support": int(per_class_supp[idx])
        }
        
    return {
        "accuracy": round(float(acc), 4),
        "macro_precision": round(float(macro_p), 4),
        "macro_recall": round(float(macro_r), 4),
        "macro_f1": round(float(macro_f1), 4),
        "weighted_precision": round(float(weighted_p), 4),
        "weighted_recall": round(float(weighted_r), 4),
        "weighted_f1": round(float(weighted_f1), 4),
        "per_category": per_category,
        "confusion_matrix": cm.tolist(),
        "labels": labels
    }


def format_confusion_matrix_markdown(cm: List[List[int]], labels: List[str]) -> str:
    """Format a 2D confusion matrix into a readable Markdown table."""
    short_labels = [l.split(" / ")[0][:14] for l in labels]
    header = "| True \\ Pred | " + " | ".join(short_labels) + " |"
    divider = "|:---|:" + "-:|:".join(["---" for _ in labels]) + "-:|"
    rows = [header, divider]
    
    for idx, row in enumerate(cm):
        row_str = f"| **{short_labels[idx]}** | " + " | ".join(str(val) for val in row) + " |"
        rows.append(row_str)
        
    return "\n".join(rows)
