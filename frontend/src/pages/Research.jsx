import React from 'react';
import { Target, BookOpen, GitCompare, Network, Scale, ShieldAlert, Award } from 'lucide-react';

export default function Research() {
  return (
    <div className="editorial-page">
      {/* Editorial Header */}
      <header className="editorial-header">
        <span className="editorial-doc-code">RESEARCH BRIEF // MONOGRAPH 02</span>
        <h2 className="editorial-title">Conceptual Foundations & Theoretical Context</h2>
        <p className="editorial-subtitle">
          Investigating the dynamics of strategic information manipulation, cognitive vulnerability exploitation, and conversational asymmetry through computational discourse analysis.
        </p>
      </header>

      {/* The Problem */}
      <section className="editorial-section">
        <span className="editorial-section-num">THE PROBLEM</span>
        <h3 className="editorial-section-heading">The Hidden Mechanics of Covert Influence</h3>
        <p>
          Contemporary digital discourse analysis has excelled at catching overt hostility, explicit profanity, and crude disinformation. Yet the most destructive forms of manipulation—coercive workplace pressure, fraudulent investment prospectuses, and emotionally abusive interpersonal communications—operate almost exclusively within the confines of polite, professional, and seemingly reasoned dialogue.
        </p>
      </section>

      {/* The Concept: Shakuni Archetype */}
      <section className="editorial-section">
        <span className="editorial-section-num">THE CONCEPT</span>
        <h3 className="editorial-section-heading">
          <Target size={20} color="var(--accent-gold)" />
          The Shakuni Archetype: Asymmetric Information Warfare
        </h3>
        <p>
          In classical epic traditions (principally the Mahabharata), the figure of <strong>Shakuni</strong> serves as the archetype of strategic deception. Rather than relying on physical martial might, Shakuni orchestrated political outcomes by exploiting cognitive biases: inciting familial pride, manufacturing false choices, and skewing probability through the loaded dice game.
        </p>
        <p>
          In contemporary computational terms, the "loaded dice" metaphor directly maps to <strong>information asymmetry</strong>: when one party selectively presents evidence, conceals critical caveats, or manufactures synthetic social pressure, the decision environment is manipulated while preserving the surface illusion of fair consent.
        </p>
      </section>

      {/* Existing Approaches & Comparative Matrix */}
      <section className="editorial-section">
        <span className="editorial-section-num">EXISTING APPROACHES</span>
        <h3 className="editorial-section-heading">
          <GitCompare size={20} color="var(--accent-gold)" />
          Comparative Analysis of Analytical Paradigms
        </h3>
        <p>
          Existing automated discourse tools fail to capture the specific subtleties of strategic manipulation due to misaligned objective functions:
        </p>

        <div className="matrix-table-wrapper">
          <table className="matrix-table">
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
                <td style={{ fontWeight: 700, color: 'var(--accent-gold-light)' }}>Shakuni Framework</td>
                <td>Asymmetric framing, withholding, and rhetorical coercion</td>
                <td>7-Class Probability + Risk Score (0–100)</td>
                <td>Context-dependent sarcasm requiring external world knowledge.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      {/* Research Gap */}
      <section className="editorial-section">
        <span className="editorial-section-num">RESEARCH GAP</span>
        <h3 className="editorial-section-heading">
          <BookOpen size={20} color="var(--accent-gold)" />
          The Void in Contemporary Discourse NLP
        </h3>
        <p>
          While natural language processing has produced thousands of studies on sentiment and profanity, there exists a profound scarcity of computational frameworks dedicated to <strong>persuasive manipulation taxonomy</strong>.
        </p>
        <p>
          Shakuni addresses this gap by defining and validating a seven-category structure focused on how information is packaged and weaponized rather than whether it contains offensive words.
        </p>
      </section>

      {/* Our Architectural Approach */}
      <section className="editorial-section">
        <span className="editorial-section-num">OUR APPROACH</span>
        <h3 className="editorial-section-heading">
          <Network size={20} color="var(--accent-gold)" />
          Decoupled, Explainable Engineering
        </h3>
        <p>
          Rather than relying on uninterpretable billion-parameter models that hallucinate confidence, Shakuni combines:
        </p>
        <div className="brief-grid">
          <div className="brief-box">
            <h4>Calibrated Probabilities</h4>
            <p>Multinomial Logistic Regression delivers mathematically sound class distributions with verifiable coefficient contributions.</p>
          </div>
          <div className="brief-box">
            <h4>Evidence-Grounded Explanations</h4>
            <p>Every analysis extracts specific linguistic markers that anchor the qualitative rationale in surface text evidence.</p>
          </div>
        </div>
      </section>

      {/* Ethical Considerations & Responsible Use */}
      <section className="editorial-section">
        <span className="editorial-section-num">ETHICAL USE & RESPONSIBLE AI</span>
        <h3 className="editorial-section-heading">
          <Scale size={20} color="var(--accent-gold)" />
          Ethical Guardrails & Judicial Restraint
        </h3>
        <p>
          Deploying AI to evaluate human communication involves serious ethical responsibilities:
        </p>
        <div className="brief-grid">
          <div className="brief-box">
            <h4>Not a Lie Detector</h4>
            <p>Shakuni analyzes linguistic patterns. It never claims to evaluate whether a speaker is objectively lying or determine subjective moral guilt.</p>
          </div>
          <div className="brief-box">
            <h4>Human-in-the-Loop Mandate</h4>
            <p>Model scores must never be utilized as autonomous grounds for disciplinary action, content censorship, or legal sanction without human audit.</p>
          </div>
        </div>
      </section>

      {/* Academic Citations */}
      <section className="editorial-section">
        <span className="editorial-section-num">REFERENCES & SCHOLARLY LITERATURE</span>
        <h3 className="editorial-section-heading">
          <Award size={20} color="var(--accent-gold)" />
          Foundational Bibliography
        </h3>
        <ul style={{ paddingLeft: '1.25rem', color: 'var(--text-secondary)', lineHeight: '1.9', fontSize: '0.9rem' }}>
          <li><strong>Tversky, A., & Kahneman, D. (1981).</strong> The Framing of Decisions and the Psychology of Choice. <em>Science</em>, 211(4481), 453-458.</li>
          <li><strong>Cialdini, R. B. (2001).</strong> <em>Influence: Science and Practice</em> (4th ed.). Allyn & Bacon.</li>
          <li><strong>Walton, D. (1996).</strong> <em>Argumentation Schemes for Presumptive Reasoning</em>. Lawrence Erlbaum Associates.</li>
          <li><strong>Mathur, A., et al. (2019).</strong> Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. <em>Proc. ACM Hum.-Comput. Interact.</em>, 3(CSCW).</li>
          <li><strong>Festinger, L. (1957).</strong> <em>A Theory of Cognitive Dissonance</em>. Stanford University Press.</li>
        </ul>
      </section>
    </div>
  );
}
