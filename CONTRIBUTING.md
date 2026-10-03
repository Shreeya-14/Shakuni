# Contributing to Shakuni

Thank you for your interest in contributing to Shakuni! This project is an open research and educational framework for strategic deception and information manipulation pattern analysis.

## Core Code of Conduct & Research Integrity

1. **No Absolute Deception Claims**: All PRs, features, and documentation must adhere to our principle that the system classifies **probabilistic linguistic communication patterns**, NOT objective truth or personal dishonesty.
2. **Real Metrics Only**: Do not submit fabricated evaluation numbers or falsified datasets. All benchmark numbers must be reproducible via `python -m evaluation.evaluate`.
3. **Transparent Sources**: Clearly document the origin of dataset samples (e.g., synthetic research curation, academic corpora).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Shakuni.git
   cd Shakuni
   ```

2. Set up the Python backend environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r backend/requirements.txt
   pip install pytest httpx
   ```

3. Set up the Frontend environment:
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. Train the baseline model:
   ```bash
   python -m ai_engine.training.train_model
   ```

5. Run test suite:
   ```bash
   python -m pytest tests/ -v
   ```

## Development Guidelines

- **Clean Architecture**: Backend uses FastAPI with Pydantic validation. The AI engine is decoupled from the web layer.
- **Centralized Categories**: Any category-level changes must occur in `ai_engine/classifier/categories.py`.
- **Typing and Linting**: Use standard Python type hints for clarity.
- **Frontend Conventions**: Functional React components with hooks, clear CSS structure, and responsive mobile-first views.
