import React from 'react';
import { MODEL_SPECS, EVALUATION_METRICS } from '../data/evaluation';
import { 
  Cpu, 
  Binary, 
  Database, 
  CheckCircle2, 
  AlertTriangle, 
  Sliders, 
  BarChart3, 
  Table,
  Layers,
  ShieldAlert
} from 'lucide-react';

export default function Model() {
  const { accuracy, macroPrecision, macroRecall, macroF1, perCategory, confusionMatrix } = EVALUATION_METRICS;

  return (
    <article className="editorial-monograph" role="article">
      {/* Header */}
      <header className="monograph-header">
        <span className="monograph-ref">TECHNICAL SPECIFICATION // AI ARCHITECTURE</span>
        <h1 className="monograph-title">Inside the Intelligence Layer</h1>
        <p className="monograph-abstract">
          Complete transparency into natural language feature extraction, multinomial logistic calibration, and verified benchmark performance from the Shakuni research evaluation pipeline.
        </p>
      </header>

      {/* 1. Core Model Specs Grid */}
      <section className="monograph-section">
        <span className="monograph-sec-number">ARCHITECTURE OVERVIEW</span>
        <h2 className="monograph-sec-title">
          <Cpu size={20} color="var(--brand-burgundy)" />
          Classifier Specifications
        </h2>
        
        <div className="model-specs-grid">
          <div className="model-spec-card">
            <span className="spec-card-label">CLASSIFIER ALGORITHM</span>
            <strong className="spec-card-value">Multinomial Logistic Softmax</strong>
            <p className="spec-card-desc">L2-regularized convex optimization with balanced class weighting for calibrated posterior probabilities.</p>
          </div>

          <div className="model-spec-card">
            <span className="spec-card-label">VECTOR REPRESENTATION</span>
            <strong className="spec-card-value">Sublinear TF-IDF (1–2 N-Grams)</strong>
            <p className="spec-card-desc">Captures unigram lexemes and tactical bigram pairings across 4,595 distinct vocabulary features.</p>
          </div>

          <div className="model-spec-card">
            <span className="spec-card-label">BENCHMARK DATASET</span>
            <strong className="spec-card-value">280 Balanced Curated Samples</strong>
            <p className="spec-card-desc">Uniform stratification: 40 samples across each of the 7 manipulation taxonomy categories.</p>
          </div>

          <div className="model-spec-card">
            <span className="spec-card-label">EVALUATION SPLIT</span>
            <strong className="spec-card-value">Stratified Holdout Test Split</strong>
            <p className="spec-card-desc">Rigorous test partition maintaining exact class distribution balance without data leakage.</p>
          </div>
        </div>
      </section>

      {/* 2. Real Benchmark Performance Metrics */}
      <section className="monograph-section">
        <span className="monograph-sec-number">EVALUATION BENCHMARK</span>
        <h2 className="monograph-sec-title">
          <CheckCircle2 size={20} color="var(--brand-burgundy)" />
          Verified Test-Set Performance
        </h2>
        <p>
          Evaluation metrics generated from the official test holdout suite (`evaluation/results/metrics.json`):
        </p>

        <div className="metrics-banner-grid">
          <div className="metric-banner-item">
            <span className="banner-metric-label">OVERALL ACCURACY</span>
            <strong className="banner-metric-value">{Math.round(accuracy * 1000) / 10}%</strong>
            <span className="banner-metric-sub">Across 7 Categories</span>
          </div>

          <div className="metric-banner-item">
            <span className="banner-metric-label">MACRO PRECISION</span>
            <strong className="banner-metric-value">{Math.round(macroPrecision * 1000) / 10}%</strong>
            <span className="banner-metric-sub">Unweighted Class Average</span>
          </div>

          <div className="metric-banner-item">
            <span className="banner-metric-label">MACRO RECALL</span>
            <strong className="banner-metric-value">{Math.round(macroRecall * 1000) / 10}%</strong>
            <span className="banner-metric-sub">Unweighted Sensitivity</span>
          </div>

          <div className="metric-banner-item">
            <span className="banner-metric-label">MACRO F1-SCORE</span>
            <strong className="banner-metric-value">{Math.round(macroF1 * 1000) / 10}%</strong>
            <span className="banner-metric-sub">Harmonic Precision/Recall Mean</span>
          </div>
        </div>
      </section>

      {/* 3. Per-Category Performance Breakdown Table */}
      <section className="monograph-section">
        <span className="monograph-sec-number">CATEGORY BREAKDOWN</span>
        <h2 className="monograph-sec-title">
          <BarChart3 size={20} color="var(--brand-burgundy)" />
          Per-Category Precision, Recall & F1
        </h2>
        <p>
          Detailed breakdown demonstrating consistent discrimination across subtle and overt persuasion forms:
        </p>

        <div className="research-table-wrapper">
          <table className="research-table">
            <thead>
              <tr>
                <th>Code</th>
                <th>Category</th>
                <th style={{ textAlign: 'right' }}>Precision</th>
                <th style={{ textAlign: 'right' }}>Recall</th>
                <th style={{ textAlign: 'right' }}>F1-Score</th>
                <th style={{ textAlign: 'right' }}>Test Support</th>
              </tr>
            </thead>
            <tbody>
              {perCategory.map((row) => (
                <tr key={row.code}>
                  <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.78rem', color: 'var(--brand-burgundy)' }}>
                    {row.code}
                  </td>
                  <td style={{ fontWeight: 500, color: 'var(--text-primary)' }}>
                    {row.category}
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'var(--font-mono)' }}>
                    {(row.precision * 100).toFixed(1)}%
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'var(--font-mono)' }}>
                    {(row.recall * 100).toFixed(1)}%
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'var(--font-mono)', fontWeight: 600, color: 'var(--brand-burgundy)' }}>
                    {(row.f1 * 100).toFixed(1)}%
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'var(--font-mono)', color: 'var(--text-muted)' }}>
                    {row.support}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* 4. Confusion Matrix Visualization */}
      <section className="monograph-section">
        <span className="monograph-sec-number">ERROR ANALYSIS</span>
        <h2 className="monograph-sec-title">
          <Table size={20} color="var(--brand-burgundy)" />
          Holdout Confusion Matrix
        </h2>
        <p>
          Rows represent the <strong>True Label</strong>; columns represent the <strong>Predicted Label</strong>. Diagonal elements signify correct classifications:
        </p>

        <div className="research-table-wrapper">
          <table className="research-table confusion-matrix-table">
            <thead>
              <tr>
                <th style={{ width: '130px' }}>True \ Pred</th>
                {confusionMatrix.labels.map((lbl, idx) => (
                  <th key={idx} style={{ textAlign: 'center', fontSize: '0.7rem' }}>
                    {lbl}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {confusionMatrix.matrix.map((row, rIdx) => (
                <tr key={rIdx}>
                  <td style={{ fontWeight: 600, fontSize: '0.78rem', color: 'var(--text-primary)' }}>
                    {confusionMatrix.labels[rIdx]}
                  </td>
                  {row.map((val, cIdx) => {
                    const isDiagonal = rIdx === cIdx;
                    const cellBg = isDiagonal && val > 0 
                      ? 'rgba(122, 28, 48, 0.12)' 
                      : val > 0 
                        ? 'rgba(217, 83, 79, 0.18)' 
                        : 'transparent';
                    const textColor = isDiagonal && val > 0 
                      ? 'var(--brand-burgundy)' 
                      : val > 0 
                        ? '#a61c33' 
                        : 'var(--text-muted)';
                    return (
                      <td 
                        key={cIdx} 
                        style={{ 
                          textAlign: 'center', 
                          background: cellBg,
                          color: textColor,
                          fontWeight: val > 0 ? 700 : 400,
                          fontFamily: 'var(--font-mono)',
                          fontSize: '0.85rem'
                        }}
                      >
                        {val}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <span style={{ display: 'block', marginTop: '0.5rem', fontSize: '0.75rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
          * Evaluated on holdout test partition of 35 stratified samples (5 per category).
        </span>
      </section>

      {/* 5. Mathematical Formulations */}
      <section className="monograph-section">
        <span className="monograph-sec-number">MATHEMATICAL FORMULATIONS</span>
        <h2 className="monograph-sec-title">
          <Binary size={20} color="var(--brand-burgundy)" />
          Feature Extraction & Probability Calibration
        </h2>
        
        <p><strong>1. Sublinear Term Frequency Inverse Document Frequency (TF-IDF):</strong></p>
        <div className="monograph-formula-box">
          {"TF-IDF(t, d, D) = [1 + ln(count(t, d))] × [ln((1 + |D|) / (1 + DF(t, D))) + 1]"}
        </div>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
          Sublinear scaling prevents high-frequency terms from overwhelming subtle rhetorical bigram markers.
        </p>

        <p style={{ marginTop: '1.25rem' }}><strong>2. Multinomial Softmax Posterior Distribution:</strong></p>
        <div className="monograph-formula-box">
          {"P(y = c | x) = exp(w_c^T x + b_c) / Σ_j exp(w_j^T x + b_j)"}
        </div>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
          Transforms unconstrained linear outputs into a calibrated continuous probability distribution summing to 1.0.
        </p>

        <p style={{ marginTop: '1.25rem' }}><strong>3. Explainable Composite Risk Scoring Index:</strong></p>
        <div className="monograph-formula-box">
          {"Risk Score = Clamp[ (W_cat × 0.45) + (P_manip × 30.0) + (Confidence × 12.0) + I_mod, 0, 100 ]"}
        </div>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
          Synthesizes baseline categorical severity (10–88), non-normal probability mass, model confidence, and detected syntactic indicator density.
        </p>
      </section>

      {/* 6. Prominent Model Limitations */}
      <section className="monograph-section">
        <span className="monograph-sec-number">MODEL BOUNDARIES</span>
        <h2 className="monograph-sec-title">
          <AlertTriangle size={20} color="var(--brand-burgundy)" />
          Important Methodological Limitations
        </h2>

        <div className="limitation-callout-card">
          <h4>Academic & Methodological Scope</h4>
          <ul style={{ paddingLeft: '1.25rem', marginTop: '0.75rem', lineHeight: '1.8', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
            <li><strong>Dataset Scale</strong>: Trained on 280 carefully curated research examples. While sufficient for linear n-gram boundaries, performance on highly informal slang may vary.</li>
            <li><strong>Probabilistic Predictions</strong>: Model scores represent statistical resemblance to training patterns, not absolute truth or definitive deceit.</li>
            <li><strong>Confidence vs Truthfulness</strong>: High model confidence indicates strong pattern congruence with the training data, NOT that an author is definitely deceptive.</li>
            <li><strong>Domain Sensitivity</strong>: Legal disclaimers, medical warnings, and corporate acquisitions employ domain-specific framing that may trigger false-positive pressure markers without human context.</li>
          </ul>
        </div>
      </section>
    </article>
  );
}
