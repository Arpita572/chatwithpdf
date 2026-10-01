from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title="ChatWithPDF API",
    description="RAG-based knowledge base API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "ChatWithPDF API is running"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env,
    }