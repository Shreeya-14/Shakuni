import React, { useState } from 'react';
import AnalyzerForm from '../components/AnalyzerForm';
import ResultCard from '../components/ResultCard';
import LoadingState from '../components/LoadingState';
import { analyzeText } from '../services/api';
import { Compass, RotateCcw, ShieldCheck, ChevronRight } from 'lucide-react';

const STRATEGIC_VECTORS = [
  { code: '01', name: 'Normal / Neutral', tier: 'Low Risk' },
  { code: '02', name: 'Social Pressure', tier: 'Moderate' },
  { code: '03', name: 'Emotional Pressure', tier: 'High' },
  { code: '04', name: 'Misleading Framing', tier: 'Moderate' },
  { code: '05', name: 'Selective Information', tier: 'Moderate' },
  { code: '06', name: 'Information Withholding', tier: 'High' },
  { code: '07', name: 'Deceptive Persuasion', tier: 'High' }
];

export default function Home() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async (text) => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await analyzeText(text);
      setAnalysisResult(data);
    } catch (err) {
      console.error('Analysis error:', err);
      setError(err.message || 'Failed to analyze text. Please verify backend service connectivity.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewAnalysis = () => {
    setAnalysisResult(null);
    setError(null);
  };

  return (
    <div className="home-container">
      {/* Editorial Hero Header */}
      <section className="hero-editorial">
        <div className="hero-eyebrow">
          <div className="hero-eyebrow-pip" />
          <span>Strategic Communication Analysis // Covert Pattern Intelligence</span>
        </div>
        <h2 className="hero-headline">
          Every message has a <em>strategy</em>.
        </h2>
        <p className="hero-description">
          Shakuni examines language for patterns of pressure, framing, selective information, withholding, and deceptive persuasion.
        </p>
      </section>

      {/* Main Workspace Section */}
      {!analysisResult && !isLoading && (
        <div className="workspace-grid">
          {/* Left Column: Case Input Form */}
          <div className="workspace-input-col">
            <AnalyzerForm 
              onAnalyze={handleAnalyze} 
              isLoading={isLoading} 
              error={error} 
            />
          </div>

          {/* Right Column: Strategic Visual Intelligence Preview */}
          <div className="workspace-preview-col">
            <div className="dossier-card preview-panel">
              <div className="preview-header">
                <Compass size={14} color="var(--accent-gold)" />
                <span>The Architecture of Asymmetry</span>
              </div>
              <h3 className="preview-title">Information As a Tactical Move</h3>
              <p className="preview-desc">
                Strategic communication rarely relies on overt falsehoods. Instead, influence is exercised by altering the decision space: manufacturing urgency, anchoring false dilemmas, and withholding material caveats.
              </p>

              {/* Manipulation Vectors Matrix */}
              <div className="vectors-matrix">
                {STRATEGIC_VECTORS.map((v) => (
                  <div key={v.code} className="vector-row">
                    <span className="vector-code">VEC-{v.code}</span>
                    <span className="vector-name">{v.name}</span>
                    <span className="vector-tier">{v.tier}</span>
                  </div>
                ))}
              </div>

              {/* Geometric Dice Motif Box */}
              <div className="dice-motif-graphic">
                <svg viewBox="0 0 36 36" width="36" height="36" fill="none" style={{ flexShrink: 0 }}>
                  <polygon points="18,3 33,11 18,20 3,11" stroke="#c5a059" strokeWidth="1.2" fill="rgba(197, 160, 89, 0.08)" />
                  <polygon points="3,11 18,20 18,33 3,24" stroke="#8b1e3f" strokeWidth="1.2" fill="rgba(139, 30, 63, 0.12)" />
                  <polygon points="33,11 18,20 18,33 33,24" stroke="#c5a059" strokeWidth="1.2" fill="rgba(197, 160, 89, 0.04)" />
                  <circle cx="18" cy="11" r="1.5" fill="#f5f2eb" />
                  <circle cx="10" cy="22" r="1.2" fill="#c5a059" />
                  <circle cx="26" cy="22" r="1.2" fill="#8b1e3f" />
                </svg>
                <div className="dice-motif-desc">
                  <strong>Game-Theoretic Framework:</strong> Evaluates rhetoric as asymmetric signaling where the speaker holds informational advantage over the receiver.
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Loading Dossier Animation */}
      {isLoading && <LoadingState />}

      {/* Analysis Result Dossier Brief */}
      {!isLoading && analysisResult && (
        <div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '1rem' }}>
            <button 
              type="button" 
              className="btn-clear" 
              onClick={handleNewAnalysis}
            >
              <RotateCcw size={13} />
              Analyze Another Statement
            </button>
          </div>

          <ResultCard result={analysisResult} />
        </div>
      )}
    </div>
  );
}
