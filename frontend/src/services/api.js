/**
 * API Client Service for Shakuni.
 * Interacts with FastAPI backend endpoints.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

/**
 * Handle HTTP response and parse JSON or generate user-friendly error.
 */
async function handleResponse(response) {
  if (!response.ok) {
    let errorDetail = 'An unexpected server error occurred.';
    try {
      const data = await response.json();
      if (data.message) {
        errorDetail = data.message;
      } else if (data.detail) {
        errorDetail = typeof data.detail === 'string' ? data.detail : JSON.stringify(data.detail);
      }
    } catch {
      errorDetail = `Server responded with HTTP status ${response.status} (${response.statusText})`;
    }
    throw new Error(errorDetail);
  }
  return response.json();
}

/**
 * Fetch health status of the backend API.
 */
export async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: { 'Accept': 'application/json' },
    });
    return await handleResponse(res);
  } catch (err) {
    console.error('Health check failed:', err);
    throw new Error('API service is unavailable. Please verify the backend is running.');
  }
}

/**
 * Submit text for manipulation and strategic deception pattern analysis.
 */
export async function analyzeText(text) {
  if (!text || !text.trim()) {
    throw new Error('Please enter text to analyze.');
  }

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 15000); // 15s timeout

  try {
    const res = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({ text }),
      signal: controller.signal
    });
    return await handleResponse(res);
  } catch (err) {
    if (err.name === 'AbortError') {
      throw new Error('Request timed out. The server took too long to respond.');
    }
    throw err;
  } finally {
    clearTimeout(timeoutId);
  }
}

/**
 * Submit multiple texts for batch analysis.
 */
export async function batchAnalyze(texts) {
  if (!Array.isArray(texts) || texts.length === 0) {
    throw new Error('Batch list must contain at least one message.');
  }

  const res = await fetch(`${API_BASE_URL}/batch-analyze`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({ texts })
  });
  return await handleResponse(res);
}

/**
 * Fetch all 7 manipulation categories and qualitative definitions.
 */
export async function getCategories() {
  const res = await fetch(`${API_BASE_URL}/categories`, {
    method: 'GET',
    headers: { 'Accept': 'application/json' }
  });
  return await handleResponse(res);
}
