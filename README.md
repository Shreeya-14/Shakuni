# Shakuni: An AI Framework for Strategic Deception and Information Manipulation Analysis

[![CI Pipeline](https://github.com/shakuni-project/shakuni/actions/workflows/ci.yml/badge.svg)](https://github.com/shakuni-project/shakuni/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-teal.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![React + Vite](https://img.shields.io/badge/Frontend-React_18_+_Vite-61dafb.svg)](https://vitejs.dev/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-f7931e.svg)](https://scikit-learn.org/)

---

## 1. Project Overview

**Shakuni** is a full-stack, research-grade natural language processing framework designed to identify and analyze **strategic deception, coercive rhetoric, and information manipulation patterns** in textual communication.

Named after the classical strategist archetype known for manipulating decision spaces through psychological priming and loaded scenarios, Shakuni explores how modern deceptive persuasion operates: not merely through crude factual lies or explicit toxicity, but through **subtle framing, peer coercion, guilt leverage, selective presentation, and calculated withholding**.

> **Important Research Prototype Notice:**  
> Shakuni analyzes *probabilistic linguistic communication patterns*. It is **NOT** a "lie detector" and does not claim to objectively determine whether a human speaker is lying or whether their subjective moral intent is deceptive. All classifications reflect statistical similarity against documented rhetorical structures.

---

## 2. Problem Statement & Motivation

Existing online safety systems suffer from critical blind spots:
- **Toxicity Classifiers (e.g. Perspective API)** focus almost exclusively on profanity, hate speech, and overt aggression. Polite, manipulative coercion (such as corporate gaslighting or contractual pressure) sails through undetected.
- **Automated Fact-Checkers** verify verifiable historical claims against databases, yet fail when statements are technically true but selectively cherry-picked or deceptively framed.
- **Binary Sentiment Classifiers** reduce nuanced discourse to positive or negative valence, obscuring toxic pressure cloaked in urgency or enthusiasm.

Shakuni addresses this research gap by providing a specialized typology, an explainable machine learning classifier, and a transparent risk-scoring engine focused specifically on **how information is packaged and weaponized**.

---

## 3. Key Features

- **7-Category Manipulation Taxonomy**: Centralized definition catalog across 7 distinct communication patterns.
- **True Machine Learning Pipeline**: TF-IDF n-gram vectorization with Multinomial Logistic Regression trained on a balanced dataset (no hardcoded `if text contains X` prediction rules).
- **Transparent Composite Risk Scoring**: Calculates an explainable 0–100 risk score based on model confidence, category baseline severity, manipulation probability mass, and linguistic marker density.
- **Statistical Confidence & Probability Distributions**: Full posterior probabilities across all 7 categories.
- **Linguistic Indicator Detection**: Pattern engine flagging specific rhetorical markers (e.g. false dichotomies, conformity demands, manufactured urgency).
- **Accessible Contextual Explanations**: Plain-English rationale generated for non-technical users while preserving epistemic humility.
- **Modern Dark UI**: Polished, responsive React interface with circular SVG gauges, probability horizontal bars, indicator chips, and research documentation views.
- **Production-Ready Backend**: FastAPI with strict Pydantic schemas, dependency injection, CORS configuration, and comprehensive pytest coverage.

---

## 4. Manipulation Categories

Defined centrally in `ai_engine/classifier/categories.py`:

| # | Category Name | Core Description | Typical Indicators | Base Risk |
|---|---|---|---|:---:|
| 1 | **Normal / No Significant Manipulation** | Objective, balanced, and neutral communication with no coercive tactics. | Objective tone, factual assertions, balanced context | 10 / 100 |
| 2 | **Social Pressure** | Bandwagon appeals, consensus coercion, and fear of professional or social ostracization. | *"everyone agrees"*, *"lone dissenter"*, *"let the team down"* | 65 / 100 |
| 3 | **Emotional Pressure** | Guilt trips, emotional blackmail, panic-inducing urgency, and sympathy exploitation. | *"if you really cared"*, *"on your conscience"*, *"ruin my life"* | 72 / 100 |
| 4 | **Misleading Framing** | False dichotomies, euphemistic corporate recontextualization, and loaded terminology. | *"either ... or"*, *"rightsizng"*, *"synergy"*, *"war on"* | 60 / 100 |
| 5 | **Selective Information** | Cherry-picking favorable statistics and isolated testimonials while omitting counter-evidence. | *"100% record"*, *"400% surge"*, *"every customer doubled"* | 52 / 100 |
| 6 | **Information Withholding** | Conspicuously concealing material caveats, recurring fees, or restrictive terms. | *"completely free"*, *"just click agree"*, *"no upfront"* | 75 / 100 |
| 7 | **Deceptive Persuasion** | Fabricated authority, zero-risk promises, pretexts, and false official directives. | *"CEO personally authorized"*, *"100% risk-free"*, *"secretly approved"* | 88 / 100 |

---

## 5. System Architecture

```
User (Browser) 
      │
      ▼
React 18 + Vite Frontend (Port 5173 / Docker 3000)
      │
      ▼ HTTP POST /api/analyze
FastAPI Backend (Port 8000)
      │
      ├──> Pydantic Request Validation
      │
      └──> Shakuni AI Engine
            │
            ├──> Text Normalization & Tokenization
            ├──> TF-IDF Unigram/Bigram Vectorizer
            ├──> Logistic Regression Inference (Probabilities)
            ├──> Linguistic Indicator Matcher (Rhetorical Rules)
            ├──> Transparent Risk Scoring Engine (0-100)
            └──> Contextual Narrative Explainer
```

---

## 6. Dataset & Methodology

### Dataset Provenance
All training and evaluation data are explicitly documented as **`synthetic/curated research examples`**:
- **Training Set (`data/raw/manipulation_dataset.csv`)**: 280 balanced samples (40 per category).
- **Benchmark Evaluation Set (`evaluation/test_cases/evaluation_cases.csv`)**: 35 held-out samples (5 per category).

### Preprocessing & Training
1. Text normalization and punctuation preservation.
2. Stratified 80/20 train/test split with fixed random seed (`42`).
3. TF-IDF feature extraction with sublinear term-frequency scaling and unigram/bigram captures (vocabulary size: 4,595 features).
4. Regularized Logistic Regression with balanced class weights.

---

## 7. Model Evaluation (Actual Empirical Results)

The following metrics were obtained by running the actual trained model against the held-out benchmark dataset:

```bash
python -m evaluation.evaluate
```

### Empirical Results Summary ($N = 35$ Held-Out Cases)

| Metric | Measured Value |
|:---|:---:|
| **Overall Accuracy** | **91.43%** |
| **Macro-Averaged Precision** | **0.9238** |
| **Macro-Averaged Recall** | **0.9143** |
| **Macro-Averaged F1-Score** | **0.9137** |
| **Weighted-Averaged F1-Score** | **0.9137** |

### Per-Category Breakdown

| Category | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Normal / No Significant Manipulation** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Social Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Emotional Pressure** | 1.0000 | 1.0000 | 1.0000 | 5 |
| **Misleading Framing** | 1.0000 | 0.8000 | 0.8889 | 5 |
| **Selective Information** | 0.8333 | 1.0000 | 0.9091 | 5 |
| **Information Withholding** | 0.8000 | 0.8000 | 0.8000 | 5 |
| **Deceptive Persuasion** | 1.0000 | 0.8000 | 0.8889 | 5 |

*Complete confusion matrix and error analysis are documented in [docs/evaluation.md](docs/evaluation.md).*

---

## 8. Transparent Risk Scoring Formula

The Risk Score ($R \in [0, 100]$) combines multiple explainable factors:
$$\text{Risk Score} = \text{Clamp}\left[ (W_{\text{cat}} \times 0.45) + (P_{\text{manip}} \times 30.0) + (\text{Confidence} \times 12.0) + I_{\text{mod}}, 0, 100 \right]$$

- **$W_{\text{cat}}$**: Baseline category severity (10 for Normal, up to 88 for Deceptive Persuasion).
- **$P_{\text{manip}}$**: Probability mass assigned to non-normal categories ($1.0 - P(\text{Normal})$).
- **$I_{\text{mod}}$**: Indicator density bonus (+4 for category-congruent rhetorical markers, capped at 20).
- **Tiers**: 0–39 (**Low**), 40–69 (**Moderate**), 70–100 (**High**).

---

## 9. Repository Structure

```
Shakuni/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                     # Continuous integration workflow
│   │   └── deploy.yml                 # Environment-driven deployment workflow
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI entrypoint, middleware, lifespan
│   │   ├── api/
│   │   │   ├── dependencies.py        # Dependency injection providers
│   │   │   └── routes/
│   │   │       ├── health.py          # GET /api/health
│   │   │       └── analysis.py        # POST /api/analyze, /api/batch-analyze, GET /api/categories
│   │   ├── core/
│   │   │   └── config.py              # Environment configuration & settings
│   │   ├── schemas/
│   │   │   └── analysis.py            # Pydantic request/response models
│   │   └── services/
│   │       └── analysis_service.py    # Bridge between API and AI engine
│   ├── requirements.txt
│   └── Dockerfile
│
├── ai_engine/
│   ├── __init__.py
│   ├── analyzer.py                    # Unified ShakuniAnalyzer facade
│   ├── classifier/
│   │   ├── categories.py              # Centralized category taxonomy
│   │   └── classifier.py              # TF-IDF & LogisticRegression inference
│   ├── analysis/
│   │   ├── indicators.py              # Regex rhetorical marker extraction
│   │   ├── confidence.py              # Statistical confidence normalization
│   │   ├── risk_score.py              # Transparent composite risk scorer
│   │   └── explanation.py             # Plain-language narrative explanation generator
│   ├── training/
│   │   ├── generate_dataset.py        # Synthetic dataset generator
│   │   └── train_model.py             # End-to-end model training script
│   └── models/
│       ├── shakuni_classifier.joblib  # Trained model weights
│       └── shakuni_vectorizer.joblib  # Fitted TF-IDF vectorizer
│
├── data/
│   ├── raw/
│   │   └── manipulation_dataset.csv   # 280-sample curated dataset
│   ├── processed/
│   └── README.md
│
├── evaluation/
│   ├── test_cases/
│   │   └── evaluation_cases.csv       # 35 held-out evaluation cases
│   ├── evaluate.py                    # Empirical evaluation runner
│   ├── metrics.py                     # Metric calculation utilities
│   └── results/
│       ├── metrics.json               # Raw metrics JSON
│       ├── training_metrics.json      # Training split metrics JSON
│       └── evaluation_report.md       # Formatted markdown benchmark report
│
├── frontend/
│   ├── public/
│   │   └── dice.svg                   # Brand favicon & motif
│   ├── src/
│   │   ├── components/
│   │   │   ├── AnalyzerForm.jsx       # Input form with character limits & pills
│   │   │   ├── ResultCard.jsx         # Visual results, bars, and chips
│   │   │   ├── RiskIndicator.jsx      # SVG circular risk gauge
│   │   │   ├── CategoryBadge.jsx      # Styled category badge
│   │   │   └── LoadingState.jsx       # Animated execution steps
│   │   ├── pages/
│   │   │   ├── Home.jsx               # Main analyzer interface
│   │   │   ├── Methodology.jsx        # NLP and risk math documentation
│   │   │   └── Research.jsx           # Conceptual foundations & academic literature
│   │   ├── services/
│   │   │   └── api.js                 # Frontend API client
│   │   ├── styles/
│   │   │   └── main.css               # Clean modern dark theme design system
│   │   ├── App.jsx                    # Root application component
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── nginx.conf                     # Nginx configuration for Docker
│   └── Dockerfile
│
├── tests/
│   ├── conftest.py                    # Session fixtures & TestClient
│   ├── backend/
│   │   ├── test_health.py
│   │   ├── test_analysis_api.py
│   │   └── test_categories_api.py
│   └── ai_engine/
│       ├── test_categories.py
│       ├── test_classifier.py
│       ├── test_scoring.py
│       └── test_analyzer.py
│
├── research/
│   ├── shakuni/
│   │   └── strategic_principles.md    # Asymmetric information game theory
│   ├── existing_systems/
│   │   └── comparative_analysis.md    # Perspective API vs Shakuni comparison
│   ├── research_gap.md                # Research gap in polite manipulation
│   └── references.md                  # Real academic citations
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── dataset.md
│   ├── methodology.md
│   └── evaluation.md
│
├── .env.example
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                            # MIT License
├── docker-compose.yml
└── Makefile
```

---

## 10. Local Setup & Installation

### Prerequisites
- Python 3.11+
- Node.js 18+ and npm
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Shakuni.git
cd Shakuni
```

### 2. Configure Python Backend
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
pip install pytest httpx
```

### 3. Train the Model & Run Evaluation
```bash
# Train ML model
python -m ai_engine.training.train_model

# Run evaluation on held-out test suite
python -m evaluation.evaluate
```

### 4. Run Test Suite
```bash
python -m pytest tests/ -v
```

### 5. Start Backend Server
```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```
Backend will be live at `http://localhost:8000`. Interactive API documentation available at `http://localhost:8000/docs`.

### 6. Set Up and Launch Frontend
In a new terminal window:
```bash
cd frontend
npm install
npm run dev
```
Frontend will be accessible at `http://localhost:5173`.

---

## 11. Docker Setup

To run the entire full-stack application inside isolated containers:

```bash
docker-compose up --build
```

- **Frontend**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000`
- **API Docs**: `http://localhost:8000/docs`

To stop the containers:
```bash
docker-compose down
```

---

## 12. Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Default Value | Description |
|---|---|---|
| `ENVIRONMENT` | `development` | Runtime environment mode |
| `DEBUG` | `True` | Enable verbose debugging and error details |
| `HOST` | `0.0.0.0` | Backend bind host |
| `PORT` | `8000` | Backend bind port |
| `ALLOWED_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Comma-separated allowed CORS origins |
| `MODEL_PATH` | `ai_engine/models/shakuni_classifier.joblib` | Path to serialized classification model |
| `VECTORIZER_PATH` | `ai_engine/models/shakuni_vectorizer.joblib` | Path to serialized TF-IDF vectorizer |
| `VITE_API_BASE_URL` | `http://localhost:8000/api` | API Base URL consumed by Vite frontend |

---

## 13. Limitations & Ethical Safeguards

1. **Descriptive, Not Judicial**: Shakuni identifies stylistic, lexical, and structural rhetoric that resembles documented manipulation tactics. It cannot evaluate external truth or moral honesty.
2. **Context Blindness**: Sarcasm, interpersonal banter, or domain-specific jargon may alter meaning beyond surface-level text.
3. **Human-in-the-Loop Requirement**: Outputs must never be used as automated justification for disciplinary actions, content removal, or contractual disqualification without independent human review.

---

## 14. Screenshots Placeholder

*(Screenshots of the UI, Circular Gauge, Probability Bars, and Methodology view will be placed here prior to viva presentation)*

---

## 15. Live Demo Placeholder

*(Live deployment URL will be linked here upon staging cloud rollout. Deployment is fully configured via `.github/workflows/deploy.yml` and `docker-compose.yml`.)*

---

## 16. Academic & Team Contributions

- **Project Lead / Research Author**: [College Student / Research Contributor Placeholder]
- **Academic Advisor / Department**: [Department of Computer Science & Engineering Placeholder]
- **Institution**: [University / College Name Placeholder]

---

## 17. License

This project is licensed under the [MIT License](LICENSE).
