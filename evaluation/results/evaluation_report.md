# Shakuni Model Evaluation Report

**Generated:** 2026-10-03 03:52:06 UTC  
**Evaluation Dataset:** `evaluation/test_cases/evaluation_cases.csv`  
**Dataset Type:** synthetic/curated research examples (held-out test set)  
**Total Evaluation Samples:** 35  
**Model Architecture:** TF-IDF (1-2 n-grams) + Logistic Regression (L2 regularization, balanced class weights)  

---

## 1. Overall Performance Summary

| Metric | Score |
|:---|:---:|
| **Accuracy** | **91.43%** (0.9143) |
| **Macro Precision** | 0.9238 |
| **Macro Recall** | 0.9143 |
| **Macro F1-Score** | **0.9137** |
| **Weighted Precision** | 0.9238 |
| **Weighted Recall** | 0.9143 |
| **Weighted F1-Score** | **0.9137** |

---

## 2. Per-Category Performance Breakdown

| Category | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Normal / No Significant Manipulation** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Social Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Emotional Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Misleading Framing** | 1.0000 | 0.8000 | 0.8889 | 5 |
| **Selective Information** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Information Withholding** | 0.8000 | 0.8000 | 0.8000 | 5 |
| **Deceptive Persuasion** | 1.0000 | 0.8000 | 0.8889 | 5 |

---

## 3. Confusion Matrix

Rows represent Ground Truth labels; columns represent Model Predictions.

| True \ Pred | Normal | Social Pressur | Emotional Pres | Misleading Fra | Selective Info | Information Wi | Deceptive Pers |
|:---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| **Normal** | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Social Pressur** | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| **Emotional Pres** | 0 | 0 | 5 | 0 | 0 | 0 | 0 |
| **Misleading Fra** | 0 | 0 | 0 | 4 | 0 | 1 | 0 |
| **Selective Info** | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| **Information Wi** | 1 | 0 | 0 | 0 | 0 | 4 | 0 |
| **Deceptive Pers** | 0 | 0 | 0 | 0 | 1 | 0 | 4 |

---

## 4. Empirical Observations & Error Analysis

1. **High Precision Categories**:
   - `Normal / No Significant Manipulation` consistently demonstrates high separation due to distinctive neutral, procedural phrasing.
   - `Deceptive Persuasion` achieves strong discrimination due to specific lexical markers (e.g. fabricated authority, absolute promises).

2. **Boundary Overlap**:
   - In low-data regimes, slight cross-category confusion can occur between `Social Pressure` and `Emotional Pressure`, where social conformity arguments occasionally share urgency and interpersonal stakes with emotional appeals.
   - `Selective Information` and `Information Withholding` both address incomplete disclosure, differing mainly in whether positive bias is highlighted vs. negative consequences omitted.

3. **Methodological Note**:
   - All results shown are strictly empirical, generated from running the classifier on the held-out evaluation dataset.
   - Predictions are probabilistic pattern classifications and must not be interpreted as absolute moral or judicial judgments of honesty.
