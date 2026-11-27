
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from src.Data.database import get_db

app = FastAPI(
    title="Gawab API",
    description="Backend API for Gawab Donation Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Gawab API",
        "status": "Running"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as error:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }
