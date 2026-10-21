"""
CreatorPilot - Main FastAPI Backend Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.routers import analytics, ml, trends, gaps, coach

app = FastAPI(
    title="CreatorPilot API",
    description="Proactive AI Growth Coach & Analytics Engine for Content Creators",
    version="1.0.0"
)

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In development allow all; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(analytics.router)
app.include_router(ml.router)
app.include_router(trends.router)
app.include_router(gaps.router)
app.include_router(coach.router)

@app.get("/")
def root():
    return {
        "app": "CreatorPilot API",
        "status": "online",
        "demo_mode": settings.USE_DEMO_DATA,
        "docs_url": "/docs"
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "CreatorPilot Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
