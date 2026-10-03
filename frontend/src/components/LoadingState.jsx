import React, { useState, useEffect } from 'react';

const ANALYSIS_STAGES = [
  'Extracting lexical n-grams & linguistic indicators...',
  'Evaluating manipulation pattern classifiers...',
  'Calculating probabilistic posterior distribution...',
  'Synthesizing contextual intelligence brief...'
];

export default function LoadingState() {
  const [stageIndex, setStageIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setStageIndex((prev) => (prev + 1) % ANALYSIS_STAGES.length);
    }, 1100);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dossier-card loading-dossier" style={{ marginTop: '2rem' }}>
      <div className="loading-die-orbit">
        <svg viewBox="0 0 48 48" width="56" height="56" fill="none">
          <polygon points="24,4 44,15 24,26 4,15" stroke="#c5a059" strokeWidth="1.5" fill="rgba(197, 160, 89, 0.08)" />
          <polygon points="4,15 24,26 24,44 4,33" stroke="#8b1e3f" strokeWidth="1.5" fill="rgba(139, 30, 63, 0.12)" />
          <polygon points="44,15 24,26 24,44 44,33" stroke="#c5a059" strokeWidth="1.5" fill="rgba(197, 160, 89, 0.05)" />
          <circle cx="24" cy="15" r="2" fill="#f5f2eb" />
          <circle cx="14" cy="28" r="1.5" fill="#c5a059" />
          <circle cx="34" cy="28" r="1.5" fill="#8b1e3f" />
        </svg>
      </div>

      <div className="loading-headline">Analyzing communication pattern...</div>
      <div className="loading-stepper">{ANALYSIS_STAGES[stageIndex]}</div>
    </div>
  );
}
