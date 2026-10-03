# Shakuni System Architecture

## Architectural Overview

Shakuni is engineered as a decoupled, layered full-stack application designed specifically for natural language analysis of strategic deception and manipulative communication patterns.

```mermaid
flowchart TD
    User([User / Browser])
    
    subgraph Frontend ["Frontend (React 18 + Vite)"]
        UI[UI Components]
        Form[AnalyzerForm Component]
        Visual[ResultCard & Risk Gauge]
        APIClient[API Service Module]
    end
    
    subgraph Backend ["Backend API (FastAPI)"]
        Main[FastAPI Router & CORS]
        Dep[Dependency Provider]
        Service[AnalysisService]
        Schema[Pydantic Validation Schemas]
    end
    
    subgraph Engine ["AI Engine (Scikit-Learn NLP)"]
        Analyzer[ShakuniAnalyzer Facade]
        Classifier[ShakuniClassifier]
        Indicators[Indicator Rule Matcher]
        Scorer[Risk & Confidence Engine]
        Explainer[Explanation Synthesizer]
        Model[(Serialized Model & TF-IDF Vectorizer)]
    end

    User -->|Enter text sample| Form
    Form -->|Trigger analysis| APIClient
    APIClient -->|POST /api/analyze| Main
    Main -->|Validate request| Schema
    Schema -->|Validated DTO| Service
    Service -->|Run pipeline| Analyzer
    
    Analyzer --> Classifier
    Analyzer --> Indicators
    Classifier --> Model
    Classifier --> Scorer
    Indicators --> Scorer
    Scorer --> Explainer
    
    Analyzer -->|Structured AnalysisResult| Service
    Service -->|AnalysisResponse JSON| Main
    Main -->|HTTP 200 JSON| APIClient
    APIClient --> Visual
    Visual -->|Render gauge, probabilities, indicators| User
```

## Detailed Component Breakdown

### 1. Frontend Layer (`frontend/`)
- **Framework**: React 18, Vite build tool.
- **Styling**: Native CSS modern dark theme with CSS custom properties (`var(--...)`), responsive layout grids, and accessible color contrasts.
- **Components**:
  - `AnalyzerForm.jsx`: Text input area, character counter, preset research test examples, submission state handling.
  - `ResultCard.jsx`: Multi-panel display orchestrating the category badge, probability horizontal bars, and explanation.
  - `RiskIndicator.jsx`: Animated SVG circular gauge mapping composite scores (0–100) into Low, Moderate, or High tiers.
  - `CategoryBadge.jsx`: Dynamic visual badge reflecting category iconography and color coding.
  - `LoadingState.jsx`: Rotating status indicators demonstrating pipeline execution steps.

### 2. Backend API Layer (`backend/app/`)
- **Framework**: FastAPI with asynchronous route handlers.
- **Configuration**: `Settings` class loading variables from `.env` (CORS origins, payload caps, debug toggles).
- **Validation**: Pydantic v2 schemas (`AnalysisRequest`, `BatchAnalysisRequest`, `AnalysisResponse`, `CategoriesResponse`, `HealthResponse`).
- **Error Handling**: Custom exception handlers with standard JSON envelopes.

### 3. AI / NLP Engine (`ai_engine/`)
- **Centralized Taxonomy** (`classifier/categories.py`): Single source of truth for all 7 manipulation categories, descriptions, typical indicators, and baseline risk weights.
- **Feature Extraction & Classification** (`classifier/classifier.py`): Text normalization, unigram/bigram TF-IDF vectorization, and multinomial logistic regression inference.
- **Linguistic Marker Extraction** (`analysis/indicators.py`): Rule-based pattern matcher identifying rhetorical strategies (e.g. false dichotomies, conformity demands, manufactured urgency).
- **Risk & Confidence Calculation** (`analysis/risk_score.py`, `analysis/confidence.py`): Mathematical scoring model combining model posterior probabilities, category base severity, and indicator density into a normalized 0–100 index.
- **Explanation Generator** (`analysis/explanation.py`): Human-readable synthesis citing specific linguistic evidence while enforcing non-absolute, probabilistic framing.
