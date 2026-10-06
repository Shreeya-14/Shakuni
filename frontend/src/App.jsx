import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// Pages
import Home from './pages/Home';
import Analyze from './pages/Analyze';
import Patterns from './pages/Patterns';
import Research from './pages/Research';
import Model from './pages/Model';
import About from './pages/About';
import NotFound from './pages/NotFound';

/**
 * ScrollToTop helper to reset window scroll position on route change.
 */
function ScrollToTop() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [pathname]);

  return null;
}

function AppContent() {
  return (
    <div className="app-container">
      <ScrollToTop />
      <Navbar />

      <main id="main-content" className="main-content" role="main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/analyze" element={<Analyze />} />
          <Route path="/patterns" element={<Patterns />} />
          <Route path="/research" element={<Research />} />
          <Route path="/model" element={<Model />} />
          <Route path="/methodology" element={<Navigate to="/model" replace />} />
          <Route path="/about" element={<About />} />
          {/* Dedicated 404 route */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>

      <Footer />
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  );
}
