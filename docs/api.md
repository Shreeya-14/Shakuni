# Shakuni API Documentation

Base URL: `http://localhost:8000/api`

Interactive Swagger UI: `http://localhost:8000/docs`  
Interactive ReDoc: `http://localhost:8000/redoc`

---

## 1. Health Check

### `GET /api/health`
Verifies backend operational status, framework version, and ML model availability.

#### Request Example
```bash
curl -X GET "http://localhost:8000/api/health"
```

#### Response Example (`200 OK`)
```json
{
  "status": "healthy",
  "service": "shakuni-api",
  "version": "1.0.0",
  "model_loaded": true
}
```

---

## 2. Text Analysis

### `POST /api/analyze`
Classifies a message into one of 7 manipulation categories, calculates an explainable risk score (0-100), statistical confidence, detected linguistic indicators, and full posterior probability distribution.

#### Request Headers
- `Content-Type: application/json`

#### Request Body Schema
```json
{
  "text": "string (1 - 10,000 characters, required)"
}
```

#### Request Example
```bash
curl -X POST "http://localhost:8000/api/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "Everyone else in the department has already agreed to the new policy, don'\''t be the lone dissenter holding us back."}'
```

#### Response Example (`200 OK`)
```json
{
  "text": "Everyone else in the department has already agreed to the new policy, don't be the lone dissenter holding us back.",
  "category": "Social Pressure",
  "risk_score": 67,
  "risk_level": "Moderate",
  "confidence": 0.8124,
  "explanation": "The communication pattern was classified as 'Social Pressure' with an estimated model certainty of 81%. This pattern typically involves: Communication that leverages bandwagon appeals, peer conformity, social shaming, consensus coercion, or fear of ostracization. Key rhetorical markers detected include: 'everyone else' (Social Conformity Demand), 'lone dissenter' (Social Conformity Demand). Note: This reflects an algorithmic pattern assessment and does not constitute a definitive judgment of intent.",
  "indicators": [
    {
      "name": "Social Conformity Demand",
      "matched_phrase": "everyone else",
      "category_relevance": "Social Pressure",
      "description": "Appeals to group consensus or highlights the target's deviation from peer behavior."
    },
    {
      "name": "Fear of Professional Ostracization",
      "matched_phrase": "holding us back",
      "category_relevance": "Social Pressure",
      "description": "Warns of reputational damage, social isolation, or peer judgment for non-compliance."
    }
  ],
  "probabilities": {
    "Normal / No Significant Manipulation": 0.0125,
    "Social Pressure": 0.8124,
    "Emotional Pressure": 0.0612,
    "Misleading Framing": 0.0381,
    "Selective Information": 0.0211,
    "Information Withholding": 0.0247,
    "Deceptive Persuasion": 0.0300
  }
}
```

---

## 3. Batch Analysis

### `POST /api/batch-analyze`
Analyzes multiple messages in a single request (1 to 50 items).

#### Request Body
```json
{
  "texts": [
    "The lab confirmed that the water sample adheres to municipal drinking safety guidelines.",
    "Our revolutionary battery technology demonstrated a four hundred percent charge retention in lab tests."
  ]
}
```

#### Response Example (`200 OK`)
```json
{
  "total_analyzed": 2,
  "results": [
    {
      "text": "The lab confirmed that the water sample adheres to municipal drinking safety guidelines.",
      "category": "Normal / No Significant Manipulation",
      "risk_score": 8,
      "risk_level": "Low",
      "confidence": 0.9412,
      "explanation": "The text exhibits standard, objective communication patterns (model certainty: 94%). No significant persuasive coercion, deceptive framing, or emotional pressure indicators were identified.",
      "indicators": [],
      "probabilities": { ... }
    },
    {
      "text": "Our revolutionary battery technology demonstrated a four hundred percent charge retention in lab tests.",
      "category": "Selective Information",
      "risk_score": 58,
      "risk_level": "Moderate",
      "confidence": 0.8245,
      "explanation": "The communication pattern was classified as 'Selective Information' with an estimated model certainty of 82%...",
      "indicators": [ ... ],
      "probabilities": { ... }
    }
  ]
}
```

---

## 4. Manipulation Categories Catalog

### `GET /api/categories`
Retrieves the centralized catalog of supported manipulation categories with metadata, examples, and baseline risk weights.

#### Response Example (`200 OK`)
```json
{
  "total_categories": 7,
  "categories": [
    {
      "id": "normal",
      "name": "Normal / No Significant Manipulation",
      "description": "Standard, neutral, objective, or transparent communication exhibiting no significant coercive, deceptive, or manipulative tactics.",
      "examples": [ ... ],
      "typical_linguistic_indicators": [ ... ],
      "risk_interpretation": "Minimal risk of undue influence.",
      "base_risk_weight": 10.0
    },
    ...
  ]
}
```

---

## 5. Error Responses

### Validation Error (`422 Unprocessable Entity`)
```json
{
  "error": "Validation Error",
  "message": "Input text must contain at least one non-whitespace character.",
  "field": "body -> text",
  "details": [ ... ]
}
```
