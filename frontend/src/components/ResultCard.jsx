import React from 'react';
import CategoryBadge from './CategoryBadge';
import RiskIndicator from './RiskIndicator';
import { Tag, BarChart3, ShieldAlert, Compass, CheckCircle2 } from 'lucide-react';

export default function ResultCard({ result }) {
  if (!result) return null;

  const {
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
    <div className="report-dossier">
      <div className="dossier-card">
        {/* Top Report Metadata Strip */}
        <div className="report-meta-strip">
          <div>DOSSIER REPORT // CLASSIFICATION BRIEF</div>
          <div>STATUS: ANALYSIS COMPLETE &bull; MODEL: TF-IDF + LOGISTIC REGRESSION</div>
        </div>

        {/* Lead Grid: Category + Confidence + Precision Radial Risk Gauge */}
        <div className="report-lead-grid">
          <div>
            <div className="pattern-eyebrow">DETECTED RHETORICAL PATTERN</div>
            <div className="pattern-title">{category}</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem', flexWrap: 'wrap' }}>
              <CategoryBadge category={category} />
              
              <div style={{ display: 'flex', alignItems: 'baseline', gap: '0.45rem' }}>
                <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.72rem', color: 'var(--text-muted)', letterSpacing: '0.1em', textTransform: 'uppercase' }}>
                  Model Confidence:
                </span>
                <span style={{ fontFamily: 'var(--font-mono)', fontSize: '1.35rem', fontWeight: '700', color: 'var(--accent-gold-light)' }}>
                  {confidencePct}%
                </span>
              </div>
            </div>
          </div>

          {/* Right Column: Radial Risk Gauge */}
          <RiskIndicator score={risk_score} level={risk_level} />
        </div>

        {/* Dossier Body Content */}
        <div className="dossier-body">
          {/* Editorial Analysis Explanation */}
          <div>
            <div className="dossier-section-title">
              <Compass size={14} color="var(--accent-gold)" />
              <span>Contextual Pattern Analysis & Qualitative Rationale</span>
            </div>
            <div className="editorial-explanation">
              {explanation}
            </div>
          </div>

          {/* Potential Linguistic Indicators */}
          <div>
            <div className="dossier-section-title">
              <Tag size={14} color="var(--accent-gold)" />
              <span>Potential Rhetorical Indicators Detected ({indicators.length})</span>
            </div>

            {indicators.length > 0 ? (
              <div className="indicator-tag-grid">
                {indicators.map((ind, idx) => (
                  <div key={idx} className="indicator-dossier-tag" title={ind.description}>
                    <strong>{ind.name}</strong>
                    <span>"{ind.matched_phrase}"</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="no-indicators-note">
                No overt lexical coercion, urgent panic, or deceptive framing markers isolated. Pattern classification established primarily via continuous n-gram distribution.
              </div>
            )}
          </div>

          {/* Category Probability Distribution */}
          {sortedProbabilities.length > 0 && (
            <div>
              <div className="dossier-section-title">
                <BarChart3 size={14} color="var(--accent-gold)" />
                <span>Posterior Probability Distribution Across Taxonomy</span>
              </div>

              <div className="probabilities-matrix">
                {sortedProbabilities.map(([catName, prob]) => {
                  const pct = Math.round(prob * 100);
                  const isTop = catName === category;
                  return (
                    <div key={catName} className="prob-metric-row">
                      <span 
                        className="prob-metric-name" 
                        style={{ 
                          color: isTop ? 'var(--text-primary)' : 'var(--text-muted)',
                          fontWeight: isTop ? '600' : '400'
                        }}
                      >
                        {catName}
                      </span>
                      <div className="prob-track">
                        <div 
                          className="prob-fill" 
                          style={{ 
                            width: `${pct}%`,
                            background: isTop 
                              ? 'linear-gradient(90deg, var(--accent-wine), var(--accent-gold))' 
                              : 'rgba(197, 160, 89, 0.2)'
                          }} 
                        />
                      </div>
                      <span className="prob-pct-number" style={{ color: isTop ? 'var(--accent-gold-light)' : 'var(--text-muted)' }}>
                        {pct}%
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Ethical / Methodological Caveat Strip */}
        <div className="dossier-caveat">
          <ShieldAlert size={18} style={{ color: 'var(--accent-gold)', flexShrink: 0, marginTop: '2px' }} />
          <div className="dossier-caveat-text">
            <strong>Research Prototype Notice:</strong> This analysis identifies statistical communication patterns using natural language processing. It does not determine whether a person is lying or whether an author's subjective intentions are deceptive. Predictions are probabilistic and intended exclusively for academic research, communication auditing, and media literacy analysis.
          </div>
        </div>
      </div>
    </div>
  );
}
