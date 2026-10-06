import React from 'react';
import { History, Trash2, ArrowUpRight } from 'lucide-react';
import CategoryBadge from './CategoryBadge';

export default function AnalysisHistory({ history = [], onSelect, onClear }) {
  if (!history || history.length === 0) {
    return (
      <div className="history-drawer-empty">
        <History size={15} color="var(--text-muted)" />
        <span>Recent analyses in this browser session will be stored here.</span>
      </div>
    );
  }

  return (
    <div className="history-panel">
      <div className="history-header">
        <div className="history-title">
          <History size={14} color="var(--brand-burgundy)" />
          <span>RECENT ANALYSES ({history.length})</span>
        </div>
        <button 
          type="button" 
          className="btn-history-clear" 
          onClick={onClear}
          title="Clear stored analysis history"
        >
          <Trash2 size={12} />
          <span>Clear History</span>
        </button>
      </div>

      <div className="history-list">
        {history.map((item, index) => {
          const tierClass = (item.risk_level || 'low').toLowerCase();
          return (
            <div 
              key={item.id || index} 
              className="history-item"
              onClick={() => onSelect(item)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  onSelect(item);
                }
              }}
              title="Click to reload this analysis report"
            >
              <div className="history-item-top">
                <span className="history-item-cat">{item.category}</span>
                <span className={`history-risk-pill ${tierClass}`}>
                  {item.risk_score}/100 {item.risk_level}
                </span>
              </div>
              <p className="history-item-snippet">
                "{item.text ? item.text.slice(0, 90) : ''}{item.text && item.text.length > 90 ? '...' : ''}"
              </p>
              <div className="history-item-footer">
                <span className="history-time">{item.timestamp || 'Just now'}</span>
                <span className="history-load-link">
                  Reopen <ArrowUpRight size={11} style={{ display: 'inline' }} />
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
