# Shakuni Model Evaluation & Benchmarks

## 1. Evaluation Methodology

Evaluation is conducted across two complementary protocols:
1. **Stratified Holdout Validation**: A 20% stratified split of the 280-sample dataset ($N=56$), evaluated immediately after training with seed `42`.
2. **Dedicated Benchmark Testing**: A distinct 35-sample held-out evaluation suite (`evaluation/test_cases/evaluation_cases.csv`), containing 5 newly authored, unseen examples for each of the 7 manipulation categories.

All metrics reported below were computed directly by running the evaluation pipeline:
```bash
python -m evaluation.evaluate
```

---

## 2. Empirical Benchmark Results

### 2.1 Overall Performance on Held-Out Benchmark ($N=35$)

| Evaluation Metric | Measured Score |
|:---|:---:|
| **Test Accuracy** | **91.43%** |
| **Macro-Averaged Precision** | **0.9238** |
| **Macro-Averaged Recall** | **0.9143** |
| **Macro-Averaged F1-Score** | **0.9137** |
| **Weighted-Averaged F1-Score** | **0.9137** |

### 2.2 Per-Category Performance Breakdown

| Manipulation Category | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Normal / No Significant Manipulation** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Social Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Emotional Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Misleading Framing** | 1.0000 | 0.8000 | 0.8889 | 5 |
| **Selective Information** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Information Withholding** | 0.8000 | 0.8000 | 0.8000 | 5 |
| **Deceptive Persuasion** | 1.0000 | 0.8000 | 0.8889 | 5 |

### 2.3 Empirical Confusion Matrix

| Ground Truth \ Predicted | Normal | Social | Emotional | Framing | Selective | Withholding | Persuasion |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Normal** | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Social Pressure** | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| **Emotional Pressure** | 0 | 0 | 5 | 0 | 0 | 0 | 0 |
| **Misleading Framing** | 0 | 0 | 0 | 4 | 0 | 1 | 0 |
| **Selective Information** | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| **Information Withholding** | 1 | 0 | 0 | 0 | 0 | 4 | 0 |
| **Deceptive Persuasion** | 0 | 0 | 0 | 0 | 1 | 0 | 4 |

---

## 3. Detailed Error & Boundary Analysis

1. **High Confidence Separation**:
   - `Social Pressure` and `Emotional Pressure` achieved 100% precision and recall on the evaluation set due to distinct rhetorical markers (conformity appeals vs guilt/familial duty).
   - `Normal` utterances exhibited zero false positives against manipulative categories.

2. **Observed Confusion Vectors**:
   - **Information Withholding vs Normal**: One promotional utterance ("The new company wellness plan maintains your exact premium contribution rate") was categorized as normal because it lacked an overt deceptive cue, illustrating the challenge of detecting omission from surface text alone.
   - **Deceptive Persuasion vs Selective Information**: A claim highlighting unreleased clinical trials shared lexical overlap with statistical assertions, distributing probability between the two categories.

---

## 4. Reproducing Evaluation

To re-run and generate a new evaluation report:
```bash
python -m evaluation.evaluate
```
Results and metrics will be saved in `evaluation/results/evaluation_report.md` and `evaluation/results/metrics.json`.
