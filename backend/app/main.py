from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler

from .database import init_db
from .routers import issues, auth
from .services.escalation_engine import run_escalation_check

# Initialize scheduler (single instance)
scheduler = BackgroundScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- STARTUP ----------
    print("Starting application...")

    # Initialize database
    init_db()
    print("Database initialized.")

    # Start scheduler only if not already running
    if not scheduler.running:
        scheduler.add_job(
            run_escalation_check,
            trigger="interval",
            minutes=1,  # Demo: 1 min | Production: 5–15 mins
            id="risk_escalation_job",
            replace_existing=True,
        )
        scheduler.start()
        print("Scheduler started.")

    yield

    # ---------- SHUTDOWN ----------
    print("Shutting down application...")

    if scheduler.running:
        scheduler.shutdown(wait=False)
        print("Scheduler stopped.")


app = FastAPI(
    title="Risk-Aware Civic Issue Management System",
    lifespan=lifespan,
)

# Routers
app.include_router(auth.router)
app.include_router(issues.router)


@app.get("/")
def root():
    return {"message": "Civic Issue System API is running"}
