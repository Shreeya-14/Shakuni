import React from 'react';
import CategoryBadge from './CategoryBadge';
import RiskIndicator from './RiskIndicator';
import { Tag, BarChart3, ShieldAlert, Compass, Gauge, CheckCircle2, FileText, CornerDownRight } from 'lucide-react';

export default function ResultCard({ result }) {
  if (!result) return null;

  const {
    text,
    category,
    risk_score,
    risk_level,
    confidence,
    explanation,
    indicators = [],
    probabilities = {}
  } = result;

  const confidencePct = Math.round((confidence || 0) * 100);

  // Sort probabilities descending
  const sortedProbabilities = Object.entries(probabilities).sort(
    ([, a], [, b]) => b - a
  );

  return (
    <div className="analysis-report-container" role="region" aria-label="Analysis Results Dossier">
      <div className="report-document">
        {/* Top Report Metadata Strip */}
        <div className="report-top-strip">
          <div>
            <span style={{ color: 'var(--brand-burgundy)', fontWeight: 700 }}>DOSSIER // </span>
            CLASSIFICATION BRIEF
          </div>
          <div>
            CONTEXTUAL LANGUAGE MODEL &bull; CALIBRATED EVIDENCE SOFTMAX
          </div>
        </div>

        {/* Lead Category Banner */}
        <div className="report-lead-section">
          <div className="report-category-eyebrow">DETECTED COMMUNICATION PATTERN</div>
          <h2 className="report-category-heading">{category}</h2>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.85rem', flexWrap: 'wrap' }}>
            <CategoryBadge category={category} />
            {text && (
              <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.74rem', color: 'var(--text-muted)' }}>
                Sample length: {text.length.toLocaleString()} chars
              </span>
            )}
          </div>
        </div>

        {/* Two-Column Key Metrics: Composite Risk Index & Model Confidence */}
        <div className="report-metrics-grid">
          <div className="metric-card-block">
            <div className="metric-card-title">
              <Gauge size={13} color="var(--brand-burgundy)" />
              <span>Composite Threat & Risk Profile</span>
            </div>
            <RiskIndicator score={risk_score} level={risk_level} />
          </div>

          <div className="metric-card-block">
            <div className="metric-card-title">
              <CheckCircle2 size={13} color="var(--brand-burgundy)" />
              <span>Model Classification Confidence</span>
            </div>
            <div className="confidence-display-row">
              <span className="confidence-big-pct">{confidencePct}%</span>
            </div>
            <p className="confidence-description">
              Estimated posterior probability mass assigned to the identified pattern under the fine-tuned contextual model with evidence-based uncertainty calibration.
            </p>
          </div>
        </div>

        {/* Body Content: Explanation, Indicators, Probability Distribution */}
        <div className="report-content-body">
          {/* Qualitative Rationale */}
          <div>
            <div className="section-label-bar">
              <Compass size={13} />
              <span>Contextual Pattern Analysis & Qualitative Rationale</span>
            </div>
            <div className="editorial-explanation-box">
              {explanation}
            </div>
          </div>

          {/* Potential Linguistic Indicators */}
          <div>
            <div className="section-label-bar">
              <Tag size={13} />
              <span>Potential Rhetorical Indicators Isolated ({indicators.length})</span>
            </div>

            {indicators.length > 0 ? (
              <div className="indicator-tags-list">
                {indicators.map((ind, idx) => (
                  <div key={idx} className="editorial-indicator-tag" title={ind.description}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                      <CornerDownRight size={11} color="var(--brand-burgundy)" />
                      <strong>{ind.name}</strong>
                    </div>
                    <span>"{ind.matched_phrase}"</span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="no-indicators-text">
                No overt lexical coercion, urgent panic, or deceptive framing markers isolated. Pattern classification established primarily via continuous n-gram feature distribution.
              </p>
            )}
          </div>

          {/* Probability Distribution */}
          {sortedProbabilities.length > 0 && (
            <div>
              <div className="section-label-bar">
                <BarChart3 size={13} />
                <span>Posterior Probability Distribution Across Taxonomy</span>
              </div>

              <div className="probability-bars-table">
                {sortedProbabilities.map(([catName, prob]) => {
                  const pct = Math.round(prob * 100);
                  const isTop = catName === category;
                  return (
                    <div key={catName} className="prob-row-light">
                      <span className={`prob-name-light ${isTop ? 'highlight' : ''}`}>
                        {catName}
                      </span>
                      <div className="prob-track-light">
                        <div 
                          className={`prob-fill-light ${isTop ? 'top' : ''}`}
                          style={{ width: `${Math.max(2, pct)}%` }}
                        />
                      </div>
                      <span className="prob-pct-light">
                        {pct}%
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Ethical / Methodological Limitation Strip */}
        <div className="report-caveat-strip">
          <ShieldAlert size={18} style={{ color: 'var(--brand-burgundy)', flexShrink: 0, marginTop: '2px' }} />
          <div>
            <strong>Research Prototype Notice:</strong> This analysis identifies statistical communication patterns using natural language processing. It does not determine whether a person is lying or whether an author's subjective intentions are deceptive. Predictions are probabilistic and intended exclusively for academic research, communication auditing, and media literacy analysis.
          </div>
        </div>
      </div>
    </div>
  );
}

export { ResultCard as ResultDossier };
