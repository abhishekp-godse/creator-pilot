"""
CreatorPilot - FastAPI Backend Gateway
Configures CORS, middleware, and registers all MVC Controllers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.controllers import (
    channel_controller,
    ml_controller,
    growth_controller,
    coach_controller,
    auth_controller
)
from backend.app.routers import trends

app = FastAPI(
    title="CreatorPilot API",
    description="Proactive AI Growth Coach & Decision Engine for Content Creators (MVC Architecture)",
    version="2.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register MVC Controllers
app.include_router(auth_controller.router)
app.include_router(channel_controller.router)
app.include_router(ml_controller.router)
app.include_router(growth_controller.router)
app.include_router(coach_controller.router)
app.include_router(trends.router)

@app.get("/")
def root():
    return {
        "service": "CreatorPilot Backend API",
        "architecture": "Model-View-Controller (MVC)",
        "status": "operational",
        "docs": "/docs",
        "endpoints": [
            "/api/channel/summary",
            "/api/ml/growth-forecast",
            "/api/ml/score-title",
            "/api/growth/content-gaps",
            "/api/growth/idea-vault",
            "/api/growth/collab-matcher",
            "/api/growth/monetization-sprint",
            "/api/coach/chat"
        ]
    }

@app.get("/api/health")
def health():
    return {"status": "healthy", "engine": "CreatorPilot v2.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
