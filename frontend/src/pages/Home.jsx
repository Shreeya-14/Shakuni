import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { CATEGORIES_DATA } from '../data/categories';
import { 
  ArrowRight, 
  Search, 
  Layers, 
  Compass, 
  Binary, 
  Cpu, 
  Sliders, 
  Gauge, 
  ShieldCheck, 
  ChevronRight,
  Sparkles
} from 'lucide-react';

export default function Home() {
  const [selectedPatternIndex, setSelectedPatternIndex] = useState(0);
  const navigate = useNavigate();

  const activePattern = CATEGORIES_DATA[selectedPatternIndex] || CATEGORIES_DATA[0];

  return (
    <div className="home-page-container">
      {/* 1. EDITORIAL ASYMMETRIC HERO SECTION */}
      <section className="hero-editorial-light" aria-label="Introduction">
        <div className="hero-left-col">
          <div className="eyebrow-tag">
            <span style={{ fontSize: '0.85rem' }}>&#9670;</span>
            <span>STRATEGIC COMMUNICATION INTELLIGENCE</span>
          </div>

          <h1 className="hero-headline-light">
            Read between <br />
            the <em>lines</em>.
          </h1>

          <p className="hero-description-light">
            Shakuni examines natural language for observable patterns of social coercion, framing traps, selective omission, and persuasive influence through game-theoretic asymmetry and machine learning.
          </p>

          <div className="hero-cta-cluster">
            <Link to="/analyze" className="btn-primary-burgundy hero-btn-main">
              <span>Start Analysis</span>
              <ArrowRight size={15} />
            </Link>

            <Link to="/patterns" className="btn-secondary-light hero-btn-sub">
              <span>Explore The Framework</span>
              <ChevronRight size={14} />
            </Link>
          </div>

          <div className="hero-ethical-note">
            <ShieldCheck size={14} color="var(--brand-burgundy)" />
            <span>Probabilistic language auditing &bull; Not a lie detector</span>
          </div>
        </div>

        {/* Hero Right: Strategic Telemetry Flow Panel */}
        <div className="hero-right-col">
          <div className="strategic-viz-panel">
            <div className="viz-panel-header">
              <span>ANALYTICAL TELEMETRY</span>
              <span className="live-pulse-badge">MODEL PIPELINE ACTIVE</span>
            </div>

            <div className="telemetry-flow-box">
              <div className="telemetry-node">
                <div className="node-marker">01</div>
                <div className="node-info">
                  <strong>Unstructured Input Text</strong>
                  <span>Email, speech, pitch, advertisement, dialogue</span>
                </div>
              </div>

              <div className="telemetry-connector" />

              <div className="telemetry-node">
                <div className="node-marker">02</div>
                <div className="node-info">
                  <strong>Sublinear TF-IDF Vectorizer</strong>
                  <span>4,595 lexical unigram & bigram vocabulary features</span>
                </div>
              </div>

              <div className="telemetry-connector" />

              <div className="telemetry-node">
                <div className="node-marker">03</div>
                <div className="node-info">
                  <strong>Multinomial Softmax Classifier</strong>
                  <span>7-class posterior probability distribution</span>
                </div>
              </div>

              <div className="telemetry-connector" />

              <div className="telemetry-node highlighted">
                <div className="node-marker pulse">04</div>
                <div className="node-info">
                  <strong>Composite Threat & Risk Profile</strong>
                  <span>Explainable score (0–100) + isolated indicator markers</span>
                </div>
              </div>
            </div>

            <div className="viz-panel-footer">
              <div className="mini-dice-pip">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none">
                  <polygon points="12,2 21,7 12,12 3,7" stroke="#b89047" strokeWidth="1.2" fill="#fdfaf4" />
                  <polygon points="3,7 12,12 12,22 3,17" stroke="#7a1c30" strokeWidth="1.2" fill="#faedf0" />
                  <polygon points="21,7 12,12 12,22 21,17" stroke="#b89047" strokeWidth="1.2" fill="#fcf9f2" />
                  <circle cx="12" cy="7" r="1.2" fill="#7a1c30" />
                  <circle cx="7.5" cy="14.5" r="1" fill="#b89047" />
                  <circle cx="16.5" cy="14.5" r="1" fill="#7a1c30" />
                </svg>
              </div>
              <span>Game-Theoretic Framework: Evaluating language as strategic signaling.</span>
            </div>
          </div>
        </div>
      </section>

      {/* 2. PRODUCT SNAPSHOT / EDITORIAL STATISTICS */}
      <section className="snapshot-strip" aria-label="Platform Specifications">
        <div className="snapshot-grid">
          <div className="snapshot-item">
            <span className="snapshot-number">07</span>
            <span className="snapshot-label">COMMUNICATION PATTERNS</span>
            <p className="snapshot-sub">Taxonomic classes covering coercive, framing & withholding maneuvers.</p>
          </div>

          <div className="snapshot-item">
            <span className="snapshot-number">4,595</span>
            <span className="snapshot-label">LEXICAL N-GRAM FEATURES</span>
            <p className="snapshot-sub">Sublinear TF-IDF term weights capturing unigrams and strategic bigrams.</p>
          </div>

          <div className="snapshot-item">
            <span className="snapshot-number">91.4%</span>
            <span className="snapshot-label">BENCHMARK ACCURACY</span>
            <p className="snapshot-sub">Multinomial logistic regression calibrated across 280 curated samples.</p>
          </div>

          <div className="snapshot-item">
            <span className="snapshot-number">0–100</span>
            <span className="snapshot-label">EXPLAINABLE RISK SCORE</span>
            <p className="snapshot-sub">Multi-factor composite index grounded in category severity and confidence.</p>
          </div>
        </div>
      </section>

      {/* 3. INTERACTIVE SECTION: THE SEVEN PATTERNS */}
      <section className="homepage-section" aria-label="Taxonomic Framework">
        <div className="section-head-cluster">
          <span className="section-eyebrow">TAXONOMIC REPOSITORY</span>
          <h2 className="section-main-heading">Seven ways language can influence a decision.</h2>
          <p className="section-lead-paragraph">
            Strategic influence rarely relies on overt falsehoods. Rather, it operates by reshaping the receiver's perception of risk, consensus, and necessity. Click any category to preview its linguistic characteristics:
          </p>
        </div>

        <div className="patterns-interactive-stage">
          {/* Left: Numbered Index Selector */}
          <div className="pattern-index-column" role="tablist" aria-label="Category Selector">
            {CATEGORIES_DATA.map((cat, idx) => {
              const isSelected = idx === selectedPatternIndex;
              return (
                <button
                  key={cat.id}
                  type="button"
                  role="tab"
                  aria-selected={isSelected}
                  className={`pattern-index-row ${isSelected ? 'active' : ''}`}
                  onClick={() => setSelectedPatternIndex(idx)}
                >
                  <span className="pattern-row-num">{cat.num}</span>
                  <div className="pattern-row-text">
                    <strong className="pattern-row-name">{cat.name}</strong>
                    <span className="pattern-row-tier">{cat.riskTier} Risk</span>
                  </div>
                  <ChevronRight size={14} className="pattern-row-arrow" />
                </button>
              );
            })}
          </div>

          {/* Right: Dynamic Pattern Preview Card */}
          <div className="pattern-preview-card" role="tabpanel">
            <div className="preview-top-strip">
              <span className="preview-category-code">{activePattern.code} // CLASSIFICATION PROFILE</span>
              <span className={`preview-risk-badge ${activePattern.riskTier.toLowerCase()}`}>
                {activePattern.riskTier} Risk ({activePattern.riskScoreRange})
              </span>
            </div>

            <h3 className="preview-category-name">{activePattern.name}</h3>
            <p className="preview-tagline">{activePattern.tagline}</p>

            <div className="preview-block">
              <span className="preview-block-label">Formal Definition</span>
              <p className="preview-block-text">{activePattern.description}</p>
            </div>

            <div className="preview-block">
              <span className="preview-block-label">Representative Linguistic Sample</span>
              <blockquote className="preview-quote-box">
                "{activePattern.example}"
              </blockquote>
            </div>

            <div className="preview-block">
              <span className="preview-block-label">Typical Rhetorical Indicators</span>
              <div className="preview-indicators-wrap">
                {activePattern.typicalIndicators.map((ind, i) => (
                  <span key={i} className="preview-indicator-pill">{ind}</span>
                ))}
              </div>
            </div>

            <div className="preview-card-actions">
              <button 
                type="button" 
                className="btn-primary-burgundy"
                onClick={() => navigate(`/analyze?sample=${encodeURIComponent(activePattern.example)}`)}
              >
                <Search size={14} />
                <span>Test this example in Workspace</span>
              </button>

              <Link to="/patterns" className="btn-secondary-light">
                <span>View Full Category Monograph</span>
                <ArrowRight size={13} />
              </Link>
            </div>
          </div>
        </div>

        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <Link to="/patterns" className="text-link-editorial">
            <span>Explore all seven categories in depth &rarr;</span>
          </Link>
        </div>
      </section>

      {/* 4. VISUAL PROCESS PIPELINE (HOW IT WORKS) */}
      <section className="homepage-section" aria-label="System Process Flow">
        <div className="section-head-cluster">
          <span className="section-eyebrow">COMPUTATIONAL ARCHITECTURE</span>
          <h2 className="section-main-heading">How Shakuni analyzes communication.</h2>
          <p className="section-lead-paragraph">
            Input utterances pass sequentially through five decoupled analysis stages, transforming unstructured text into audited probability distributions and grounded threat indices.
          </p>
        </div>

        <div className="pipeline-steps-container">
          <div className="pipeline-step-card">
            <div className="step-card-num">STAGE 01</div>
            <div className="step-card-icon-box">
              <Compass size={18} color="var(--brand-burgundy)" />
            </div>
            <h3 className="step-card-title">Token Normalization</h3>
            <p className="step-card-desc">
              Cleanses formatting noise, standardizes unicode casing, and parses conversational boundaries.
            </p>
          </div>

          <div className="pipeline-step-card">
            <div className="step-card-num">STAGE 02</div>
            <div className="step-card-icon-box">
              <Binary size={18} color="var(--brand-burgundy)" />
            </div>
            <h3 className="step-card-title">TF-IDF Vector Space</h3>
            <p className="step-card-desc">
              Extracts 4,595 unigrams and bigrams using sublinear term-frequency inverse document frequency weighting.
            </p>
          </div>

          <div className="pipeline-step-card">
            <div className="step-card-num">STAGE 03</div>
            <div className="step-card-icon-box">
              <Cpu size={18} color="var(--brand-burgundy)" />
            </div>
            <h3 className="step-card-title">Logistic Softmax</h3>
            <p className="step-card-desc">
              Computes balanced posterior probability distributions across all seven manipulation categories.
            </p>
          </div>

          <div className="pipeline-step-card">
            <div className="step-card-num">STAGE 04</div>
            <div className="step-card-icon-box">
              <Sliders size={18} color="var(--brand-burgundy)" />
            </div>
            <h3 className="step-card-title">Linguistic Markers</h3>
            <p className="step-card-desc">
              Deterministic syntactic scanner isolates exact evidence clauses such as false dilemmas and guilt appeals.
            </p>
          </div>

          <div className="pipeline-step-card">
            <div className="step-card-num">STAGE 05</div>
            <div className="step-card-icon-box">
              <Gauge size={18} color="var(--brand-burgundy)" />
            </div>
            <h3 className="step-card-title">Risk Formulation</h3>
            <p className="step-card-desc">
              Generates an explainable composite score (0–100) weighing baseline severity, manipulation mass, and confidence.
            </p>
          </div>
        </div>

        <div style={{ textAlign: 'center', marginTop: '2rem' }}>
          <Link to="/model" className="text-link-editorial">
            <span>Inspect the machine learning model architecture & evaluation &rarr;</span>
          </Link>
        </div>
      </section>

      {/* 5. RESEARCH STATEMENT SECTION */}
      <section className="homepage-section" aria-label="Theoretical Foundation">
        <div className="research-statement-box">
          <div className="statement-motif-pip">
            <Sparkles size={18} color="var(--brand-gold)" />
          </div>
          <span className="statement-eyebrow">RESEARCH FOUNDATION & ETHICAL SCOPE</span>
          <h2 className="statement-headline">
            Can a machine analyze influence without pretending to read intent?
          </h2>
          <div className="statement-body-columns">
            <p>
              Contemporary natural language processing often overreaches by purporting to measure objective deception or verify moral intent. In reality, surface text alone cannot reveal what an author secretly believes or whether a statement is an honest mistake, irony, or malice.
            </p>
            <p>
              Shakuni addresses this dilemma through disciplined restraint: rather than claiming to be a "lie detector", the framework focuses strictly on <strong>observable rhetorical structure</strong>. It flags manufactured consensus, selective omissions, and coercive pressure so human readers can evaluate strategic asymmetry for themselves.
            </p>
          </div>
          <div className="statement-footer">
            <Link to="/research" className="btn-secondary-light">
              <span>Read the Academic Research Monograph</span>
              <ArrowRight size={13} />
            </Link>
          </div>
        </div>
      </section>

      {/* 6. FINAL BOTTOM CTA BANNER */}
      <section className="homepage-cta-banner" aria-label="Get Started">
        <div className="cta-banner-inner">
          <h2 className="cta-banner-headline">
            Explore the language behind the strategy.
          </h2>
          <p className="cta-banner-sub">
            Paste any statement, marketing pitch, or executive communication to audit its rhetorical framing.
          </p>
          <div className="cta-banner-buttons">
            <Link to="/analyze" className="btn-primary-burgundy btn-large">
              <Search size={15} />
              <span>Launch Analyzer Workspace</span>
            </Link>
            <Link to="/patterns" className="btn-secondary-light btn-large">
              <span>Explore The 07 Patterns</span>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
