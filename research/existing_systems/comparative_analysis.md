# Comparative Analysis of Existing Automated Discourse Systems

## Executive Summary
This document surveys existing computational frameworks for discourse evaluation—spanning toxicity filters, automated fact-checkers, dark pattern detectors, and sentiment analyzers—and highlights their architectural divergence from the Shakuni manipulation analysis engine.

---

## 1. Taxonomic Comparison

| Framework Category | Leading Implementations | Target Phenomena | Primary Limitation Regarding Strategic Deception |
|:---|:---|:---|:---|
| **Toxicity & Abuse Classifiers** | Jigsaw / Google Perspective API, Detoxify | Profanity, hate speech, explicit insults, identity attacks | Blind to polite manipulation, corporate spin, and authoritative coercion. |
| **Automated Fact-Checking** | ClaimBuster, Full Fact AI, FEVER benchmarks | Verifiable factual claims, historical assertions | Fails when statements are technically accurate yet cherry-picked or deceitfully framed. |
| **Sentiment Analysis** | VADER, RoBERTa-Sentiment | Positive vs negative affective polarity | Conflates persuasive urgency with negative sentiment, or manipulative enthusiasm with positive sentiment. |
| **Dark Pattern Detectors** | Mathur et al., UI crawlers | E-commerce layout traps, hidden cart items, fake countdowns | Strictly constrained to web visual structures; lacks capability for textual discourse analysis. |
| **Shakuni Framework** | Shakuni AI Engine | 7-category manipulation typology, explainable risk scoring | Focuses on rhetorical packaging, selective disclosure, and coercion indicators. |

---

## 2. In-Depth Case Comparison

### Case A: The Polite Coercion Vector
> *"Everyone on the leadership team has already signed off on the revised contract; please sign before 5 PM so you do not delay the team's bonus."*

- **Perspective API Output**: Toxicity score $< 0.05$ (classified as completely non-toxic).
- **Automated Fact-Checker**: Cannot evaluate (no empirical historical fact claim to verify against Wikipedia/knowledge base).
- **Shakuni Output**: Classified as **Social Pressure** (Confidence: ~85%, Risk Score: 68/100, Detected Markers: *"everyone on the leadership team"*, *"delay the team"*).

### Case B: The Cherry-Picked Statistical Vector
> *"Our product achieved a four hundred percent charge retention in controlled laboratory tests."*

- **Fact-Checker**: Might verify that the lab test indeed occurred (marking claim as "True").
- **Shakuni Output**: Classified as **Selective Information** (Confidence: ~88%, Risk Score: 56/100, Detected Markers: *"four hundred percent"*, *"controlled laboratory tests"*).
