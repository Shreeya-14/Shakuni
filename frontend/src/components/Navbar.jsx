import React, { useState, useEffect } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { checkHealth } from '../services/api';
import { Search, Layers, BookOpen, Cpu, Info, Menu, X, ShieldAlert } from 'lucide-react';

export default function Navbar() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [apiStatus, setApiStatus] = useState({ isChecking: true, isHealthy: false });

  useEffect(() => {
    let isMounted = true;
    async function verifyBackend() {
      try {
        const res = await checkHealth();
        if (isMounted) {
          if (res && res.status === 'healthy') {
            setApiStatus({ isChecking: false, isHealthy: true });
          } else {
            setApiStatus({ isChecking: false, isHealthy: false });
          }
        }
      } catch (err) {
        if (isMounted) {
          setApiStatus({ isChecking: false, isHealthy: false });
        }
      }
    }
    verifyBackend();
    return () => {
      isMounted = false;
    };
  }, []);

  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false);
  };

  return (
    <header className="navbar" role="banner">
      <div className="nav-inner">
        {/* Brand Wordmark & Icon */}
        <Link to="/" className="brand-button" onClick={closeMobileMenu} aria-label="Shakuni Home">
          <div className="brand-icon-box">
            <svg viewBox="0 0 32 32" width="22" height="22" fill="none">
              <polygon points="16,3 29,10 16,17 3,10" stroke="#b89047" strokeWidth="1.4" fill="#fdfaf3" />
              <polygon points="3,10 16,17 16,29 3,22" stroke="#7a1c30" strokeWidth="1.4" fill="#f9edf0" />
              <polygon points="29,10 16,17 16,29 29,22" stroke="#b89047" strokeWidth="1.4" fill="#fbf7ee" />
              <circle cx="16" cy="10" r="1.3" fill="#7a1c30" />
              <circle cx="9.5" cy="19.5" r="1.1" fill="#b89047" />
              <circle cx="22.5" cy="19.5" r="1.1" fill="#b89047" />
            </svg>
          </div>
          <div className="brand-title-group">
            <h1>Shakuni</h1>
            <p>Strategic Communication Intelligence</p>
          </div>
        </Link>

        {/* Desktop Navigation Links */}
        <nav className="desktop-nav" aria-label="Main Navigation">
          <ul className="nav-links">
            <li>
              <NavLink 
                to="/analyze" 
                className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}
              >
                <Search size={13} />
                <span>Analyze</span>
              </NavLink>
            </li>
            <li>
              <NavLink 
                to="/patterns" 
                className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}
              >
                <Layers size={13} />
                <span>Patterns</span>
              </NavLink>
            </li>
            <li>
              <NavLink 
                to="/research" 
                className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}
              >
                <BookOpen size={13} />
                <span>Research</span>
              </NavLink>
            </li>
            <li>
              <NavLink 
                to="/model" 
                className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}
              >
                <Cpu size={13} />
                <span>Model</span>
              </NavLink>
            </li>
            <li>
              <NavLink 
                to="/about" 
                className={({ isActive }) => `nav-btn ${isActive ? 'active' : ''}`}
              >
                <Info size={13} />
                <span>About</span>
              </NavLink>
            </li>
          </ul>
        </nav>

        {/* Right Section: System Status Pill & Mobile Toggle */}
        <div className="nav-right-cluster">
          <div 
            className="nav-status-pill" 
            title={apiStatus.isHealthy ? 'FastAPI model backend is connected and ready.' : 'API connection not detected.'}
          >
            <span className={`status-dot ${apiStatus.isHealthy ? '' : 'inactive'}`} />
            <span>
              {apiStatus.isChecking ? 'Connecting...' : apiStatus.isHealthy ? 'AI Engine Ready' : 'System Offline'}
            </span>
          </div>

          <button 
            type="button" 
            className="mobile-nav-toggle"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label={isMobileMenuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={isMobileMenuOpen}
          >
            {isMobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {isMobileMenuOpen && (
        <div className="mobile-drawer-overlay" onClick={closeMobileMenu}>
          <div className="mobile-drawer-panel" onClick={(e) => e.stopPropagation()}>
            <div className="mobile-drawer-header">
              <span className="mobile-drawer-title">Navigation Index</span>
              <button 
                type="button" 
                className="btn-icon-subtle" 
                onClick={closeMobileMenu}
                aria-label="Close menu"
              >
                <X size={18} />
              </button>
            </div>
            <ul className="mobile-drawer-links">
              <li>
                <NavLink to="/" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  Overview (Home)
                </NavLink>
              </li>
              <li>
                <NavLink to="/analyze" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  <Search size={14} /> Analyze Workspace
                </NavLink>
              </li>
              <li>
                <NavLink to="/patterns" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  <Layers size={14} /> 07 Manipulation Patterns
                </NavLink>
              </li>
              <li>
                <NavLink to="/research" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  <BookOpen size={14} /> Research Foundations
                </NavLink>
              </li>
              <li>
                <NavLink to="/model" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  <Cpu size={14} /> Model & Evaluation
                </NavLink>
              </li>
              <li>
                <NavLink to="/about" onClick={closeMobileMenu} className={({ isActive }) => `mobile-link ${isActive ? 'active' : ''}`}>
                  <Info size={14} /> About Platform
                </NavLink>
              </li>
            </ul>
            <div className="mobile-drawer-footer">
              <div className="nav-status-pill" style={{ display: 'inline-flex' }}>
                <span className={`status-dot ${apiStatus.isHealthy ? '' : 'inactive'}`} />
                <span>{apiStatus.isHealthy ? 'AI Engine Ready' : 'System Offline'}</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
