import React, { useState, useEffect } from 'react';

const ANALYSIS_STAGES = [
  'Reading communication & standardizing tokens...',
  'Extracting lexical n-grams & rhetorical indicators...',
  'Evaluating multinomial category classifiers...',
  'Computing posterior probability distribution...',
  'Synthesizing contextual rationale dossier...'
];

export default function LoadingState() {
  const [stageIndex, setStageIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setStageIndex((prev) => (prev + 1) % ANALYSIS_STAGES.length);
    }, 750);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="loading-editorial-box" role="status" aria-live="polite">
      <div className="spinner-dice-orbit">
        <svg viewBox="0 0 48 48" width="48" height="48" fill="none">
          <polygon points="24,4 44,15 24,26 4,15" stroke="#b89047" strokeWidth="1.5" fill="#fdfaf4" />
          <polygon points="4,15 24,26 24,44 4,33" stroke="#7a1c30" strokeWidth="1.5" fill="#f8edf0" />
          <polygon points="44,15 24,26 24,44 44,33" stroke="#b89047" strokeWidth="1.5" fill="#fbf8f0" />
          <circle cx="24" cy="15" r="2" fill="#7a1c30" />
          <circle cx="14" cy="28" r="1.5" fill="#b89047" />
          <circle cx="34" cy="28" r="1.5" fill="#7a1c30" />
        </svg>
      </div>

      <div className="loading-main-text">Analyzing communication pattern...</div>
      <div className="loading-sub-text">{ANALYSIS_STAGES[stageIndex]}</div>
    </div>
  );
}

export { LoadingState as LoadingDossier };
