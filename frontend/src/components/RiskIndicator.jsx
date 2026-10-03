import React from 'react';

export default function RiskIndicator({ score = 0, level = 'Low' }) {
  const normalizedScore = Math.max(0, Math.min(100, score));
  const radius = 58;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (normalizedScore / 100) * circumference;

  let strokeColor = '#78907a'; // Low / Sage
  let tierClass = 'low';

  if (level === 'Moderate') {
    strokeColor = '#c48037'; // Amber
    tierClass = 'moderate';
  } else if (level === 'High') {
    strokeColor = '#a62639'; // Deep Crimson / Wine
    tierClass = 'high';
  }

  return (
    <div className="precision-risk-panel">
      <div className="radial-gauge-container">
        <svg className="gauge-svg-precision" viewBox="0 0 144 144">
          {/* Faint Concentric Alignment Ring */}
          <circle
            cx="72"
            cy="72"
            r="66"
            fill="none"
            stroke="rgba(197, 160, 89, 0.08)"
            strokeWidth="1"
            strokeDasharray="2 4"
          />
          {/* Background Track */}
          <circle
            className="gauge-track"
            cx="72"
            cy="72"
            r={radius}
          />
          {/* Active Precision Arc */}
          <circle
            className="gauge-stroke-fill"
            cx="72"
            cy="72"
            r={radius}
            stroke={strokeColor}
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
          />
        </svg>

        <div className="gauge-inner-content">
          <span className="gauge-main-score" style={{ color: strokeColor }}>
            {normalizedScore}
          </span>
          <span className="gauge-denominator">SCALE / 100</span>
        </div>
      </div>

      <div className={`risk-tier-tag ${tierClass}`}>
        {level} Manipulation Risk
      </div>

      <p style={{ fontFamily: 'var(--font-mono)', fontSize: '0.68rem', color: 'var(--text-muted)', letterSpacing: '0.08em', textTransform: 'uppercase' }}>
        Rhetorical Threat Intensity
      </p>
    </div>
  );
}
