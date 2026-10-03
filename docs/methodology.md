# Shakuni Analytical Methodology

## 1. Mathematical Formulation of NLP Pipeline

### 1.1 Text Normalization
Every input string $s$ undergoes lowercasing, unicode normalization (stripping accents), and whitespace regularization:
$$s' = \text{RegexReplace}(s, \text{pattern} = \texttt{\\s+}, \text{repl} = \text{" "})$$

### 1.2 TF-IDF Feature Extraction
We employ sublinear term frequency scaling across unigram and bigram ranges:
$$\text{TF}(t, d) = 1 + \ln(\text{count}(t, d)) \quad \text{if count}(t, d) > 0$$
$$\text{IDF}(t, D) = \ln\left(\frac{1 + |D|}{1 + \text{DF}(t, D)}\right) + 1$$
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

Features are normalized using the Euclidean $L_2$ norm:
$$\mathbf{x} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2}$$

### 1.3 Interpretable Classification: Multinomial Logistic Regression
Given feature vector $\mathbf{x} \in \mathbb{R}^V$, the probability that the text belongs to category $c \in \{1, \dots, 7\}$ is modeled via the softmax function:
$$P(y = c \mid \mathbf{x}) = \frac{\exp(\mathbf{w}_c^T \mathbf{x} + b_c)}{\sum_{j=1}^7 \exp(\mathbf{w}_j^T \mathbf{x} + b_j)}$$

Objective function minimized with $L_2$ penalty:
$$\min_{\mathbf{w}, b} \left[ -\sum_{i=1}^N \sum_{c=1}^7 \mathbb{I}(y_i = c) \ln P(y_i = c \mid \mathbf{x}_i) + \frac{1}{2C} \sum_{c=1}^7 \|\mathbf{w}_c\|_2^2 \right]$$
where $C = 2.5$, class weights are inverse-frequency balanced, and optimization utilizes the L-BFGS solver.

---

## 2. Statistical Confidence Estimation

Confidence represents the classifier's posterior probability margin over its learned vocabulary:
$$\text{Confidence} = \max_{c \in \{1, \dots, 7\}} P(y = c \mid \mathbf{x})$$

> **Important Distinction**: Statistical confidence reflects classification margin against historical training distributions; it does **not** measure factual truthfulness or the moral honesty of the speaker.

---

## 3. Explainable Risk Scoring Engine

The Shakuni Risk Score $R \in [0, 100]$ evaluates the intensity of deceptive and manipulative persuasion patterns.

### 3.1 Parameters
1. **Base Category Severity ($W_{\text{cat}}$)**:
   - *Normal / No Significant Manipulation*: 10.0
   - *Selective Information*: 52.0
   - *Misleading Framing*: 60.0
   - *Social Pressure*: 65.0
   - *Emotional Pressure*: 72.0
   - *Information Withholding*: 75.0
   - *Deceptive Persuasion*: 88.0

2. **Manipulation Mass Probability ($P_{\text{manip}}$)**:
   $$P_{\text{manip}} = \sum_{c \neq \text{Normal}} P(y = c \mid \mathbf{x}) = 1.0 - P(y = \text{Normal} \mid \mathbf{x})$$

3. **Linguistic Indicator Density ($I_{\text{mod}}$)**:
   $$I_{\text{mod}} = \min\left(20, \sum_{k \in \mathcal{K}} \begin{cases} 4.0 & \text{if } \text{cat}(k) = c^* \\ 2.0 & \text{otherwise} \end{cases}\right)$$

### 3.2 Scoring Equation
For texts classified as manipulative ($c^* \neq \text{Normal}$):
$$R = \text{round}\left( \text{clamp}\left( (W_{\text{cat}} \times 0.45) + (P_{\text{manip}} \times 30.0) + (\text{Confidence} \times 12.0) + I_{\text{mod}}, 0, 100 \right) \right)$$

For texts classified as Normal ($c^* = \text{Normal}$):
$$R = \text{round}\left( \text{clamp}\left( (W_{\text{cat}} \times 0.50) + (P_{\text{manip}} \times 20.0) + \min(I_{\text{mod}}, 8.0), 0, 100 \right) \right)$$

### 3.3 Risk Tier Mapping
- **0 – 39**: **Low Risk** (predominantly objective, routine communication).
- **40 – 69**: **Moderate Risk** (presence of subtle framing, selective disclosures, or social appeals).
- **70 – 100**: **High Risk** (acute emotional coercion, calculated information withholding, or fabricated authority).

---

## 4. Explanation Generation Pipeline

The explanation module translates statistical and linguistic evidence into clear natural language prose:
1. Primary classification attribution and model certainty percentage.
2. Conceptual definition of the predicted communication pattern.
3. Citation of extracted linguistic markers (e.g. *"Everyone else has already signed"*).
4. Explicit research caveat disclaiming absolute determination of personal deception.
