from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from .database import init_db
from .routers import issues, auth
from .services.escalation_engine import run_escalation_check

# Initialize Scheduler
scheduler = BackgroundScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    
    # Start Scheduler (Run every 1 minute for demo purposes, 5-15m in prod)
    scheduler.add_job(run_escalation_check, 'interval', minutes=1)
    scheduler.start()
    print("Scheduler started...")
    
    yield
    
    # Shutdown
    scheduler.shutdown()
    print("Scheduler shutdown...")

app = FastAPI(title="Risk-Aware Civic Issue System", lifespan=lifespan)

app.include_router(issues.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Civic Issue System API is running"}
