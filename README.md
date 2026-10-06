# Shakuni
### AI Framework for Strategic Deception and Information Manipulation Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-teal.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![React 18 + Vite](https://img.shields.io/badge/Frontend-React_18_+_Vite-61dafb.svg)](https://vitejs.dev/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-f7931e.svg)](https://scikit-learn.org/)
[![Test Suite](https://img.shields.io/badge/Pytest-27%2F27_Passed-brightgreen.svg)](tests/)
[![Benchmark Accuracy](https://img.shields.io/badge/Benchmark_Accuracy-91.4%25-success.svg)](evaluation/)

---

## 1. Project Overview

**Shakuni** is a full-stack, research-grade natural language processing platform designed to identify, categorize, and quantify **strategic deception, coercive rhetoric, and information manipulation patterns** in textual communication.

Named after the classical strategist archetype renowned for altering decision landscapes through psychological priming, loaded dilemmas, and asymmetric disclosure, Shakuni investigates how modern manipulative persuasion functions: not merely through crude factual fabrications or overt profanity, but through **subtle framing traps, peer conformity coercion, emotional leverage, selective metric presentation, and calculated information withholding**.

Rather than relying on opaque multi-billion-parameter neural models that hallucinate assertions without auditability, Shakuni combines an **interpretable scikit-learn classifier (sublinear TF-IDF + regularized Multinomial Logistic Regression)** with a deterministic linguistic marker engine and a transparent composite risk formula to generate verifiable intelligence reports.

> **Important Research & Epistemic Disclaimer:**  
> Shakuni analyzes *probabilistic linguistic communication patterns* against documented rhetorical structures. It is **NOT** a "lie detector", does not establish objective factual truth, and does not assess the internal moral intent or character of human speakers. All classifications represent statistical correspondence with curated communication archetypes.

---

## 2. Problem Statement & Motivation

Modern content moderation and NLP safety infrastructures exhibit critical blind spots when confronted with sophisticated persuasive maneuvers:

- **Toxicity Classifiers (e.g., Perspective API)** focus almost entirely on profanity, hate speech, and explicit aggression. Polite, manipulative coercion—such as corporate gaslighting, manufactured urgency, or contractual arm-twisting—easily bypasses detection.
- **Automated Fact-Checkers** verify discrete claims against historical knowledge bases, yet fail completely when statements are technically accurate but selectively cherry-picked, presented out of context, or stripped of critical caveats.
- **Binary Sentiment Classifiers** reduce nuanced discourse to positive or negative valence, obscuring predatory pressure cloaked in optimism or professional enthusiasm.

Shakuni addresses this research gap by establishing a formal 7-category taxonomy of strategic manipulation, an explainable machine learning classifier, and a calibrated threat-scoring engine dedicated to **how information is packaged, framed, and weaponized**.

---

## 3. Key Features

- **7-Category Manipulation Taxonomy**: Rigorous taxonomy classifying discourse into balanced non-manipulative communication or six discrete tactical maneuvers.
- **Interpretable Machine Learning Architecture**: Sublinear TF-IDF unigram/bigram feature extraction coupled with balanced Multinomial Logistic Regression.
- **Empirically Validated Performance**: **91.43% test accuracy** and **0.9137 Macro F1-score** on a held-out benchmark evaluation suite ($N=35$).
- **Explainable Composite Risk Scoring**: Transparent index ($0 \text{ to } 100$) integrating model confidence, category baseline severity, manipulation probability mass, and rhetorical marker density.
- **Calibrated Posterior Probabilities**: Softmax probability distributions across all seven taxonomy classes for transparent auditing.
- **Deterministic Linguistic Marker Extraction**: Grounded pattern recognition isolating specific rhetorical devices (false dichotomies, conformity appeals, manufactured urgency).
- **Plain-Language Explanations**: Contextual narrative synthesis communicating findings without technical jargon or absolute epistemic claims.
- **Light Editorial Multi-Page Web Application**: Six dedicated routes (`/`, `/analyze`, `/patterns`, `/research`, `/model`, `/about`) plus a resilient 404 handler, built with an editorial research publication aesthetic.
- **Production-Ready FastAPI Backend**: Asynchronous API endpoints with strict Pydantic schemas, dependency injection, CORS handling, and structured error responses.
- **Automated Verification**: Complete test suite of 27 unit and integration tests passing in under 3 seconds.
- **Containerized Deployment**: Multi-stage Dockerfiles and `docker-compose.yml` for unified local or server deployments.

---

## 4. Manipulation Categories

The taxonomy is defined centrally in `ai_engine/classifier/categories.py`:

| # | Category Name | Core Description | Typical Linguistic Indicators | Base Risk ($W_{\text{cat}}$) |
|:---:|---|---|---|:---:|
| 1 | **Normal / No Significant Manipulation** | Objective, balanced, and neutral communication with no coercive tactics or tactical omissions. | Balanced context, factual assertions, neutral framing, conditional phrasing | 10 / 100 |
| 2 | **Social Pressure** | Bandwagon appeals, consensus coercion, manufactured unanimity, and fear of professional or social isolation. | *"everyone agrees"*, *"lone dissenter"*, *"let the team down"*, *"don't be the only one"* | 65 / 100 |
| 3 | **Emotional Pressure** | Guilt induction, emotional blackmail, acute panic-inducing urgency, and sympathy exploitation. | *"if you really cared"*, *"on your conscience"*, *"ruin my life"*, *"sacrificed everything"* | 72 / 100 |
| 4 | **Misleading Framing** | False dichotomies, euphemistic corporate recontextualization, and loaded rhetoric constraining decision spaces. | *"either ... or"*, *"no other alternative"*, *"rightsizng"*, *"realigned synergy"* | 60 / 100 |
| 5 | **Selective Information** | Cherry-picking favorable statistics, isolated testimonials, and unrepresentative success metrics without baseline controls. | *"100% success rate"*, *"400% surge"*, *"every customer doubled"*, *"zero complaints"* | 52 / 100 |
| 6 | **Information Withholding** | Conspicuously concealing material caveats, recurring subscription obligations, penalties, or restrictive clauses. | *"completely free"*, *"just click agree"*, *"no upfront payment"*, *"standard boilerplate"* | 75 / 100 |
| 7 | **Deceptive Persuasion** | Fabricated executive authority, pretexts, artificial regulatory imperatives, and zero-risk guarantees. | *"CEO personally authorized"*, *"100% risk-free"*, *"secretly approved"*, *"mandatory audit"* | 88 / 100 |

---

## 5. System Architecture

Shakuni employs a layered, decoupled system design:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        USER (BROWSER CLIENT)                           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│             FRONTEND APPLICATION (React 18 + Vite :5173)               │
│                                                                        │
│  Routes: / (Home)  /analyze  /patterns  /research  /model  /about  404 │
│  Design: Light Editorial Research System (Ivory / Charcoal / Burgundy) │
│  Components: AnalyzerForm, ResultCard, RiskIndicator, AnalysisHistory │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTP POST /api/analyze
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                 BACKEND API SERVICE (FastAPI :8000)                    │
│                                                                        │
│  - CORS Middleware & Settings (core/config.py)                         │
│  - Pydantic Request & Response Validation (schemas/analysis.py)        │
│  - Service Bridge & Orchestration (services/analysis_service.py)       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      SHAKUNI AI / NLP ENGINE                           │
│                                                                        │
│  1. ShakuniAnalyzer (Unified Facade)                                   │
│     ├── Text Normalization (Unicode / Whitespace / Lowercase)          │
│     │                                                                  │
│  2. ShakuniClassifier                                                  │
│     ├── Sublinear TF-IDF Vectorizer (1–2 n-grams, 4,595 vocabulary)    │
│     └── Multinomial Logistic Regression Softmax Calibration            │
│         └── Yields: Primary Category & Full Class Probabilities        │
│                                                                        │
│  3. Indicator Engine (analysis/indicators.py)                          │
│     └── Deterministic Regex Extraction of Tactical Linguistic Devices  │
│                                                                        │
│  4. Transparent Risk Engine (analysis/risk_score.py)                   │
│     └── Composite Score Formulation (0–100) + Risk Tier Calibration    │
│                                                                        │
│  5. Narrative Explainer (analysis/explanation.py)                      │
│     └── Contextual, Evidence-Grounded Plain-Language Report Generation │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 6. AI / ML Methodology

### 6.1 Text Preprocessing & Vectorization
Input text strings undergo unicode normalization, lowercasing, and whitespace compaction. Feature vectors are extracted using sublinear term-frequency inverse-document-frequency ($\text{TF-IDF}$):

$$\text{TF}(t, d) = 1 + \ln(\text{count}(t, d)) \quad \text{for } \text{count}(t, d) > 0$$
$$\text{IDF}(t, D) = \ln\left(\frac{1 + |D|}{1 + \text{DF}(t, D)}\right) + 1$$
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

Features are extracted across **unigram and bigram ranges (1–2)** to capture both isolated tactical terms (*"guaranteed"*, *"dissenter"*) and compound rhetorical phrases (*"either you"*, *"completely free"*, *"lone holdout"*). Vectors are $L_2$-normalized across a fitted vocabulary of 4,595 features.

### 6.2 Classification & Posterior Probability Calibration
Shakuni uses an $L_2$-regularized **Multinomial Logistic Regression** model with balanced class weights. Posterior probabilities for each category $c \in \{1, \dots, 7\}$ are computed via the softmax function:

$$P(y = c \mid \mathbf{x}) = \frac{\exp(\mathbf{w}_c^T \mathbf{x} + b_c)}{\sum_{j=1}^7 \exp(\mathbf{w}_j^T \mathbf{x} + b_j)}$$

### 6.3 Confidence Estimation
Statistical confidence reflects the posterior margin of the top-ranked category:

$$\text{Confidence} = \max_{c \in \{1, \dots, 7\}} P(y = c \mid \mathbf{x})$$

### 6.4 Composite Risk Scoring Formula
The Shakuni Risk Score $R \in [0, 100]$ is computed using an explainable multi-factor formula:

$$R = \text{round}\left( \text{clamp}\left( (W_{\text{cat}} \times 0.45) + (P_{\text{manip}} \times 30.0) + (\text{Confidence} \times 12.0) + I_{\text{mod}}, 0, 100 \right) \right)$$

Where:
- **$W_{\text{cat}}$**: Qualitative baseline severity for the predicted class (10 for Normal up to 88 for Deceptive Persuasion).
- **$P_{\text{manip}}$**: Aggregate probability mass assigned to non-normal categories ($1.0 - P(\text{Normal})$).
- **$\text{Confidence}$**: Model posterior probability for the assigned class.
- **$I_{\text{mod}}$**: Density bonus for category-congruent linguistic markers (+4 for primary markers, +2 for secondary markers, capped at 20).

**Risk Tier Calibration:**
- **Low Risk (0–39)**: Neutral communication, baseline professional framing.
- **Moderate Risk (40–69)**: Observable rhetorical nudges, framing constraints, or mild urgency.
- **High Risk (70–100)**: Acute coercive pressure, deceptive authority claims, or severe omission.

---

## 7. Dataset Documentation

All samples in the Shakuni dataset are explicitly documented as **`synthetic/curated research examples`**.

### Provenance & Rationale
1. **Privacy Preservation**: Analyzing manipulative communication using unconsented private correspondence or scraped messaging threads violates user privacy. Curated research examples eliminate privacy concerns.
2. **Signal Isolation**: Organic social media data frequently conflates vulgarity, hate speech, and slang. Curated examples isolate subtle manipulative structures without confounding lexical noise.
3. **Reproducibility**: Provides an open, verifiable baseline for academic replication.

### Dataset Stratification
- **Training Corpus (`data/raw/manipulation_dataset.csv`)**: 280 balanced samples (exactly 40 samples per category, zero missing values, zero duplicate entries).
- **Evaluation Benchmark Suite (`evaluation/test_cases/evaluation_cases.csv`)**: 35 held-out samples (exactly 5 unseen samples per category).

### CSV Schema
```csv
id,text,category,source_type
1,"The quarterly product documentation is ready for review.",Normal / No Significant Manipulation,synthetic/curated research examples
```

---

## 8. Empirical Model Evaluation & Results

Evaluation is executed directly against the held-out benchmark dataset ($N = 35$) via:

```bash
python -m evaluation.evaluate
```

### Overall Benchmark Metrics
| Evaluation Metric | Measured Score | Benchmark Target | Status |
|:---|:---:|:---:|:---:|
| **Overall Accuracy** | **91.43%** | $\ge 85.0\%$ | Exceeded |
| **Macro-Averaged Precision** | **0.9238** | $\ge 0.850$ | Exceeded |
| **Macro-Averaged Recall** | **0.9143** | $\ge 0.850$ | Exceeded |
| **Macro-Averaged F1-Score** | **0.9137** | $\ge 0.850$ | Exceeded |
| **Weighted-Averaged F1-Score** | **0.9137** | $\ge 0.850$ | Exceeded |

### Per-Category Performance Breakdown
| Category | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Normal / No Significant Manipulation** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Social Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Emotional Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Misleading Framing** | 1.0000 | 0.8000 | 0.8889 | 5 |
| **Selective Information** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Information Withholding** | 0.8000 | 0.8000 | 0.8000 | 5 |
| **Deceptive Persuasion** | 1.0000 | 0.8000 | 0.8889 | 5 |

### Empirical Confusion Matrix
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

## 9. Frontend Application Architecture

The frontend is a multi-page single-page application built on React 18, React Router v6, and Vite.

### Visual Identity & Design System
- **Aesthetic**: Light editorial research monograph and strategic intelligence platform.
- **Palette**:
  - Background: Warm ivory (`#fbf9f5`) and clean white surfaces (`#ffffff`).
  - Typography: Deep charcoal (`#18191c`), warm slate (`#484b53`), and muted taupe (`#6e727c`).
  - Primary Brand Accent: Deep burgundy / wine (`#7a1c30`).
  - Secondary Accent: Antique gold / brass (`#b89047`).
  - Supporting Accent: Muted forest sage (`#3d6852`).
- **Typography Pairing**: Elegant editorial serif (`Playfair Display`) for headings and monograph titles paired with geometric UI sans (`Plus Jakarta Sans`) and code monospace (`JetBrains Mono`).

### Route Structure
- **`/` (Home)**: Editorial asymmetric hero, live pattern spotlight carousel, interactive mini-analyzer, empirical system metrics, and architectural overview.
- **`/analyze` (Workbench)**: Interactive analysis workbench with live text input, word/character counter, preset scenario pills, segmented risk spectrum bar, linguistic evidence chips, posterior probability distribution, and collapsible session history drawer.
- **`/patterns` (Taxonomy)**: Tactical dossier exploring all 7 categories with game-theoretic mechanisms, behavioral markers, detection logic, and real-world citations.
- **`/research` (Literature)**: Academic monograph covering asymmetric information theory, rhetorical coercion, bounded rationality, and comprehensive bibliography.
- **`/model` / `/methodology` (Methodology)**: Detailed mathematical documentation of the NLP pipeline, TF-IDF formulas, logistic regression optimization, composite risk formulation, and empirical confusion matrix tables.
- **`/about` (Overview)**: Academic mission statement, core pillars, project architecture, team attribution, and ethical guardrails.
- **`*` (NotFound)**: Dedicated editorial 404 page with strategic compass motif and navigation links back to active routes.

---

## 10. Backend REST API

The FastAPI service runs on port `8000` with interactive Swagger UI at `http://localhost:8000/docs`.

### API Endpoints

#### 1. `GET /api/health`
Health verification and model availability status.
```json
{
  "status": "healthy",
  "service": "shakuni-api",
  "version": "1.0.0",
  "model_loaded": true
}
```

#### 2. `POST /api/analyze`
Submits a text sample for complete linguistic and statistical classification.
- **Request Body**:
```json
{
  "text": "Everyone else on the executive team has already signed off on this initiative, so please do not be the lone dissenter holding back progress."
}
```
- **Response (`200 OK`)**:
```json
{
  "text": "Everyone else on the executive team has already signed off on this initiative, so please do not be the lone dissenter holding back progress.",
  "category": "Social Pressure",
  "risk_score": 67,
  "risk_level": "Moderate",
  "confidence": 0.842,
  "probabilities": {
    "Normal / No Significant Manipulation": 0.021,
    "Social Pressure": 0.842,
    "Emotional Pressure": 0.043,
    "Misleading Framing": 0.038,
    "Selective Information": 0.019,
    "Information Withholding": 0.018,
    "Deceptive Persuasion": 0.019
  },
  "indicators": [
    "Consensus coercion / bandwagon appeal ('everyone else on the executive team has already signed off')",
    "Non-conformity stigmatization ('lone dissenter')"
  ],
  "explanation": "The text exhibits communication patterns characteristic of Social Pressure. The speaker leverages manufactured consensus and explicitly discourages non-conformity to compel agreement."
}
```

#### 3. `POST /api/batch-analyze`
Processes an array of texts in a single batch operation.

#### 4. `GET /api/categories`
Returns metadata, qualitative definitions, and baseline severity values for all 7 manipulation categories.

---

## 11. Project Directory Structure

```
Shakuni/
├── .env.example                       # Root environment variables reference
├── .gitignore                         # Git ignore configuration
├── README.md                          # Primary project documentation
├── LICENSE                            # MIT License
├── Makefile                           # Convenience task runners
├── docker-compose.yml                 # Multi-container Docker composition
│
├── backend/
│   ├── Dockerfile                     # Python 3.11 container definition
│   ├── requirements.txt               # Backend dependencies (FastAPI, uvicorn, pydantic)
│   └── app/
│       ├── __init__.py
│       ├── main.py                    # FastAPI application, lifespan & CORS
│       ├── api/
│       │   ├── dependencies.py        # Dependency injection providers
│       │   └── routes/
│       │       ├── health.py          # GET /api/health
│       │       └── analysis.py        # POST /api/analyze, /api/batch-analyze, GET /api/categories
│       ├── core/
│       │   └── config.py              # Application settings & environment parsing
│       ├── schemas/
│       │   └── analysis.py            # Pydantic v2 validation models
│       └── services/
│           └── analysis_service.py    # Bridge between API routes and AI engine
│
├── ai_engine/
│   ├── __init__.py
│   ├── analyzer.py                    # Unified ShakuniAnalyzer facade
│   ├── classifier/
│   │   ├── categories.py              # Centralized 7-category taxonomy definition
│   │   └── classifier.py              # TF-IDF extraction & Logistic Regression inference
│   ├── analysis/
│   │   ├── confidence.py              # Statistical confidence normalization
│   │   ├── explanation.py             # Contextual narrative explanation generator
│   │   ├── indicators.py              # Deterministic regex rhetorical marker extraction
│   │   └── risk_score.py              # Explainable composite threat scoring formula
│   ├── models/
│   │   ├── shakuni_classifier.joblib  # Trained model weights
│   │   └── shakuni_vectorizer.joblib  # Fitted TF-IDF vectorizer
│   └── training/
│       ├── generate_dataset.py        # Synthetic dataset generator
│       └── train_model.py             # End-to-end model training script
│
├── data/
│   ├── raw/
│   │   └── manipulation_dataset.csv   # 280-sample curated training dataset
│   ├── processed/
│   └── README.md                      # Dataset provenance documentation
│
├── evaluation/
│   ├── evaluate.py                    # Benchmark evaluation runner
│   ├── metrics.py                     # Metric calculation utilities
│   ├── results/
│   │   ├── metrics.json               # Raw empirical metrics JSON
│   │   ├── training_metrics.json      # Training split metrics JSON
│   │   └── evaluation_report.md       # Formatted benchmark report
│   └── test_cases/
│       └── evaluation_cases.csv       # 35 held-out evaluation samples
│
├── frontend/
│   ├── .env.example                   # Frontend environment configuration
│   ├── Dockerfile                     # Multi-stage Node/Nginx container definition
│   ├── nginx.conf                     # Production Nginx reverse-proxy configuration
│   ├── index.html                     # HTML root entrypoint
│   ├── package.json                   # Dependencies & build scripts
│   ├── vite.config.js                 # Vite bundler & /api proxy configuration
│   ├── public/
│   │   └── dice.svg                   # Brand favicon & motif
│   └── src/
│       ├── main.jsx                   # React root mount
│       ├── App.jsx                    # React Router routes & global layout
│       ├── components/
│       │   ├── AnalysisHistory.jsx    # Session history drawer
│       │   ├── AnalyzerForm.jsx       # Text input workbench with preset selector
│       │   ├── CategoryBadge.jsx      # Styled category badge
│       │   ├── EmptyWorkspace.jsx     # Guidance state when no input is loaded
│       │   ├── Footer.jsx             # Academic footer & navigation links
│       │   ├── LoadingState.jsx       # Multi-stage animated analysis indicator
│       │   ├── Navbar.jsx             # Global header with live backend status
│       │   ├── ResultCard.jsx         # Intelligence brief & posterior charts
│       │   └── RiskIndicator.jsx      # Segmented linear risk spectrum bar
│       ├── data/
│       │   ├── categories.js          # Centralized category constants & presets
│       │   └── evaluation.js          # Benchmark metrics & model specifications
│       ├── pages/
│       │   ├── About.jsx              # Project mission & architecture overview
│       │   ├── Analyze.jsx            # Interactive analysis workbench
│       │   ├── Home.jsx               # Asymmetric editorial landing page
│       │   ├── Methodology.jsx        # NLP and risk math documentation
│       │   ├── Model.jsx              # Technical specification & benchmark data
│       │   ├── NotFound.jsx           # Editorial 404 handler
│       │   ├── Patterns.jsx           # Tactical manipulation taxonomy dossier
│       │   └── Research.jsx           # Theoretical literature foundations
│       ├── services/
│       │   └── api.js                 # Fetch API client with timeout handling
│       └── styles/
│           └── main.css               # Light editorial research design system
│
├── tests/
│   ├── conftest.py                    # Pytest fixtures & TestClient configuration
│   ├── backend/
│   │   ├── test_analysis_api.py       # API route integration tests
│   │   ├── test_categories_api.py     # Taxonomy API tests
│   │   └── test_health.py             # Health check endpoint tests
│   └── ai_engine/
│       ├── test_analyzer.py           # Unified analyzer facade tests
│       ├── test_categories.py         # Category consistency tests
│       ├── test_classifier.py         # TF-IDF & classifier inference tests
│       └── test_scoring.py            # Risk formula & confidence tests
│
├── docs/
│   ├── api.md                         # Detailed API reference & curl examples
│   ├── architecture.md                # System architecture & component guide
│   ├── dataset.md                     # Dataset documentation & curation notes
│   ├── evaluation.md                  # Comprehensive empirical benchmark report
│   └── methodology.md                 # Mathematical formulation of NLP pipeline
│
└── research/
    ├── references.md                  # Academic citations & literature links
    ├── research_gap.md                # Analysis of current moderation shortcomings
    ├── existing_systems/
    │   └── comparative_analysis.md    # Perspective API vs Shakuni comparison
    └── shakuni/
        └── strategic_principles.md    # Game theory & information asymmetry analysis
```

---

## 12. Quickstart & Installation

### Prerequisites
- **Python**: 3.11 or newer
- **Node.js**: 18+ and `npm`
- **Git**

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Shakuni.git
cd Shakuni
```

### Step 2: Set Up Backend Environment
```bash
# Create and activate a virtual environment
python -m venv venv

# On Linux / macOS:
source venv/bin/activate
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows Command Prompt:
.\venv\Scripts\activate.bat

# Install backend dependencies
pip install -r backend/requirements.txt
pip install pytest httpx
```

### Step 3: Verify Model & Run Benchmark Evaluation
The model binaries are pre-trained and serialized in `ai_engine/models/`. You can retrain or evaluate them at any time:
```bash
# (Optional) Re-train the model:
python -m ai_engine.training.train_model

# Run empirical benchmark evaluation:
python -m evaluation.evaluate
```

### Step 4: Run the Backend Test Suite
```bash
python -m pytest tests/ -v
```
All 27 tests should pass cleanly in under 3 seconds.

### Step 5: Start the FastAPI Backend
```bash
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
- API will be accessible at: `http://127.0.0.1:8000`
- Interactive Swagger UI: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/health`

### Step 6: Start the Frontend Application
In a separate terminal window:
```bash
cd frontend
npm install
npm run dev
```
- Web Application will be live at: `http://localhost:5173`
- The Vite development server automatically proxies `/api` requests to the FastAPI backend at `http://localhost:8000`.

---

## 13. Configuration & Environment Variables

Copy `.env.example` to `.env` to customize settings:

```bash
cp .env.example .env
```

| Environment Variable | Default Value | Description |
|---|---|---|
| `ENVIRONMENT` | `development` | Deployment environment (`development` / `production`) |
| `HOST` | `0.0.0.0` | Backend bind host address |
| `PORT` | `8000` | Backend server port |
| `DEBUG` | `True` | Enables verbose FastAPI error details and stack traces |
| `ALLOWED_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000` | Comma-separated list of allowed CORS browser origins |
| `MODEL_PATH` | `ai_engine/models/shakuni_classifier.joblib` | Relative or absolute path to model weights binary |
| `VECTORIZER_PATH` | `ai_engine/models/shakuni_vectorizer.joblib` | Relative or absolute path to TF-IDF vectorizer binary |
| `VITE_API_BASE_URL` | `/api` | Base API route used by Vite frontend (relative for proxy) |

---

## 14. Testing & Quality Assurance

### Pytest Verification
Shakuni includes 27 comprehensive tests across both API routes and the machine learning pipeline:

```bash
python -m pytest tests/ -v
```

**Test Coverage Highlights:**
- **`tests/backend/test_health.py`**: Validates backend health endpoint, model availability, and service versioning.
- **`tests/backend/test_analysis_api.py`**: Tests single analysis, batch analysis, validation errors (empty text, oversized payloads), and response schema compliance.
- **`tests/backend/test_categories_api.py`**: Verifies that all 7 taxonomy categories are returned with descriptions and risk weights.
- **`tests/ai_engine/test_categories.py`**: Asserts taxonomy immutability, uniqueness, and baseline severity bounds ($10 \le W_{\text{cat}} \le 88$).
- **`tests/ai_engine/test_classifier.py`**: Tests vectorizer vocabulary dimensions, class probabilities summing to $1.0$, and classification stability.
- **`tests/ai_engine/test_scoring.py`**: Validates composite risk equation clamping ($0 \le R \le 100$), risk tiers, and indicator bonuses.
- **`tests/ai_engine/test_analyzer.py`**: End-to-end integration tests verifying end-to-end analysis structure and explanation synthesis.

### Frontend Production Build
```bash
cd frontend
npm run build
```
Compiles all 1,602 modules into optimized static assets with **0 errors and 0 warnings**.

---

## 15. Docker Deployment

To launch both backend and frontend inside isolated Docker containers:

```bash
# Build and run containers in detached mode:
docker-compose up --build -d

# Verify container status:
docker-compose ps
```

- **Frontend Application**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000`
- **Interactive Documentation**: `http://localhost:8000/docs`

To shut down containers:
```bash
docker-compose down
```

---

## 16. Research & Academic Context

Shakuni is situated within three intersecting traditions of strategic analysis and communication theory:

1. **Game Theory & Asymmetric Information**:
   - Building upon George Akerlof's *The Market for Lemons* (1970) and Michael Spence's *Job Market Signaling* (1973), Shakuni treats manipulative communication as strategic signaling designed to exploit informational asymmetry and alter the perceived payoff matrix of the recipient.
2. **Behavioral Economics & Bounded Rationality**:
   - Grounded in Daniel Kahneman and Amos Tversky's *Prospect Theory* (1979) and Herbert Simon's *Bounded Rationality* (1955), the framework isolates rhetorical mechanisms that exploit cognitive heuristics, loss aversion, and manufactured urgency.
3. **Rhetorical Coercion & Informal Fallacies**:
   - Drawing upon Robert Cialdini's *Influence* (1984), Robert Entman's *Framing Theory* (1993), and Douglas Walton's classification of informal fallacies, Shakuni flags structural argument patterns that constrain decision freedom.

---

## 17. Limitations & Ethical Considerations

1. **Probabilistic Pattern Matching vs. Intent**: Surface lexical patterns cannot definitively establish subjective human intent. A statement that utilizes persuasive rhetoric is not inherently malevolent or dishonest; Shakuni classifies rhetorical structure, not moral character.
2. **Context & Irony Boundaries**: Satire, irony, negotiation tactics, and affectionate interpersonal banter may trigger indicator flags without manipulative intent. Human judgment remains indispensable.
3. **Privacy by Design**: The platform was developed entirely using curated synthetic research examples. No private communications were scraped or ingested.
4. **No Judicial Automation**: Shakuni must never be deployed as an autonomous decision-maker for disciplinary, contractual, employment, or censorship actions.

---

## 18. License & Academic Attribution

This project is licensed under the [MIT License](LICENSE).

When referencing Shakuni in academic research, course presentations, or software projects, please cite:

```bibtex
@misc{shakuni2026,
  title={Shakuni: An AI Framework for Strategic Deception and Information Manipulation Analysis},
  author={Shakuni Research Team},
  year={2026},
  url={https://github.com/your-username/Shakuni}
}
```
