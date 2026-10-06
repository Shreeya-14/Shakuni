import React from 'react';

export default function RiskIndicator({ score = 0, level = 'Low' }) {
  const normalizedScore = Math.max(0, Math.min(100, Math.round(score)));
  
  const tierClass = level.toLowerCase() === 'high' 
    ? 'high' 
    : level.toLowerCase() === 'moderate' 
      ? 'moderate' 
      : 'low';

  return (
    <div className="risk-meter-container">
      <div className="risk-score-display">
        <span className="risk-score-number">{normalizedScore}</span>
        <span className="risk-score-denom">/ 100</span>
        <span className={`risk-tier-badge ${tierClass}`}>
          {level} Risk
        </span>
      </div>

      <div 
        className="risk-spectrum-bar" 
        role="progressbar" 
        aria-valuenow={normalizedScore} 
        aria-valuemin={0} 
        aria-valuemax={100}
        aria-label={`Calculated risk score: ${normalizedScore} out of 100 (${level} Risk)`}
      >
        <div className="spectrum-segment low" title="Low: 0–39" />
        <div className="spectrum-segment moderate" title="Moderate: 40–69" />
        <div className="spectrum-segment high" title="High: 70–100" />
        <div 
          className="spectrum-indicator-pin" 
          style={{ left: `calc(${normalizedScore}% - 2px)` }} 
        />
      </div>

      <div className="spectrum-labels">
        <span>0 LOW (0–39)</span>
        <span>40 MODERATE (40–69)</span>
        <span>70 HIGH (70–100)</span>
      </div>
    </div>
  );
}
