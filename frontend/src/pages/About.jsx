import React from 'react';
import { 
  Info, 
  ShieldCheck, 
  Cpu, 
  Code2, 
  Terminal, 
  BookOpen, 
  Users, 
  Scale, 
  ExternalLink,
  Layers,
  Sparkles
} from 'lucide-react';

export default function About() {
  return (
    <article className="editorial-monograph" role="article">
      {/* Header */}
      <header className="monograph-header">
        <span className="monograph-ref">PLATFORM OVERVIEW // ABOUT SHAKUNI</span>
        <h1 className="monograph-title">A Strategic Lens on Modern Communication</h1>
        <p className="monograph-abstract">
          Shakuni is an academic research platform investigating how language can be strategically structured to create cognitive pressure, manufactured consensus, and informational asymmetry.
        </p>
      </header>

      {/* 1. Project Purpose */}
      <section className="monograph-section">
        <span className="monograph-sec-number">PROJECT MISSION</span>
        <h2 className="monograph-sec-title">
          <Info size={20} color="var(--brand-burgundy)" />
          Why We Built Shakuni
        </h2>
        <p>
          In high-stakes environments—boardrooms, investment prospectuses, marketing campaigns, and interpersonal relationships—influence rarely announces itself through overt toxicity, profanity, or blatant fabrications. Instead, persuasion is orchestrated through <strong>asymmetric framing</strong>: forcing choices into false dichotomies, citing cherry-picked statistics without baseline controls, or withholding material caveats until commitments are locked.
        </p>
        <p>
          Shakuni was created as a transparent research framework to analyze these communication maneuvers. Rather than trusting opaque multi-billion-parameter neural networks that hallucinate confidence, Shakuni couples <strong>interpretable scikit-learn models</strong> with deterministic linguistic indicators to yield fully auditable intelligence reports.
        </p>
      </section>

      {/* 2. Core Pillars */}
      <section className="monograph-section">
        <span className="monograph-sec-number">FOUNDATIONAL PRINCIPLES</span>
        <h2 className="monograph-sec-title">
          <Layers size={20} color="var(--brand-burgundy)" />
          Three Core Pillars
        </h2>

        <div className="monograph-briefs-grid">
          <div className="monograph-brief-box">
            <h4>01. Explainable NLP Architecture</h4>
            <p>Every classification score is derived from transparent linear weights and identifiable surface text features. No black-box guesses or unverified assertions.</p>
          </div>

          <div className="monograph-brief-box">
            <h4>02. Game-Theoretic Asymmetry</h4>
            <p>Rhetoric is audited as strategic signaling where one actor holds informational advantage and alters the perceived payoff matrix of the recipient.</p>
          </div>

          <div className="monograph-brief-box">
            <h4>03. Strict Judicial Restraint</h4>
            <p>The framework evaluates communicative structure, never human intent. It rejects the false promise of "AI lie detection" in favor of disciplined linguistic auditing.</p>
          </div>
        </div>
      </section>

      {/* 3. Technology Stack Breakdown */}
      <section className="monograph-section">
        <span className="monograph-sec-number">TECHNICAL STACK</span>
        <h2 className="monograph-sec-title">
          <Code2 size={20} color="var(--brand-burgundy)" />
          Platform Architecture & Libraries
        </h2>

        <div className="tech-stack-cards-grid">
          <div className="tech-card">
            <span className="tech-card-category">FRONTEND CLIENT</span>
            <strong className="tech-card-title">React 18 & Vite</strong>
            <p className="tech-card-desc">Multi-page routing via React Router DOM, modern JavaScript ES modules, Lucide icons, and a custom light editorial CSS design system.</p>
          </div>

          <div className="tech-card">
            <span className="tech-card-category">BACKEND SERVICE</span>
            <strong className="tech-card-title">FastAPI & Python 3.11</strong>
            <p className="tech-card-desc">High-performance asynchronous REST API, Pydantic v2 data validation schemas, CORS middleware, and Uvicorn ASGI server.</p>
          </div>

          <div className="tech-card">
            <span className="tech-card-category">MACHINE LEARNING</span>
            <strong className="tech-card-title">Scikit-learn & TF-IDF</strong>
            <p className="tech-card-desc">Sublinear unigram/bigram vectorizer (4,595 features), Multinomial Logistic Regression with balanced class weights, and Joblib serialization.</p>
          </div>

          <div className="tech-card">
            <span className="tech-card-category">TESTING & VALIDATION</span>
            <strong className="tech-card-title">Pytest Test Suite</strong>
            <p className="tech-card-desc">27 automated unit and integration tests covering vectorization integrity, model convergence, scoring calibration, and API contracts.</p>
          </div>
        </div>
      </section>

      {/* 4. Ethical Principles */}
      <section className="monograph-section" id="ethics">
        <span className="monograph-sec-number">ETHICAL GOVERNANCE</span>
        <h2 className="monograph-sec-title">
          <Scale size={20} color="var(--brand-burgundy)" />
          Ethical Principles & Responsible Use
        </h2>

        <div className="ethical-principles-container">
          <div className="ethical-principle-item">
            <ShieldCheck size={18} color="var(--brand-burgundy)" style={{ flexShrink: 0 }} />
            <div>
              <strong>Not a Lie Detector</strong>
              <p>Shakuni analyzes linguistic patterns in surface text. It cannot verify external facts against ground truth without external feeds and cannot determine whether a speaker is lying.</p>
            </div>
          </div>

          <div className="ethical-principle-item">
            <ShieldCheck size={18} color="var(--brand-burgundy)" style={{ flexShrink: 0 }} />
            <div>
              <strong>Human-in-the-Loop Mandate</strong>
              <p>Scores are probabilistic aids designed to assist media literacy and communication auditing. They must never be used as autonomous grounds for disciplinary action, censorship, or legal sanction.</p>
            </div>
          </div>

          <div className="ethical-principle-item">
            <ShieldCheck size={18} color="var(--brand-burgundy)" style={{ flexShrink: 0 }} />
            <div>
              <strong>Privacy-Preserving Training Corpus</strong>
              <p>The model was trained exclusively on 280 peer-reviewed curated and synthetic research samples. No private user conversations or unconsented feeds were harvested.</p>
            </div>
          </div>
        </div>
      </section>

      {/* 5. Team & Academic Affiliation Placeholder */}
      <section className="monograph-section">
        <span className="monograph-sec-number">ACADEMIC ORIENTATION</span>
        <h2 className="monograph-sec-title">
          <Users size={20} color="var(--brand-burgundy)" />
          Research Project Context
        </h2>
        <p>
          This project was conceived and developed as a university research prototype in natural language processing and strategic communication analysis:
        </p>

        <div className="team-cards-grid">
          <div className="team-member-card">
            <span className="member-role">PRINCIPAL RESEARCHER & DEVELOPER</span>
            <strong className="member-name">Shakuni Engineering Project</strong>
            <p className="member-desc">Full-stack NLP architecture, TF-IDF model training, risk formulation algorithms, and React editorial design system.</p>
          </div>

          <div className="team-member-card">
            <span className="member-role">ACADEMIC SUPERVISION</span>
            <strong className="member-name">Department of Computer Science</strong>
            <p className="member-desc">Research guidance on probabilistic text classification, explainable AI, and ethical governance standards.</p>
          </div>
        </div>
      </section>
    </article>
  );
}
