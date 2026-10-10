# Shakuni AI: System & Model Audit Report

**Date:** 2026-10-09  
**Repository:** `C:\Shakuni`  
**Target:** Upgrade Shakuni into a Context-Aware Communication Manipulation Analysis System

---

## 1. Executive Summary

This audit investigates the root causes behind false positive classifications in the existing Shakuni framework (notably ordinary sentences such as *"There is a meeting tomorrow."* being classified as *Misleading Framing* or *Social Pressure* with elevated risk scores). 

The audit covers:
- Dataset composition, provenance, and lexical distribution.
- Baseline TF-IDF + Logistic Regression model architecture and inference logic.
- Confidence, risk score, and uncertainty handling mechanisms.
- Backend API endpoints, Pydantic schemas, and frontend UI data contracts.
- Deployment and hosting constraints (Render Free/Starter tier).

---

## 2. Root Cause Analysis of False Positives

### 2.1 Lack of Diverse and Conversational Neutral Data
The current dataset (`data/raw/manipulation_dataset.csv`) contains exactly 280 samples (40 samples per category across 7 classes).
- The `Normal / No Significant Manipulation` category consists solely of 40 long, formal, corporate/technical announcements (e.g., *"The scheduled software release has been postponed to Tuesday to complete standard regression testing"*).
- The training set contains **zero** short, informal, or everyday conversational utterances (e.g., meeting notifications, routine reminders, simple requests, personal worries without coercion, or balanced decision discussions).
- When presented with a short utterance like *"There is a meeting tomorrow."*, the vocabulary overlap with the 40 formal normal samples is minimal.

### 2.2 Bag-of-Words Lexical Trapping (TF-IDF Bias)
In a tiny 280-sample corpus with 4,595 n-gram features:
- The token `"tomorrow"` appears in *Deceptive Persuasion* (*"currency will be revalued tomorrow"*) and *Misleading Framing*.
- The token `"everyone"` appears across dozens of *Social Pressure* samples (*"Everyone on the leadership team..."*, *"Everyone agrees..."*). Factual sentences like *"Everyone received the announcement yesterday."* get dragged into *Social Pressure* purely because of word frequency.
- The word `"worried"` appears in *Emotional Pressure* (*"awake all night sick with worry"*). Hence, benign personal expressions like *"I am worried about the deadline."* get flagged as manipulation.
- Legitimate persuasive sentences (*"I strongly recommend this option because it reduces costs."*) contain words like `"recommend"` and `"costs"`, which TF-IDF correlates with *Deceptive Persuasion*.

### 2.3 Uncalibrated Softmax and Forced Argmax Classification
- In a 7-class problem, uniform random probability is `1 / 7 ≈ 0.1428`.
- For *"We need to make a decision today."*, the model's highest probability was `0.1940` (barely above uniform noise).
- The system unconditionally forces the top argmax category without verifying whether the model has sufficient statistical evidence to classify the text.
- There is no mechanism to reject low-confidence predictions or output `"Insufficient evidence to classify"` or `"No significant manipulation detected"`.

### 2.4 Inverted and Misleading Risk Score Formula
The existing risk formula in `ai_engine/analysis/risk_score.py`:
```python
p_manip = 1.0 - prob_normal
raw_score = (base_weight * 0.45) + (p_manip * 30.0) + (confidence * 12.0) + indicator_score
```
Where `base_weight` for *Deceptive Persuasion* is `88`, and for *Emotional Pressure* is `72`:
- When the model is completely unsure about an input, `prob_normal` is low (`~0.15`), meaning `p_manip = 0.85`.
- The formula multiplies `base_weight (88) * 0.45 = 39.6` and adds `p_manip (0.85) * 30 = 25.5`, yielding a baseline of `65.1` points before even considering indicators.
- **Paradoxical Effect:** High model uncertainty directly manufactures a Moderate/High risk score! Model ignorance is penalized as severe manipulation.

---

## 3. Dataset Audit & Provenance

- **Current Raw Dataset:** `data/raw/manipulation_dataset.csv`
  - Total samples: 280 (40 samples × 7 classes).
  - Provenance: `synthetic/curated research examples`.
  - Format: CSV (`id`, `text`, `category`, `source_type`).
- **Evaluation Dataset:** `evaluation/test_cases/evaluation_cases.csv`
  - Total samples: 35 (5 samples × 7 classes).
- **Shortcomings Identified:**
  - Complete absence of negative hard-examples (sentences with meeting words, deadlines, emotions, authority, or persuasion that are NOT manipulative).
  - Lack of contrastive pairs.
  - Very narrow syntactic diversity.

---

## 4. Environment & Deployment Constraints

- **Local Machine:** Windows 10/11, Python 3.11.9, no NVIDIA GPU available (`nvidia-smi` unavailable, CPU only).
- **Installed Packages:** `fastapi`, `uvicorn`, `scikit-learn 1.8.0`, `pandas 3.0.2`, `numpy 2.4.4`, `joblib 1.4.2`.
- **Target Deployment:** Render (configured via `render.yaml`):
  - Memory limit: 512 MB RAM (standard free/starter tier).
  - Disk / Slug size: Standard tier constraints.
  - Startup / Cold-start: Webhook timeouts on slow model loads.
  - A heavy transformer (like standard BERT/DeBERTa with PyTorch GPU/CPU runtime) consumes 400MB–800MB RAM upon import and model initialization, posing significant OOM (Out Of Memory) kill risks on Render 512MB RAM containers.
  - A lightweight, highly calibrated model or compact distilled model with ONNX / optimized runtime or calibrated scikit-learn ensemble must be benchmarked side-by-side to ensure deployment viability.

---

## 5. Action Plan

1. **Dataset Expansion & Curation:**
   - Preserve original dataset in `data/raw/manipulation_dataset_v1_backup.csv`.
   - Expand the dataset to include a rich, diverse set of neutral announcements, factual statements, ordinary requests/instructions, meeting schedules, deadlines, non-coercive emotional expressions, legitimate persuasive arguments, hard negatives, and contrastive pairs across all 7 categories.
   - Maintain explicit provenance tags (`synthetic/curated research examples`).
2. **Model Baseline & Candidate Architecture:**
   - Train baseline TF-IDF + Logistic Regression on the improved dataset.
   - Evaluate fine-tuned transformer and calibrated linear/ensemble classifiers.
   - Measure macro/weighted F1, neutral false positive rate (FPR), inference latency, and memory footprint.
   - Select the superior, most reliable deployable architecture.
3. **Evidence-Based Uncertainty & Calibrated Decision Rule:**
   - Implement rejection criteria: if predicted non-normal category confidence does not exceed a calibrated threshold or if normal/insufficient evidence dominates, classify as `"No significant manipulation detected"` or `"Insufficient evidence to classify"`.
   - Context caveat for isolated single sentences regarding *Selective Information* and *Information Withholding*.
4. **Decoupled Risk Scoring:**
   - Recompute risk score so it reflects actual evidence and verified confidence, not uncertainty or default class weights.
5. **System Integration & Testing:**
   - Preserve FastAPI endpoints (`/api/analyze`, `/api/batch-analyze`, `/api/categories`, `/api/health`).
   - Validate regression tests (12 cases).
   - Verify frontend build and API contract compatibility.
