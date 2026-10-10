import React from 'react';
import CategoryBadge from './CategoryBadge';
import RiskIndicator from './RiskIndicator';
import { 
  Tag, 
  BarChart3, 
  ShieldAlert, 
  Compass, 
  Gauge, 
  CheckCircle2, 
  FileText, 
  CornerDownRight,
  Sparkles,
  MessageSquare,
  ShieldCheck
} from 'lucide-react';

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
    probabilities = {},
    style_analysis = null
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
          {/* Deep Linguistic & Style Reasoning (ChatGPT / Gemini / Local Engine) */}
          {style_analysis && (
            <div className="style-reasoning-dossier" style={{ marginBottom: '1.75rem' }}>
              <div className="section-label-bar" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.45rem' }}>
                  <Sparkles size={14} color="var(--brand-burgundy)" />
                  <span style={{ fontWeight: 700, letterSpacing: '0.08em' }}>
                    DEEP LINGUISTIC & STYLE REASONING (WAY OF SPEAKING & WRITING)
                  </span>
                </div>
                <span style={{ 
                  fontFamily: 'var(--font-mono)', 
                  fontSize: '0.68rem', 
                  color: 'var(--brand-burgundy)',
                  background: 'var(--brand-burgundy-subtle)',
                  padding: '0.15rem 0.5rem',
                  borderRadius: '3px',
                  fontWeight: 600
                }}>
                  {style_analysis.model_provider || 'Neural Reasoning'}
                </span>
              </div>

              {/* 4-Pill Profile Bar */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
                gap: '0.75rem',
                margin: '0.85rem 0 1.25rem 0'
              }}>
                <div style={{ background: 'var(--bg-warm-tint)', padding: '0.65rem 0.85rem', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.2rem' }}>Tone of Voice</div>
                  <div style={{ fontWeight: 700, fontSize: '0.86rem', color: 'var(--brand-burgundy)' }}>{style_analysis.tone}</div>
                </div>

                <div style={{ background: 'var(--bg-warm-tint)', padding: '0.65rem 0.85rem', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.2rem' }}>Emotional Temp</div>
                  <div style={{ fontWeight: 600, fontSize: '0.84rem', color: 'var(--text-primary)' }}>{style_analysis.emotional_temperature}</div>
                </div>

                <div style={{ background: 'var(--bg-warm-tint)', padding: '0.65rem 0.85rem', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.2rem' }}>Directness Level</div>
                  <div style={{ fontWeight: 600, fontSize: '0.84rem', color: 'var(--text-primary)' }}>{style_analysis.directness}</div>
                </div>

                <div style={{ background: 'var(--bg-warm-tint)', padding: '0.65rem 0.85rem', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.2rem' }}>Formality Register</div>
                  <div style={{ fontWeight: 600, fontSize: '0.84rem', color: 'var(--text-primary)' }}>{style_analysis.formality}</div>
                </div>
              </div>

              {/* Surface Meaning vs Hidden Subtext Comparative Split */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
                gap: '1rem',
                marginBottom: '1.25rem'
              }}>
                <div style={{
                  background: '#fcfbf9',
                  border: '1px solid var(--border-medium)',
                  borderLeft: '4px solid var(--text-muted)',
                  padding: '0.9rem 1.1rem',
                  borderRadius: '4px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.35rem', fontFamily: 'var(--font-mono)', fontSize: '0.72rem', fontWeight: 700, color: 'var(--text-secondary)' }}>
                    <FileText size={13} />
                    <span>SURFACE MEANING (LITERAL ASSERTION)</span>
                  </div>
                  <p style={{ margin: 0, fontSize: '0.88rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                    {style_analysis.surface_meaning}
                  </p>
                </div>

                <div style={{
                  background: 'var(--brand-burgundy-subtle)',
                  border: '1px solid var(--brand-burgundy-border)',
                  borderLeft: '4px solid var(--brand-burgundy)',
                  padding: '0.9rem 1.1rem',
                  borderRadius: '4px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.35rem', fontFamily: 'var(--font-mono)', fontSize: '0.72rem', fontWeight: 700, color: 'var(--brand-burgundy)' }}>
                    <MessageSquare size={13} />
                    <span>HIDDEN SUBTEXT & PSYCHOLOGICAL LEVERAGE</span>
                  </div>
                  <p style={{ margin: 0, fontSize: '0.88rem', color: 'var(--text-primary)', lineHeight: 1.5, fontWeight: 500 }}>
                    {style_analysis.hidden_subtext}
                  </p>
                </div>
              </div>

              {/* Rhetorical Devices & Interpersonal Dynamic */}
              <div style={{ background: '#faf9f5', border: '1px solid var(--border-light)', borderRadius: '4px', padding: '0.9rem 1.1rem', marginBottom: '1.25rem' }}>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.4rem', fontWeight: 700 }}>
                  Interpersonal Power Dynamic
                </div>
                <div style={{ fontSize: '0.86rem', color: 'var(--text-primary)', marginBottom: '0.75rem', lineHeight: 1.45 }}>
                  {style_analysis.power_dynamic}
                </div>

                {style_analysis.rhetorical_devices?.length > 0 && (
                  <div>
                    <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.68rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.35rem' }}>
                      Rhetorical & Psychological Devices Detected:
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem' }}>
                      {style_analysis.rhetorical_devices.map((device, i) => (
                        <span key={i} style={{
                          fontFamily: 'var(--font-mono)',
                          fontSize: '0.72rem',
                          background: '#ffffff',
                          border: '1px solid var(--border-medium)',
                          padding: '0.2rem 0.55rem',
                          borderRadius: '3px',
                          color: 'var(--brand-burgundy)',
                          fontWeight: 600
                        }}>
                          {device}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Actionable Disarming Counter-Strategy */}
              {style_analysis.recommended_response && (
                <div style={{
                  background: 'var(--cat-normal-bg)',
                  border: '1px solid var(--cat-normal-border)',
                  borderLeft: '4px solid var(--cat-normal-text)',
                  padding: '0.9rem 1.1rem',
                  borderRadius: '4px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.35rem', fontFamily: 'var(--font-mono)', fontSize: '0.72rem', fontWeight: 700, color: 'var(--cat-normal-text)' }}>
                    <ShieldCheck size={14} />
                    <span>RECOMMENDED STRATEGY TO DISARM OR RESPOND</span>
                  </div>
                  <p style={{ margin: 0, fontSize: '0.88rem', color: 'var(--cat-normal-text)', lineHeight: 1.5, fontWeight: 500 }}>
                    {style_analysis.recommended_response}
                  </p>
                </div>
              )}
            </div>
          )}

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
