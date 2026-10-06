import React from 'react';
import { Compass, ShieldAlert, BarChart3, Binary, Layers } from 'lucide-react';

export default function EmptyWorkspace() {
  return (
    <div className="empty-workspace-card" role="region" aria-label="Analysis report placeholder">
      <div className="empty-workspace-motif">
        <svg viewBox="0 0 80 80" width="72" height="72" fill="none">
          {/* Subtle Geometric Dice & Strategic Coordinate Grid */}
          <circle cx="40" cy="40" r="38" stroke="rgba(184, 144, 71, 0.2)" strokeWidth="1" strokeDasharray="3 3" />
          <polygon points="40,10 68,26 40,42 12,26" stroke="#b89047" strokeWidth="1.5" fill="#fcf9f2" />
          <polygon points="12,26 40,42 40,70 12,54" stroke="#7a1c30" strokeWidth="1.5" fill="#faedf0" />
          <polygon points="68,26 40,42 40,70 68,54" stroke="#b89047" strokeWidth="1.5" fill="#f8f4eb" />
          <circle cx="40" cy="26" r="2.5" fill="#7a1c30" />
          <circle cx="26" cy="48" r="2" fill="#b89047" />
          <circle cx="54" cy="48" r="2" fill="#7a1c30" />
        </svg>
      </div>

      <div className="empty-workspace-badge">
        <span>AWAITING INPUT TEXT</span>
      </div>

      <h3 className="empty-workspace-title">Your analysis will appear here.</h3>
      <p className="empty-workspace-desc">
        Paste any email, statement, dialogue, advertisement, or executive brief into the left panel. The NLP engine will parse lexical structures and generate an explainable intelligence brief.
      </p>

      <div className="empty-features-grid">
        <div className="empty-feature-item">
          <div className="empty-feature-icon">
            <Layers size={14} color="var(--brand-burgundy)" />
          </div>
          <div>
            <strong>7 Pattern Classifiers</strong>
            <p>Categorizes pressure, framing traps, selective data, or withholding.</p>
          </div>
        </div>

        <div className="empty-feature-item">
          <div className="empty-feature-icon">
            <BarChart3 size={14} color="var(--brand-burgundy)" />
          </div>
          <div>
            <strong>Calibrated Risk Score</strong>
            <p>Weighted 0–100 threat index derived from category mass and confidence.</p>
          </div>
        </div>

        <div className="empty-feature-item">
          <div className="empty-feature-icon">
            <Binary size={14} color="var(--brand-burgundy)" />
          </div>
          <div>
            <strong>Evidence Isolation</strong>
            <p>Flags exact surface syntactic patterns and n-gram markers.</p>
          </div>
        </div>
      </div>
    </div>
  );
}
