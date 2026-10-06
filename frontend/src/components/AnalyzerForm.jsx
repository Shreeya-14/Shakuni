import React, { useState } from 'react';
import { Send, RotateCcw, AlertTriangle, FileText } from 'lucide-react';

const DOSSIER_EXAMPLES = [
  {
    code: '01',
    label: 'Social Pressure',
    text: "Everyone on the executive team has already signed the loyalty agreement; don't be the lone dissenter holding us back."
  },
  {
    code: '02',
    label: 'Emotional Pressure',
    text: "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer."
  },
  {
    code: '03',
    label: 'Misleading Framing',
    text: "You are either completely with our bold organizational turnaround strategy, or you actively want the company to fail."
  },
  {
    code: '04',
    label: 'Selective Info',
    text: "Our revolutionary battery technology demonstrated a four hundred percent charge retention in controlled lab tests."
  },
  {
    code: '05',
    label: 'Withholding',
    text: "The platform upgrade will go live at midnight as agreed. We will address any pending secondary configuration items during later maintenance cycles."
  },
  {
    code: '06',
    label: 'Deceptive Persuasion',
    text: "I just spoke directly with the CEO, and she authorized us to bypass standard compliance reviews for this wire transfer."
  },
  {
    code: '07',
    label: 'Normal Text',
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
    <div className="analyzer-workspace-card">
      <form onSubmit={handleSubmit}>
        {/* Workspace Card Header */}
        <div className="workspace-header">
          <div className="workspace-label">
            <FileText size={14} color="var(--brand-burgundy)" />
            <span>CASE FILE // INPUT TEXT SAMPLE</span>
          </div>
          <div 
            className="workspace-counter" 
            style={{ color: isOverLimit ? '#8c1e34' : 'var(--text-muted)' }}
          >
            {charCount.toLocaleString()} / 10,000 CHARACTERS
          </div>
        </div>

        {/* Text Input Area */}
        <div className="textarea-container">
          <textarea
            id="message-input"
            className="editorial-textarea"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter a message, statement, advertisement, post, or dialogue to analyze..."
            rows={5}
            disabled={isLoading}
            aria-label="Text to analyze for manipulation patterns"
          />
        </div>

        {/* Curated Research Cases */}
        <div className="example-cases-bar">
          <span className="example-cases-title">Curated Research Case Samples:</span>
          <div className="example-cases-grid">
            {DOSSIER_EXAMPLES.map((sample) => (
              <button
                key={sample.code}
                type="button"
                className="example-case-btn"
                onClick={() => handleSelectCase(sample.text)}
                disabled={isLoading}
              >
                <span className="num">{sample.code}</span>
                {sample.label}
              </button>
            ))}
          </div>
        </div>

        {/* Error Notification */}
        {error && (
          <div className="error-editorial-banner" role="alert">
            <AlertTriangle size={16} style={{ flexShrink: 0 }} />
            <span>{error}</span>
          </div>
        )}

        {/* Action Controls Footer */}
        <div className="workspace-footer">
          <div className="workspace-disclaimer">
            NLP feature vectorizer identifies asymmetric disclosure, cognitive pressure framing, and deceptive persuasion patterns.
          </div>

          <div className="workspace-actions">
            {inputText && (
              <button
                type="button"
                className="btn-secondary-light"
                onClick={handleReset}
                disabled={isLoading}
              >
                <RotateCcw size={13} />
                Clear
              </button>
            )}

            <button
              type="submit"
              className="btn-primary-burgundy"
              disabled={!inputText.trim() || isLoading || isOverLimit}
            >
              <Send size={14} />
              {isLoading ? 'Analyzing...' : 'Analyze Message'}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
