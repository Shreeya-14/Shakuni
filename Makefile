.PHONY: help install train evaluate test run-backend run-frontend docker-up docker-down clean

help:
	@echo "Shakuni Project Make Commands:"
	@echo "  make install        Install backend and frontend dependencies"
	@echo "  make train          Train the ML model from dataset"
	@echo "  make evaluate       Run evaluation and generate metrics report"
	@echo "  make test           Run unit and integration tests"
	@echo "  make run-backend    Start the FastAPI backend server"
	@echo "  make run-frontend   Start the Vite React frontend server"
	@echo "  make docker-up      Start full stack with Docker Compose"
	@echo "  make docker-down    Stop Docker Compose containers"
	@echo "  make clean          Clean temporary files and caches"

install:
	python -m pip install -r backend/requirements.txt
	cd frontend && npm install

train:
	python -m ai_engine.training.train_model

evaluate:
	python -m evaluation.evaluate

test:
	python -m pytest tests/ -v

run-backend:
	uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

run-frontend:
	cd frontend && npm run dev

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
