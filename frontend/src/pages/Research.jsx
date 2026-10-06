import React from 'react';
import { 
  Target, 
  BookOpen, 
  GitCompare, 
  Network, 
  Scale, 
  Award, 
  ShieldAlert, 
  Cpu, 
  AlertTriangle,
  Compass,
  Layers
} from 'lucide-react';

export default function Research() {
  return (
    <article className="editorial-monograph" role="article">
      {/* Header */}
      <header className="monograph-header">
        <span className="monograph-ref">RESEARCH SPECIFICATION // MONOGRAPH 02</span>
        <h1 className="monograph-title">Conceptual Foundations & Theoretical Context</h1>
        <p className="monograph-abstract">
          Investigating the dynamics of strategic information manipulation, cognitive vulnerability exploitation, and conversational asymmetry through computational discourse analysis.
        </p>
      </header>

      {/* 1. The Problem */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 01 // THE PROBLEM</span>
        <h2 className="monograph-sec-title">The Hidden Mechanics of Covert Influence</h2>
        <p>
          Contemporary automated discourse analysis has excelled at catching overt hostility, explicit profanity, and crude disinformation. Yet the most destructive forms of manipulation—coercive workplace pressure, fraudulent investment prospectuses, and emotionally abusive interpersonal communications—operate almost exclusively within the confines of polite, professional, and seemingly reasoned dialogue.
        </p>
        <p>
          Standard sentiment analyzers mark these coercive statements as "neutral" or "positive," while toxic-speech filters fail to fire because no offensive lexemes are present. There exists an acute need for tools that examine the <em>structure of the proposal</em> rather than the emotional tone of the speaker.
        </p>
      </section>

      {/* 2. Conceptual Foundation: Shakuni Archetype & Asymmetry */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 02 // CONCEPTUAL FOUNDATION</span>
        <h2 className="monograph-sec-title">
          <Target size={20} color="var(--brand-burgundy)" />
          The Shakuni Archetype & Game-Theoretic Asymmetry
        </h2>
        <p>
          In classical epic traditions (principally the Mahabharata), the figure of <strong>Shakuni</strong> serves as the seminal archetype of strategic deception. Rather than relying on physical martial might, Shakuni orchestrated political outcomes by exploiting cognitive biases: inciting familial pride, manufacturing false choices, and skewing probability through the loaded dice game.
        </p>
        <p>
          In contemporary computational terms, the "loaded dice" metaphor directly maps to <strong>information asymmetry</strong>: when one party selectively presents evidence, conceals critical caveats, or manufactures synthetic social pressure, the decision environment is manipulated while preserving the surface illusion of fair consent.
        </p>

        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>Asymmetric Signaling</h4>
            <p>The speaker holds privileged knowledge of consequences, dependencies, or group consensus that the recipient cannot independently verify in real time.</p>
          </div>
          <div className="monograph-brief-box">
            <h4>Decision-Space Distortion</h4>
            <p>Rather than asserting falsehoods, the speaker artificially constrains the listener's perceived choices (e.g., framing standard alternatives as existential betrayal).</p>
          </div>
        </div>
      </section>

      {/* 3. Existing Approaches & Comparative Matrix Table */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 03 // STATE OF THE ART</span>
        <h2 className="monograph-sec-title">
          <GitCompare size={20} color="var(--brand-burgundy)" />
          Comparative Analysis of Analytical Paradigms
        </h2>
        <p>
          Existing automated discourse tools fail to capture the specific subtleties of strategic manipulation due to misaligned objective functions:
        </p>

        <div className="research-table-wrapper">
          <table className="research-table">
            <thead>
              <tr>
                <th>Analytical Paradigm</th>
                <th>Target Feature</th>
                <th>Output Format</th>
                <th>Core Analytical Blind Spot</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--text-primary)' }}>Toxicity Detection (Perspective API)</td>
                <td>Abusive vocabulary, slurs, overt hostility</td>
                <td>Toxicity Score (0–1)</td>
                <td>Completely blind to polite, polished executive manipulation.</td>
              </tr>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--text-primary)' }}>Fact-Checking Systems (FEVER, ClaimBuster)</td>
                <td>Verifiable historical or statistical claims</td>
                <td>True / False Label</td>
                <td>Fails when cherry-picked statements are technically true yet misleading.</td>
              </tr>
              <tr>
                <td style={{ fontWeight: 600, color: 'var(--text-primary)' }}>Sentiment Classifiers (VADER, RoBERTa)</td>
                <td>Positive vs. negative emotional valence</td>
                <td>Sentiment Polarity</td>
                <td>Conflates coercive urgency with negative sentiment, ignoring positive-toned pressure.</td>
              </tr>
              <tr className="highlight-shakuni">
                <td style={{ fontWeight: 700, color: 'var(--brand-burgundy)' }}>Shakuni Framework</td>
                <td>Asymmetric framing, withholding, and rhetorical coercion</td>
                <td>7-Class Probability + Risk Score (0–100)</td>
                <td>Context-dependent sarcasm requiring external world knowledge.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      {/* 4. Research Gap */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 04 // RESEARCH GAP</span>
        <h2 className="monograph-sec-title">
          <BookOpen size={20} color="var(--brand-burgundy)" />
          The Void in Contemporary Discourse NLP
        </h2>
        <p>
          While natural language processing has produced thousands of studies on sentiment and profanity, there exists a profound scarcity of computational frameworks dedicated to <strong>persuasive manipulation taxonomy</strong>.
        </p>
        <p>
          Shakuni addresses this gap by defining and validating a seven-category structure focused on how information is packaged and weaponized rather than whether it contains offensive words.
        </p>
      </section>

      {/* 5. System Framework */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 05 // SYSTEM FRAMEWORK</span>
        <h2 className="monograph-sec-title">
          <Network size={20} color="var(--brand-burgundy)" />
          Decoupled, Explainable Engineering
        </h2>
        <p>
          Rather than relying on uninterpretable multi-billion parameter models that hallucinate confidence, Shakuni combines two auditable layers:
        </p>
        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>Calibrated Softmax Distribution</h4>
            <p>Multinomial Logistic Regression delivers mathematically sound class distributions with verifiable coefficient contributions across 4,595 n-grams.</p>
          </div>
          <div className="monograph-brief-box">
            <h4>Evidence-Grounded Explanations</h4>
            <p>Every analysis extracts specific linguistic markers that anchor the qualitative rationale in surface text evidence (e.g. false dichotomy anchors, guilt triggers).</p>
          </div>
        </div>
      </section>

      {/* 6. Ethical Considerations & Responsible AI */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 06 // ETHICAL GOVERNANCE</span>
        <h2 className="monograph-sec-title">
          <Scale size={20} color="var(--brand-burgundy)" />
          Ethical Guardrails & Judicial Restraint
        </h2>
        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>Not a Lie Detector</h4>
            <p>Shakuni analyzes linguistic patterns. It never claims to evaluate whether a speaker is objectively lying or determine subjective moral guilt.</p>
          </div>
          <div className="monograph-brief-box">
            <h4>Human-in-the-Loop Mandate</h4>
            <p>Model scores must never be utilized as autonomous grounds for disciplinary action, content censorship, or legal sanction without human audit.</p>
          </div>
        </div>
      </section>

      {/* 7. Limitations */}
      <section className="monograph-section">
        <span className="monograph-sec-number">SECTION 07 // LIMITATIONS</span>
        <h2 className="monograph-sec-title">
          <AlertTriangle size={20} color="var(--brand-burgundy)" />
          Methodological Scope & Limitations
        </h2>
        <ul style={{ paddingLeft: '1.5rem', color: 'var(--text-secondary)', lineHeight: '1.9', fontSize: '0.95rem' }}>
          <li><strong>Curated Benchmark Dataset</strong>: Training relies on 280 peer-reviewed curated research examples; continuous training on open datasets is required for domain transfer.</li>
          <li><strong>Context Sensitivity</strong>: Irony, inside humor, or affectionate teasing among close colleagues may trigger rhetorical markers without manipulative intent.</li>
          <li><strong>Domain Nuances</strong>: Legal documents and aggressive advertising use distinct framing conventions that require specialized threshold calibrations.</li>
        </ul>
      </section>

      {/* 8. Scholarly Citations */}
      <section className="monograph-section">
        <span className="monograph-sec-number">REFERENCES & SCHOLARLY LITERATURE</span>
        <h2 className="monograph-sec-title">
          <Award size={20} color="var(--brand-burgundy)" />
          Foundational Bibliography
        </h2>
        <ul style={{ paddingLeft: '1.25rem', color: 'var(--text-secondary)', lineHeight: '1.9', fontSize: '0.9rem' }}>
          <li><strong>Tversky, A., & Kahneman, D. (1981).</strong> The Framing of Decisions and the Psychology of Choice. <em>Science</em>, 211(4481), 453-458.</li>
          <li><strong>Cialdini, R. B. (2001).</strong> <em>Influence: Science and Practice</em> (4th ed.). Allyn & Bacon.</li>
          <li><strong>Walton, D. (1996).</strong> <em>Argumentation Schemes for Presumptive Reasoning</em>. Lawrence Erlbaum Associates.</li>
          <li><strong>Mathur, A., et al. (2019).</strong> Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. <em>Proc. ACM Hum.-Comput. Interact.</em>, 3(CSCW).</li>
          <li><strong>Festinger, L. (1957).</strong> <em>A Theory of Cognitive Dissonance</em>. Stanford University Press.</li>
        </ul>
      </section>
    </article>
  );
}
