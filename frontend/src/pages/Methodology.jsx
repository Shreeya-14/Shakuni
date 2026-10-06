import React from 'react';
import { Database, Binary, Cpu, Gauge, AlertTriangle, ShieldCheck, CheckCircle2, Sliders } from 'lucide-react';

export default function Methodology() {
  return (
    <article className="editorial-monograph">
      {/* Monograph Header */}
      <header className="monograph-header">
        <span className="monograph-ref">RESEARCH SPECIFICATION // MONOGRAPH 01</span>
        <h2 className="monograph-title">Analytical Methodology & Statistical Pipeline</h2>
        <p className="monograph-abstract">
          An architectural exposition of the natural language processing pipeline, n-gram feature representations, multinomial logistic calibration, and explainable risk formulation governing the Shakuni intelligence framework.
        </p>
      </header>

      {/* Section 01: Corpus Curation */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 01</span>
        <h3 className="monograph-sec-title">
          <Database size={20} color="var(--brand-burgundy)" />
          Corpus Curation & Dataset Design
        </h3>
        <p>
          To systematically analyze tactical persuasion without violating privacy rights or relying on unverified scrape feeds, Shakuni is trained upon a benchmark corpus of <strong>280 synthetic and curated research examples</strong> evenly stratified across seven manipulation patterns (40 samples per category).
        </p>
        <p>
          Each sample was authored and peer-evaluated to capture real-world discourse patterns found across executive correspondence, marketing copy, political discourse, and interpersonal communication.
        </p>

        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>Privacy-Preserving Design</h4>
            <p>No unauthorized user communications were harvested. All samples are explicitly designated as curated research examples for reproducible benchmarking.</p>
          </div>
          <div className="monograph-brief-box">
            <h4>Uniform Stratification</h4>
            <p>Equal 40-sample distribution guarantees unbiased category priors, preventing majority-class distortion across subtle communicative nuances.</p>
          </div>
        </div>
      </section>

      {/* Section 02: Text Representation */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 02</span>
        <h3 className="monograph-sec-title">
          <Binary size={20} color="var(--brand-burgundy)" />
          Text Representation & N-Gram Feature Extraction
        </h3>
        <p>
          Natural language text undergoes standard normalization (lowercasing, unicode regularizations, whitespace stripping) prior to vectorization via sublinear term-frequency inverse-document-frequency:
        </p>

        <div className="monograph-formula-box">
          {"TF-IDF(t, d, D) = [1 + ln(count(t, d))] × [ln((1 + |D|) / (1 + DF(t, D))) + 1]"}
        </div>

        <p>
          By extracting both <strong>unigrams and bigrams</strong> (n-gram range 1–2), the model preserves key rhetorical pairings such as <em>"right now"</em>, <em>"lone dissenter"</em>, <em>"completely free"</em>, and <em>"either you"</em> that carry high strategic significance across 4,595 vocabulary features.
        </p>
      </section>

      {/* Section 03: Classification */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 03</span>
        <h3 className="monograph-sec-title">
          <Cpu size={20} color="var(--brand-burgundy)" />
          Interpretable Probabilistic Classification
        </h3>
        <p>
          To maintain rigorous auditability required in institutional research, Shakuni employs a regularized <strong>Multinomial Logistic Regression</strong> classifier with balanced class weights rather than an unexplainable black-box architecture.
        </p>
        <p>
          Posterior class probabilities are derived via the softmax distribution:
        </p>

        <div className="monograph-formula-box">
          {"P(y = c | x) = exp(w_c^T x + b_c) / Σ_j exp(w_j^T x + b_j)"}
        </div>

        <p>
          This ensures that predictions provide a calibrated probability spectrum across all seven categories rather than an uncalibrated point decision.
        </p>
      </section>

      {/* Section 04: Indicators */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 04</span>
        <h3 className="monograph-sec-title">
          <Sliders size={20} color="var(--brand-burgundy)" />
          Linguistic Indicators & Rule Extraction
        </h3>
        <p>
          Statistical vector classification is supplemented by a deterministic rhetorical pattern scanner. This scanner isolates specific linguistic structures—such as consensus claims (<em>"everyone else has agreed"</em>), acute guilt appeals (<em>"if you really loved"</em>), and false dichotomies (<em>"either ... or"</em>).
        </p>
        <p>
          These indicators act as grounded evidentiary anchors displayed directly within the intelligence report brief.
        </p>
      </section>

      {/* Section 05: Risk Formulation */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 05</span>
        <h3 className="monograph-sec-title">
          <Gauge size={20} color="var(--brand-burgundy)" />
          Composite Threat & Risk Formulation
        </h3>
        <p>
          The Shakuni Risk Score (0–100) is an explainable index quantifying the estimated intensity of manipulative persuasion:
        </p>

        <div className="monograph-formula-box">
          {"Risk Score = Clamp[ (W_cat × 0.45) + (P_manip × 30.0) + (Confidence × 12.0) + I_mod, 0, 100 ]"}
        </div>

        <ul style={{ paddingLeft: '1.5rem', color: 'var(--text-secondary)', lineHeight: '1.9', fontSize: '0.95rem', marginBottom: '1.5rem' }}>
          <li><strong>W_cat (Base Severity)</strong>: Qualitative baseline assigned to the category (Normal: 10, Selective Info: 52, Framing: 60, Social Pressure: 65, Emotional Pressure: 72, Withholding: 75, Deceptive Persuasion: 88).</li>
          <li><strong>P_manip (Manipulation Mass)</strong>: Cumulative probability mass assigned to non-normal categories (1.0 - P(Normal)).</li>
          <li><strong>Confidence</strong>: Posterior probability of the predicted category.</li>
          <li><strong>I_mod (Indicator Bonus)</strong>: Density modifier (+4 for category-congruent rhetorical markers, capped at 20).</li>
        </ul>

        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
          <span className="risk-tier-badge low">0 – 39: Low Risk</span>
          <span className="risk-tier-badge moderate">40 – 69: Moderate Risk</span>
          <span className="risk-tier-badge high">70 – 100: High Risk</span>
        </div>
      </section>

      {/* Section 06: Validation */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 06</span>
        <h3 className="monograph-sec-title">
          <CheckCircle2 size={20} color="var(--brand-burgundy)" />
          Model Validation & Reproducibility
        </h3>
        <p>
          Pipeline training and inference pipelines are tested continuously via an automated test suite (27 unit and integration tests across data integrity, model calibration, and API contracts).
        </p>
        <p>
          Weights and vectorizer vocabularies are serialized via standard joblib binaries, ensuring deterministic offline reproducibility without reliance on remote model endpoints.
        </p>
      </section>

      {/* Section 07: Boundaries */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 07</span>
        <h3 className="monograph-sec-title">
          <AlertTriangle size={20} color="var(--brand-burgundy)" />
          Methodological Boundaries & Limitations
        </h3>
        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>Surface Text vs Intent</h4>
            <p>Surface text cannot definitively establish internal human intent. The framework classifies rhetorical structure, not moral character or objective truth.</p>
          </div>
          <div className="monograph-brief-box">
            <h4>Irony & Interpersonal Banter</h4>
            <p>Satirical statements or affectionate interpersonal banter may superficially match pressure markers without manipulative intent.</p>
          </div>
        </div>
      </section>
    </article>
  );
}
