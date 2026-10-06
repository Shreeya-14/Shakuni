import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { CATEGORIES_DATA } from '../data/categories';
import CategoryBadge from '../components/CategoryBadge';
import { 
  Layers, 
  Search, 
  ArrowRight, 
  ShieldAlert, 
  Sliders, 
  Tag, 
  CornerDownRight, 
  Compass, 
  ChevronRight 
} from 'lucide-react';

export default function Patterns() {
  const [selectedCategoryIndex, setSelectedCategoryIndex] = useState(0);
  const navigate = useNavigate();

  const currentCategory = CATEGORIES_DATA[selectedCategoryIndex] || CATEGORIES_DATA[0];

  const handleTestExample = (exampleText) => {
    navigate(`/analyze?sample=${encodeURIComponent(exampleText)}`);
  };

  return (
    <div className="patterns-page-container">
      {/* Header */}
      <header className="patterns-page-header">
        <span className="patterns-eyebrow">TAXONOMIC REPOSITORY // 07 CATEGORIES</span>
        <h1 className="patterns-page-title">Seven ways language can influence a decision.</h1>
        <p className="patterns-page-lead">
          Strategic communication rarely relies on overt falsehoods. Rather, influence is exercised by altering the decision space: manufacturing consensus, anchoring false dilemmas, omitting material caveats, or generating artificial urgency.
        </p>
      </header>

      {/* Main Two-Column Interactive Explorer */}
      <div className="patterns-explorer-layout">
        {/* Left Column: Vertical Category Navigation Index */}
        <div className="patterns-sidebar-nav" role="tablist" aria-label="Category Selection">
          <div className="patterns-sidebar-header">
            <span>CATEGORICAL INDEX</span>
            <span>BASE RISK</span>
          </div>

          <div className="patterns-nav-items-list">
            {CATEGORIES_DATA.map((cat, idx) => {
              const isSelected = idx === selectedCategoryIndex;
              return (
                <button
                  key={cat.id}
                  type="button"
                  role="tab"
                  aria-selected={isSelected}
                  className={`pattern-nav-item ${isSelected ? 'active' : ''}`}
                  onClick={() => setSelectedCategoryIndex(idx)}
                >
                  <div className="pattern-nav-left">
                    <span className="pattern-nav-code">{cat.code}</span>
                    <strong className="pattern-nav-title">{cat.name}</strong>
                  </div>
                  <div className="pattern-nav-right">
                    <span className={`pattern-nav-tier-tag ${cat.riskTier.toLowerCase()}`}>
                      {cat.riskTier}
                    </span>
                    <ChevronRight size={14} className="pattern-nav-arrow" />
                  </div>
                </button>
              );
            })}
          </div>

          <div className="patterns-sidebar-summary">
            <ShieldAlert size={14} color="var(--brand-burgundy)" />
            <span>Each category carries a calibrated baseline severity score (10–88) utilized in composite risk formulation.</span>
          </div>
        </div>

        {/* Right Column: Deep-Dive Pattern Detail Dossier */}
        <div className="patterns-detail-panel" role="tabpanel">
          {/* Top Metadata Strip */}
          <div className="pattern-detail-top-strip">
            <div className="pattern-detail-code-badge">
              <span>{currentCategory.code}</span>
              <span>// TAXONOMIC PROFILE</span>
            </div>
            <div className="pattern-detail-risk-indicator">
              <span className={`risk-tier-badge ${currentCategory.riskTier.toLowerCase()}`}>
                {currentCategory.riskTier} Risk ({currentCategory.riskScoreRange})
              </span>
              <span className="pattern-base-weight">
                Base Weight: {currentCategory.baseRiskWeight} / 100
              </span>
            </div>
          </div>

          {/* Heading & Tagline */}
          <div className="pattern-detail-title-cluster">
            <h2 className="pattern-detail-heading">{currentCategory.name}</h2>
            <p className="pattern-detail-tagline">{currentCategory.tagline}</p>
            <div style={{ marginTop: '0.75rem' }}>
              <CategoryBadge category={currentCategory.name} />
            </div>
          </div>

          {/* Core Content Blocks */}
          <div className="pattern-detail-body">
            {/* 1. Definition */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <Compass size={14} color="var(--brand-burgundy)" />
                <span>Formal Taxonomic Definition</span>
              </div>
              <p className="detail-block-text">
                {currentCategory.description}
              </p>
            </div>

            {/* 2. What the Model Looks For */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <Sliders size={14} color="var(--brand-burgundy)" />
                <span>What the Model Looks For (Lexical & Syntactic Features)</span>
              </div>
              <p className="detail-block-text">
                {currentCategory.whatModelLooksFor}
              </p>
            </div>

            {/* 3. Typical Indicators */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <Tag size={14} color="var(--brand-burgundy)" />
                <span>Typical Linguistic Indicators & Evidentiary Markers</span>
              </div>
              <div className="pattern-indicators-grid">
                {currentCategory.typicalIndicators.map((ind, i) => (
                  <div key={i} className="pattern-indicator-cell">
                    <CornerDownRight size={12} color="var(--brand-burgundy)" style={{ flexShrink: 0 }} />
                    <span>{ind}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* 4. Representative Example */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <Layers size={14} color="var(--brand-burgundy)" />
                <span>Curated Research Text Sample</span>
              </div>
              <div className="pattern-example-quote-box">
                <blockquote className="pattern-example-quote">
                  "{currentCategory.example}"
                </blockquote>
                <div className="pattern-quote-actions">
                  <button 
                    type="button" 
                    className="btn-primary-burgundy btn-sm"
                    onClick={() => handleTestExample(currentCategory.example)}
                  >
                    <Search size={13} />
                    <span>Analyze this sample in Workspace</span>
                  </button>
                </div>
              </div>
            </div>

            {/* 5. Qualitative Risk Interpretation */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <ShieldAlert size={14} color="var(--brand-burgundy)" />
                <span>Qualitative Risk Interpretation & Psychological Impact</span>
              </div>
              <p className="detail-block-text">
                {currentCategory.riskInterpretation}
              </p>
            </div>

            {/* 6. Related Categories */}
            <div className="pattern-detail-block">
              <div className="detail-block-header">
                <Layers size={14} color="var(--brand-burgundy)" />
                <span>Related Categorical Overlaps</span>
              </div>
              <div className="related-cats-row">
                {currentCategory.relatedCategories.map((relCat, idx) => (
                  <span key={idx} className="related-cat-pill">
                    {relCat}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
