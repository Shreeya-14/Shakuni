import React, { useState } from 'react';
import { Send, RotateCcw, AlertTriangle, Compass, FileText } from 'lucide-react';

const DOSSIER_EXAMPLES = [
  {
    code: 'EX-01',
    label: 'Social Pressure',
    text: "Everyone on the executive team has already signed the loyalty agreement; don't be the lone dissenter holding us back."
  },
  {
    code: 'EX-02',
    label: 'Emotional Pressure',
    text: "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer."
  },
  {
    code: 'EX-03',
    label: 'Misleading Framing',
    text: "You are either completely with our bold organizational turnaround strategy, or you actively want the company to fail."
  },
  {
    code: 'EX-04',
    label: 'Selective Info',
    text: "Our revolutionary battery technology demonstrated a four hundred percent charge retention in controlled lab tests."
  },
  {
    code: 'EX-05',
    label: 'Deceptive Persuasion',
    text: "I just spoke directly with the CEO, and she authorized us to bypass standard compliance reviews for this wire transfer."
  },
  {
    code: 'EX-06',
    label: 'Neutral Baseline',
    text: "The scheduled software release has been postponed to Tuesday to complete standard regression testing."
  }
];

export default function AnalyzerForm({ onAnalyze, isLoading, error }) {
  const [inputText, setInputText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputText.trim() || isLoading) return;
    onAnalyze(inputText.trim());
  };

  const handleSelectCase = (text) => {
    setInputText(text);
  };

  const handleReset = () => {
    setInputText('');
  };

  const charCount = inputText.length;
  const isOverLimit = charCount > 10000;

  return (
    <div className="dossier-card">
      <form onSubmit={handleSubmit}>
        {/* Dossier Header */}
        <div className="card-header-editorial">
          <div className="card-header-tag">
            <FileText size={14} color="var(--accent-gold)" />
            <span>CASE FILE // INPUT TEXT SAMPLE</span>
          </div>
          <div className="card-header-counter" style={{ color: isOverLimit ? 'var(--accent-crimson)' : 'var(--text-muted)' }}>
            {charCount.toLocaleString()} / 10,000 CHARACTERS
          </div>
        </div>

        {/* Input Textarea Area */}
        <div className="case-input-container">
          <textarea
            id="message-input"
            className="case-textarea"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter a message, statement, advertisement, post, or dialogue to analyze..."
            rows={6}
            disabled={isLoading}
          />
        </div>

        {/* Research Case Samples */}
        <div className="case-samples-section">
          <span className="case-samples-label">Curated Research Case Samples:</span>
          <div className="case-samples-pills">
            {DOSSIER_EXAMPLES.map((sample) => (
              <button
                key={sample.code}
                type="button"
                className="case-sample-pill"
                onClick={() => handleSelectCase(sample.text)}
                disabled={isLoading}
              >
                <span style={{ color: 'var(--accent-gold)', marginRight: '0.35rem' }}>{sample.code}</span>
                {sample.label}
              </button>
            ))}
          </div>
        </div>

        {/* Error Feedback */}
        {error && (
          <div style={{ padding: '0 1.5rem 1rem' }}>
            <div className="error-dossier-banner">
              <AlertTriangle size={18} style={{ flexShrink: 0, color: 'var(--accent-crimson)' }} />
              <span>{error}</span>
            </div>
          </div>
        )}

        {/* Action Controls Bar */}
        <div className="case-action-bar">
          <div className="case-policy-note">
            NLP feature vectorizer identifies asymmetric disclosure, cognitive pressure framing, and deceptive rhetoric.
          </div>

          <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
            {inputText && (
              <button
                type="button"
                className="btn-clear"
                onClick={handleReset}
                disabled={isLoading}
              >
                <RotateCcw size={13} />
                Clear
              </button>
            )}

            <button
              type="submit"
              className="btn-wine-primary"
              disabled={!inputText.trim() || isLoading || isOverLimit}
            >
              <Send size={14} />
              {isLoading ? 'Analyzing communication pattern...' : 'Analyze Message'}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
