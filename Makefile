.PHONY: install run test lint docker-up docker-down seed clean

install:
	pip install -r requirements.txt
	cd frontend && npm install

run:
	uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

run-frontend:
	cd frontend && npm start

test:
	pytest tests/ -v

lint:
	flake8 backend/ --max-line-length=120

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

seed:
	python scripts/seed_data.py

init-db:
	python scripts/init_db.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
