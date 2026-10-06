import React from 'react';
import { Link } from 'react-router-dom';
import { Compass, ArrowLeft, Search, Layers, BookOpen, ShieldAlert } from 'lucide-react';

export default function NotFound() {
  return (
    <article className="editorial-monograph" role="article" style={{ maxWidth: '840px', margin: '4rem auto', textAlign: 'center' }}>
      <header className="monograph-header" style={{ borderBottom: 'none', paddingBottom: '1rem' }}>
        <span className="monograph-ref">
          <ShieldAlert size={14} style={{ verticalAlign: 'middle', marginRight: '6px' }} />
          ERROR 404 // UNRESOLVED REFERENCE
        </span>
        <h1 className="monograph-title" style={{ marginTop: '0.75rem', marginBottom: '1rem' }}>
          Coordinate Not Found
        </h1>
        <p className="monograph-abstract" style={{ margin: '0 auto', maxWidth: '600px' }}>
          The requested route does not correspond to an established document, pattern ledger, or evaluation record within the Shakuni framework.
        </p>
      </header>

      <div 
        style={{
          background: 'var(--bg-surface)',
          border: '1px solid var(--border-light)',
          borderRadius: 'var(--radius-md)',
          padding: '2.5rem 2rem',
          margin: '2rem auto',
          boxShadow: 'var(--shadow-card)',
          maxWidth: '640px'
        }}
      >
        <div style={{ display: 'inline-flex', padding: '1rem', background: 'var(--bg-subtle)', borderRadius: '50%', marginBottom: '1.5rem', color: 'var(--brand-burgundy)' }}>
          <Compass size={36} />
        </div>
        
        <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', marginBottom: '0.75rem', color: 'var(--text-primary)' }}>
          Navigate Back to Strategic Grounds
        </h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', lineHeight: '1.6', marginBottom: '2rem' }}>
          You may return to the primary briefing or proceed directly to the strategic analysis workbench.
        </p>

        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          <Link to="/" className="btn-secondary-light" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1.25rem' }}>
            <ArrowLeft size={16} />
            <span>Return to Overview</span>
          </Link>
          <Link to="/analyze" className="btn-primary-burgundy" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1.25rem' }}>
            <Search size={16} />
            <span>Open Analyzer</span>
          </Link>
        </div>

        <div style={{ marginTop: '2.5rem', paddingTop: '1.5rem', borderTop: '1px dashed var(--border-medium)', textAlign: 'left' }}>
          <span style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--text-muted)', display: 'block', marginBottom: '0.75rem' }}>
            Available Framework Routes:
          </span>
          <div style={{ display: 'flex', gap: '1.25rem', flexWrap: 'wrap', fontSize: '0.85rem' }}>
            <Link to="/patterns" style={{ color: 'var(--brand-burgundy)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
              <Layers size={13} /> Pattern Taxonomy
            </Link>
            <Link to="/research" style={{ color: 'var(--brand-burgundy)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
              <BookOpen size={13} /> Research & Literature
            </Link>
            <Link to="/model" style={{ color: 'var(--brand-burgundy)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
              <Compass size={13} /> Model Methodology
            </Link>
            <Link to="/about" style={{ color: 'var(--brand-burgundy)', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
              <span>&bull;</span> Project Overview
            </Link>
          </div>
        </div>
      </div>
    </article>
  );
}
