# Backend Setup

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Environment Variables
Create a `.env` file (copied from `.env.example` if exists) or just ensure `DATABASE_URL` is set.
By default it assumes a local postgres DB.

## 3. Run Server
```bash
uvicorn app.main:app --reload
```

## Features
- **FastAPI** for core API.
- **SQLModel** (SQLAlchemy) for ORM.
- **APScheduler** runs `run_escalation_check` every 1 minute to upgrade risk levels.
- **Sequential Escalation**: Low -> Medium (24h) -> High (12h) -> Critical (6h).
