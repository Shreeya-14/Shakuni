import React, { useState, useEffect } from 'react';
import Home from './pages/Home';
import Methodology from './pages/Methodology';
import Research from './pages/Research';
import { checkHealth } from './services/api';
import { Compass, BookOpen, Layers, Search, ShieldCheck } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [apiStatus, setApiStatus] = useState({ isChecking: true, isHealthy: false });

  useEffect(() => {
    async function verifyBackend() {
      try {
        const res = await checkHealth();
        if (res && res.status === 'healthy') {
          setApiStatus({ isChecking: false, isHealthy: true });
        } else {
          setApiStatus({ isChecking: false, isHealthy: false });
        }
      } catch (err) {
        setApiStatus({ isChecking: false, isHealthy: false });
      }
    }
    verifyBackend();
  }, []);

  return (
    <div className="app-container">
      {/* Luxury Editorial Header */}
      <header className="navbar">
        <div className="nav-inner">
          <button 
            type="button"
            className="brand" 
            style={{ cursor: 'pointer' }} 
            onClick={() => setActiveTab('home')}
          >
            <div className="brand-icon-box">
              <svg viewBox="0 0 32 32" width="24" height="24" fill="none">
                <polygon points="16,3 29,10 16,17 3,10" stroke="#c5a059" strokeWidth="1.5" fill="rgba(197, 160, 89, 0.08)" />
                <polygon points="3,10 16,17 16,29 3,22" stroke="#8b1e3f" strokeWidth="1.5" fill="rgba(139, 30, 63, 0.15)" />
                <polygon points="29,10 16,17 16,29 29,22" stroke="#c5a059" strokeWidth="1.5" fill="rgba(197, 160, 89, 0.04)" />
                <circle cx="16" cy="10" r="1.5" fill="#f5f2eb" />
                <circle cx="9.5" cy="19.5" r="1.2" fill="#c5a059" />
                <circle cx="22.5" cy="19.5" r="1.2" fill="#c5a059" />
              </svg>
            </div>
            <div className="brand-title-group">
              <h1>Shakuni</h1>
              <p>Strategic Manipulation Analysis</p>
            </div>
          </button>

          {/* Navigation Links */}
          <nav>
            <ul className="nav-links">
              <li>
                <button
                  type="button"
                  className={`nav-btn ${activeTab === 'home' ? 'active' : ''}`}
                  onClick={() => setActiveTab('home')}
                >
                  <Search size={13} />
                  Analyze
                </button>
              </li>
              <li>
                <button
                  type="button"
                  className={`nav-btn ${activeTab === 'methodology' ? 'active' : ''}`}
                  onClick={() => setActiveTab('methodology')}
                >
                  <Layers size={13} />
                  Methodology
                </button>
              </li>
              <li>
                <button
                  type="button"
                  className={`nav-btn ${activeTab === 'research' ? 'active' : ''}`}
                  onClick={() => setActiveTab('research')}
                >
                  <BookOpen size={13} />
                  Research
                </button>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main Editorial View */}
      <main className="main-content">
        {activeTab === 'home' && <Home />}
        {activeTab === 'methodology' && <Methodology />}
        {activeTab === 'research' && <Research />}
      </main>

      {/* Luxury Editorial Footer */}
      <footer className="editorial-footer">
        <div className="footer-dossier-inner">
          <div className="footer-col-left">
            <span className="footer-brand-mark">SHAKUNI INTELLIGENCE ARCHIVE</span>
            <p>An academic research framework for computational analysis of strategic deception & information manipulation.</p>
          </div>

          <div className="footer-col-right">
            {/* Live Engine Status */}
            <div className="footer-engine-pill">
              <span className={`engine-dot ${apiStatus.isHealthy ? '' : 'inactive'}`} />
              <span>{apiStatus.isChecking ? 'SYNCING ENGINE...' : apiStatus.isHealthy ? 'AI ENGINE ACTIVE' : 'API DISCONNECTED'}</span>
            </div>

            <ul className="footer-links-list">
              <li>
                <button 
                  type="button"
                  onClick={() => setActiveTab('methodology')}
                  className="footer-link-btn"
                >
                  Methodology
                </button>
              </li>
              <li>
                <button 
                  type="button"
                  onClick={() => setActiveTab('research')}
                  className="footer-link-btn"
                >
                  Research
                </button>
              </li>
            </ul>
          </div>
        </div>
      </footer>
    </div>
  );
}
