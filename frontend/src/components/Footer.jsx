import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="editorial-footer-light" role="contentinfo">
      <div className="footer-inner-light">
        <div className="footer-left-col">
          <div className="footer-brand-title">
            <strong>SHAKUNI</strong>
            <span>// Strategic Communication Intelligence</span>
          </div>
          <p className="footer-desc">
            An academic research framework for computational analysis of strategic deception, coercive rhetoric, and information manipulation through natural language processing.
          </p>
          <div className="footer-disclaimer-chip">
            <ShieldCheck size={14} color="var(--brand-burgundy)" style={{ flexShrink: 0 }} />
            <span>Research prototype — model outputs are probabilistic and should not be treated as proof of deception.</span>
          </div>
        </div>

        <div className="footer-right-col">
          <div className="footer-nav-group">
            <span className="footer-group-heading">Platform</span>
            <ul className="footer-links-list">
              <li><Link to="/analyze" className="footer-nav-link">Analyze Workspace</Link></li>
              <li><Link to="/patterns" className="footer-nav-link">07 Patterns Index</Link></li>
              <li><Link to="/model" className="footer-nav-link">Model & Evaluation</Link></li>
            </ul>
          </div>

          <div className="footer-nav-group">
            <span className="footer-group-heading">Research</span>
            <ul className="footer-links-list">
              <li><Link to="/research" className="footer-nav-link">Conceptual Foundations</Link></li>
              <li><Link to="/about" className="footer-nav-link">About Project</Link></li>
              <li><Link to="/about#ethics" className="footer-nav-link">Ethical Principles</Link></li>
            </ul>
          </div>
        </div>
      </div>

      <div className="footer-bottom-bar">
        <div className="footer-bottom-inner">
          <span>&copy; {new Date().getFullYear()} Shakuni Intelligence Project. Academic & Research Prototype.</span>
          <span>TF-IDF + Multinomial Logistic Softmax Architecture</span>
        </div>
      </div>
    </footer>
  );
}
