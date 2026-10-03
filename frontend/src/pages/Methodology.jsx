import React from 'react';
import { Database, Binary, Cpu, Gauge, AlertTriangle, ArrowRight, ShieldCheck } from 'lucide-react';

export default function Methodology() {
  return (
    <div className="editorial-page">
      {/* Editorial Header */}
      <header className="editorial-header">
        <span className="editorial-doc-code">RESEARCH SPECIFICATION // MONOGRAPH 01</span>
        <h2 className="editorial-title">Analytical Methodology & Statistical Pipeline</h2>
        <p className="editorial-subtitle">
          An architectural exposition of the natural language processing pipeline, n-gram feature representations, multinomial logistic calibration, and explainable risk formulation governing the Shakuni intelligence framework.
        </p>
      </header>

      {/* Visual Process Flow */}
      <section className="editorial-section">
        <span className="editorial-section-num">SYSTEM PROCESS FLOW</span>
        <h3 className="editorial-section-heading">Analytical Pipeline Architecture</h3>
        <p>
          Input utterances pass sequentially through five decoupled analysis stages, converting unstructured linguistic statements into audited posterior probability distributions and composite threat indices.
        </p>

        <div className="flow-diagram-container">
          <div className="flow-step-box">
            <div className="flow-step-num">STAGE 01</div>
            <div className="flow-step-title">Corpus Data</div>
            <div className="flow-step-sub">280 Balanced Curated Samples</div>
          </div>
          <div className="flow-step-box">
            <div className="flow-step-num">STAGE 02</div>
            <div className="flow-step-title">TF-IDF Vector</div>
            <div className="flow-step-sub">1–2 N-grams (4,595 features)</div>
          </div>
          <div className="flow-step-box">
            <div className="flow-step-num">STAGE 03</div>
            <div className="flow-step-title">Classification</div>
            <div className="flow-step-sub">Multinomial Logistic Softmax</div>
          </div>
          <div className="flow-step-box">
            <div className="flow-step-num">STAGE 04</div>
            <div className="flow-step-title">Indicators</div>
            <div className="flow-step-sub">Lexicon & Syntax Rule Matcher</div>
          </div>
          <div className="flow-step-box">
            <div className="flow-step-num">STAGE 05</div>
            <div className="flow-step-title">Risk Scoring</div>
            <div className="flow-step-sub">Composite Index (0–100)</div>
          </div>
        </div>
      </section>

      {/* Section 01: Corpus Curation */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 01</span>
        <h3 className="editorial-section-heading">
          <Database size={20} color="var(--accent-gold)" />
          Corpus Curation & Dataset Design
        </h3>
        <p>
          To systematically analyze tactical persuasion without violating privacy rights or relying on unverified scrape feeds, Shakuni is trained upon a benchmark corpus of <strong>280 synthetic/curated research examples</strong> evenly stratified across seven manipulation patterns (40 samples per category).
        </p>
        <p>
          Each sample was authored and peer-evaluated to capture real-world discourse patterns found across executive correspondence, marketing copy, political discourse, and interpersonal communication.
        </p>

        <div className="brief-grid">
          <div className="brief-box">
            <h4>Privacy-Preserving Design</h4>
            <p>No unauthorized user communications were harvested. All samples are explicitly designated as curated research examples for reproducible benchmarking.</p>
          </div>
          <div className="brief-box">
            <h4>Uniform Stratification</h4>
            <p>Equal 40-sample distribution guarantees unbiased category priors, preventing majority-class distortion across subtle communicative nuances.</p>
          </div>
        </div>
      </section>

      {/* Section 02: Text Representation */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 02</span>
        <h3 className="editorial-section-heading">
          <Binary size={20} color="var(--accent-gold)" />
          Text Representation & N-Gram Feature Extraction
        </h3>
        <p>
          Natural language text undergoes standard normalization (lowercasing, unicode regularizations, whitespace stripping) prior to vectorization via sublinear term-frequency inverse-document-frequency:
        </p>

        <div className="formula-callout">
          {"TF-IDF(t, d, D) = [1 + ln(count(t, d))] × [ln((1 + |D|) / (1 + DF(t, D))) + 1]"}
        </div>

        <p>
          By extracting both <strong>unigrams and bigrams</strong> (n-gram range 1–2), the model preserves key rhetorical pairings such as <em>"right now"</em>, <em>"lone dissenter"</em>, <em>"completely free"</em>, and <em>"either you"</em> that carry high strategic significance.
        </p>
      </section>

      {/* Section 03: Classification */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 03</span>
        <h3 className="editorial-section-heading">
          <Cpu size={20} color="var(--accent-gold)" />
          Interpretable Probabilistic Classification
        </h3>
        <p>
          To maintain rigorous auditability required in institutional research, Shakuni employs a regularized <strong>Multinomial Logistic Regression</strong> classifier with balanced class weights rather than an unexplainable black-box architecture.
        </p>
        <p>
          Posterior class probabilities are derived via the softmax distribution:
        </p>

        <div className="formula-callout">
          {"P(y = c | x) = exp(w_c^T x + b_c) / Σ_j exp(w_j^T x + b_j)"}
        </div>

        <p>
          This ensures that predictions provide a calibrated probability spectrum across all seven categories rather than an uncalibrated point decision.
        </p>
      </section>

      {/* Section 04: Indicators */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 04</span>
        <h3 className="editorial-section-heading">
          <Gauge size={20} color="var(--accent-gold)" />
          Linguistic Indicators & Rule Extraction
        </h3>
        <p>
          Statistical vector classification is supplemented by a deterministic rhetorical pattern scanner. This scanner isolates specific linguistic structures—such as consensus claims (*"everyone else has agreed"*), acute guilt appeals (*"if you really loved"*), and false dichotomies (*"either ... or"*).
        </p>
        <p>
          These indicators act as grounded evidentiary anchors displayed directly within the intelligence report brief.
        </p>
      </section>

      {/* Section 05: Risk Analysis */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 05</span>
        <h3 className="editorial-section-heading">
          <Gauge size={20} color="var(--accent-gold)" />
          Composite Threat & Risk Formulation
        </h3>
        <p>
          The Shakuni Risk Score (0–100) is an explainable index quantifying the estimated intensity of manipulative persuasion:
        </p>

        <div className="formula-callout">
          {"Risk Score = Clamp[ (W_cat × 0.45) + (P_manip × 30.0) + (Confidence × 12.0) + I_mod, 0, 100 ]"}
        </div>

        <ul style={{ paddingLeft: '1.5rem', color: 'var(--text-secondary)', lineHeight: '1.9', fontSize: '0.95rem' }}>
          <li><strong>W_cat (Base Severity)</strong>: Qualitative baseline assigned to the category (Normal: 10, Selective Info: 52, Framing: 60, Social Pressure: 65, Emotional Pressure: 72, Withholding: 75, Deceptive Persuasion: 88).</li>
          <li><strong>P_manip (Manipulation Mass)</strong>: Cumulative probability mass assigned to non-normal categories (1.0 - P(Normal)).</li>
          <li><strong>Confidence</strong>: Posterior probability of the predicted category.</li>
          <li><strong>I_mod (Indicator Bonus)</strong>: Density modifier (+4 for category-congruent rhetorical markers, capped at 20).</li>
        </ul>

        <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <span className="risk-tier-tag low">0 – 39: Low Risk</span>
          <span className="risk-tier-tag moderate">40 – 69: Moderate Risk</span>
          <span className="risk-tier-tag high">70 – 100: High Risk</span>
        </div>
      </section>

      {/* Known Limitations */}
      <section className="editorial-section">
        <span className="editorial-section-num">SECTION 06</span>
        <h3 className="editorial-section-heading">
          <AlertTriangle size={20} color="var(--accent-wine)" />
          Methodological Boundaries & Limitations
        </h3>
        <div className="brief-grid">
          <div className="brief-box">
            <h4>Context & Intent Boundary</h4>
            <p>Surface text cannot definitively establish internal human intent. The framework classifies rhetorical structure, not moral character or objective truth.</p>
          </div>
          <div className="brief-box">
            <h4>Irony & Inside Banter</h4>
            <p>Satirical statements or affectionate interpersonal banter may superficially match pressure markers without manipulative intent.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
