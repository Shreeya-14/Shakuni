import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { analyzeText } from '../services/api';
import EmptyWorkspace from '../components/EmptyWorkspace';
import LoadingState from '../components/LoadingState';
import ResultCard from '../components/ResultCard';
import AnalysisHistory from '../components/AnalysisHistory';
import { 
  Send, 
  RotateCcw, 
  AlertTriangle, 
  FileText, 
  Sparkles,
  ChevronRight,
  History,
  Cpu,
  Key,
  Settings,
  ChevronDown,
  ChevronUp
} from 'lucide-react';

const CURATED_SAMPLES = [
  {
    code: '01',
    label: 'Social Pressure',
    text: "Everyone on the executive team has already signed the loyalty agreement; don't be the lone dissenter holding us back."
  },
  {
    code: '02',
    label: 'Emotional Pressure',
    text: "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer."
  },
  {
    code: '03',
    label: 'Misleading Framing',
    text: "You are either completely with our bold organizational turnaround strategy, or you actively want the company to fail."
  },
  {
    code: '04',
    label: 'Selective Info',
    text: "Our revolutionary battery technology demonstrated a four hundred percent charge retention in controlled lab tests."
  },
  {
    code: '05',
    label: 'Withholding',
    text: "The platform upgrade will go live at midnight as agreed. We will address any pending secondary configuration items during later maintenance cycles."
  },
  {
    code: '06',
    label: 'Deceptive Persuasion',
    text: "I just spoke directly with the CEO, and she authorized us to bypass standard compliance reviews for this wire transfer."
  },
  {
    code: '07',
    label: 'Normal Baseline',
    text: "The scheduled software release has been postponed to Tuesday to complete standard regression testing."
  }
];

const STORAGE_KEY = 'shakuni_analysis_history';
const ENGINE_STORAGE_KEY = 'shakuni_selected_engine';
const API_KEY_STORAGE_KEY = 'shakuni_llm_api_key';

export default function Analyze() {
  const [inputText, setInputText] = useState('');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(true);

  // AI Model Engine & LLM Settings
  const [selectedEngine, setSelectedEngine] = useState(() => {
    return localStorage.getItem(ENGINE_STORAGE_KEY) || 'hybrid';
  });
  const [apiKey, setApiKey] = useState(() => {
    return localStorage.getItem(API_KEY_STORAGE_KEY) || '';
  });
  const [showEngineConfig, setShowEngineConfig] = useState(false);

  const location = useLocation();

  // Load history from localStorage on initial render
  useEffect(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        setHistory(JSON.parse(stored));
      }
    } catch (e) {
      console.warn('Unable to access localStorage history:', e);
    }
  }, []);

  // Pre-populate input from URL query string if present (?sample=...)
  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const sampleParam = params.get('sample');
    if (sampleParam) {
      setInputText(sampleParam);
      // Automatically scroll to input
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [location.search]);

  // Persist new entry to history
  const saveToHistory = (itemResult, originalText) => {
    try {
      const historyItem = {
        id: Date.now().toString(),
        text: originalText,
        category: itemResult.category,
        risk_score: itemResult.risk_score,
        risk_level: itemResult.risk_level,
        confidence: itemResult.confidence,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        fullResult: itemResult
      };

      const updated = [historyItem, ...history.filter(h => h.text !== originalText)].slice(0, 8);
      setHistory(updated);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
    } catch (e) {
      console.warn('Failed to persist history item:', e);
    }
  };

  const handleClearHistory = () => {
    try {
      localStorage.removeItem(STORAGE_KEY);
      setHistory([]);
    } catch (e) {
      console.warn('Failed to clear history:', e);
    }
  };

  const handleSelectHistoryItem = (item) => {
    setInputText(item.text);
    setAnalysisResult(item.fullResult || item);
    setError(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleAnalyze = async (textToAnalyze) => {
    const text = textToAnalyze || inputText;
    if (!text.trim() || isLoading) return;

    setIsLoading(true);
    setError(null);

    try {
      const data = await analyzeText(text.trim(), {
        engine: selectedEngine,
        apiKey: apiKey ? apiKey.trim() : undefined
      });
      setAnalysisResult(data);
      saveToHistory(data, text.trim());
    } catch (err) {
      console.error('Analysis error:', err);
      setError(err.message || 'Failed to analyze text. Please verify backend service connectivity.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleAnalyze();
  };

  const handleSelectSample = (sampleText) => {
    setInputText(sampleText);
    setError(null);
  };

  const handleReset = () => {
    setInputText('');
    setAnalysisResult(null);
    setError(null);
  };

  const charCount = inputText.length;
  const isOverLimit = charCount > 10000;

  return (
    <div className="analyze-page-container">
      {/* Workspace Header */}
      <header className="workspace-page-header">
        <div className="workspace-page-title-cluster">
          <span className="workspace-eyebrow">INTELLIGENCE WORKSPACE</span>
          <h1 className="workspace-page-heading">Communication Pattern Analyzer</h1>
          <p className="workspace-page-lead">
            Evaluate statements, announcements, dialogues, or proposals against Shakuni's seven-category rhetorical manipulation taxonomy and deep linguistic style reasoning.
          </p>
        </div>
      </header>

      {/* Main Two-Panel Workspace Grid */}
      <div className="analyze-workspace-grid">
        {/* Left Column: Input Panel & Curated Samples */}
        <div className="workspace-left-panel">
          <div className="analyzer-workspace-card">
            <form onSubmit={handleSubmit}>
              {/* Card Header Strip */}
              <div className="workspace-header">
                <div className="workspace-label">
                  <FileText size={14} color="var(--brand-burgundy)" />
                  <span>CASE FILE // INPUT TEXT SAMPLE</span>
                </div>
                <div 
                  className="workspace-counter" 
                  style={{ color: isOverLimit ? '#8c1e34' : 'var(--text-muted)' }}
                >
                  {charCount.toLocaleString()} / 10,000 CHARACTERS
                </div>
              </div>

              {/* AI Reasoning Engine Selector Bar */}
              <div style={{
                background: 'var(--bg-warm-tint)',
                padding: '0.65rem 1rem',
                borderBottom: '1px solid var(--border-light)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: '0.65rem'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap' }}>
                  <Cpu size={14} color="var(--brand-burgundy)" />
                  <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.72rem', fontWeight: 700, color: 'var(--text-secondary)' }}>
                    REASONING ENGINE:
                  </span>
                  <select
                    value={selectedEngine}
                    onChange={(e) => {
                      const val = e.target.value;
                      setSelectedEngine(val);
                      localStorage.setItem(ENGINE_STORAGE_KEY, val);
                    }}
                    style={{
                      fontFamily: 'var(--font-mono)',
                      fontSize: '0.74rem',
                      padding: '0.2rem 0.5rem',
                      background: '#ffffff',
                      border: '1px solid var(--border-medium)',
                      borderRadius: '3px',
                      color: 'var(--text-primary)',
                      cursor: 'pointer'
                    }}
                  >
                    <option value="hybrid">⚡ Shakuni Hybrid (DistilBERT + Neural Discourse Reasoner)</option>
                    <option value="gemini">✨ Google Gemini 2.0 Flash (Cloud LLM)</option>
                    <option value="openai">🤖 ChatGPT / OpenAI GPT-4o-mini (Cloud LLM)</option>
                    <option value="groq">⚡ Groq LLaMA 3.3 70B (Cloud LLM)</option>
                    <option value="ollama">💻 Local Ollama (llama3)</option>
                  </select>
                </div>

                <button
                  type="button"
                  onClick={() => setShowEngineConfig(!showEngineConfig)}
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border-medium)',
                    borderRadius: '3px',
                    padding: '0.2rem 0.6rem',
                    fontSize: '0.7rem',
                    fontFamily: 'var(--font-mono)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.35rem',
                    cursor: 'pointer',
                    color: 'var(--brand-burgundy)'
                  }}
                >
                  <Key size={12} />
                  <span>{apiKey ? 'API Key Configured' : 'Configure API Key'}</span>
                  {showEngineConfig ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
                </button>
              </div>

              {/* Collapsible API Key Drawer */}
              {showEngineConfig && (
                <div style={{
                  background: '#fdfcf7',
                  borderBottom: '1px solid var(--border-medium)',
                  padding: '0.85rem 1rem',
                  fontSize: '0.78rem'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem', marginBottom: '0.4rem' }}>
                    <input
                      type="password"
                      value={apiKey}
                      onChange={(e) => {
                        const val = e.target.value;
                        setApiKey(val);
                        localStorage.setItem(API_KEY_STORAGE_KEY, val);
                      }}
                      placeholder={`Enter your ${selectedEngine === 'gemini' ? 'Gemini' : selectedEngine === 'openai' ? 'OpenAI' : selectedEngine === 'groq' ? 'Groq' : 'LLM'} API Key...`}
                      style={{
                        flex: 1,
                        padding: '0.35rem 0.65rem',
                        fontFamily: 'var(--font-mono)',
                        fontSize: '0.75rem',
                        border: '1px solid var(--border-medium)',
                        borderRadius: '3px',
                        background: '#ffffff'
                      }}
                    />
                    {apiKey && (
                      <button
                        type="button"
                        onClick={() => {
                          setApiKey('');
                          localStorage.removeItem(API_KEY_STORAGE_KEY);
                        }}
                        style={{
                          background: '#f5f4ef',
                          border: '1px solid var(--border-medium)',
                          padding: '0.35rem 0.65rem',
                          fontSize: '0.7rem',
                          fontFamily: 'var(--font-mono)',
                          borderRadius: '3px',
                          cursor: 'pointer'
                        }}
                      >
                        Clear Key
                      </button>
                    )}
                  </div>
                  <div style={{ color: 'var(--text-muted)', fontSize: '0.72rem', lineHeight: 1.4 }}>
                    🔒 API keys are stored only locally in your browser. If left empty, Shakuni uses its built-in neural linguistic discourse reasoner with 0 API keys required.
                  </div>
                </div>
              )}

              {/* Textarea Area */}
              <div className="textarea-container">
                <textarea
                  id="message-input"
                  className="editorial-textarea"
                  value={inputText}
                  onChange={(e) => setInputText(e.target.value)}
                  placeholder="Paste a message, advertisement, post, dialogue, or statement to analyze..."
                  rows={7}
                  disabled={isLoading}
                  aria-label="Text to analyze for manipulation patterns"
                />
              </div>

              {/* Curated Research Sample Shortcuts */}
              <div className="example-cases-bar">
                <span className="example-cases-title">Curated Research Case Samples:</span>
                <div className="example-cases-grid">
                  {CURATED_SAMPLES.map((sample) => (
                    <button
                      key={sample.code}
                      type="button"
                      className="example-case-btn"
                      onClick={() => handleSelectSample(sample.text)}
                      disabled={isLoading}
                    >
                      <span className="num">{sample.code}</span>
                      {sample.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Error Banner */}
              {error && (
                <div className="error-editorial-banner" role="alert">
                  <AlertTriangle size={16} style={{ flexShrink: 0 }} />
                  <span>{error}</span>
                </div>
              )}

              {/* Action Buttons Footer */}
              <div className="workspace-footer">
                <div className="workspace-disclaimer">
                  Analyzes lexical n-grams and syntactic framing indicators. Predictions are probabilistic.
                </div>

                <div className="workspace-actions">
                  {inputText && (
                    <button
                      type="button"
                      className="btn-secondary-light"
                      onClick={handleReset}
                      disabled={isLoading}
                    >
                      <RotateCcw size={13} />
                      <span>Clear</span>
                    </button>
                  )}

                  <button
                    type="submit"
                    className="btn-primary-burgundy"
                    disabled={!inputText.trim() || isLoading || isOverLimit}
                  >
                    <Send size={14} />
                    <span>{isLoading ? 'Analyzing...' : 'Analyze Message'}</span>
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Local Analysis History Accordion */}
          <div className="history-section-wrapper">
            <AnalysisHistory 
              history={history} 
              onSelect={handleSelectHistoryItem} 
              onClear={handleClearHistory} 
            />
          </div>
        </div>

        {/* Right Column: Dynamic Analysis Result or Empty State */}
        <div className="workspace-right-panel">
          {isLoading && <LoadingState />}

          {!isLoading && !analysisResult && <EmptyWorkspace />}

          {!isLoading && analysisResult && (
            <div>
              <div className="result-action-bar">
                <span className="result-status-text">
                  Analysis completed in real-time via FastAPI ML pipeline.
                </span>
                <button 
                  type="button" 
                  className="btn-secondary-light"
                  onClick={() => {
                    setAnalysisResult(null);
                    setInputText('');
                  }}
                >
                  <RotateCcw size={13} />
                  <span>New Analysis</span>
                </button>
              </div>

              <ResultCard result={analysisResult} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
