"""
CreatorPilot - ML & Predictive Analytics Controller
Handles Time-Series Growth Forecasting, Title Click Scoring & Drop-off Diagnostics.
"""

from fastapi import APIRouter
from typing import List
from backend.app.models.prediction_model import (
    GrowthForecastResponse,
    TitleScoreRequest,
    TitleScoreResponse,
    DropoffHookDiagnostic
)
from backend.app.services.ml_service import ml_service
from backend.app.services.youtube_service import youtube_service

router = APIRouter(prefix="/api/ml", tags=["ML Predictive Controller"])

@router.get("/growth-forecast", response_model=GrowthForecastResponse)
def get_growth_forecast(days: int = 30):
    forecast = ml_service.forecast_growth(days_ahead=days)
    return GrowthForecastResponse(**forecast)

@router.post("/score-title", response_model=TitleScoreResponse)
def score_title(payload: TitleScoreRequest):
    result = ml_service.score_title(payload.title)
    
    # Calculate clickbait risk
    clickbait_words = ["insane", "you won't believe", "shocking", "free money", "instant"]
    has_clickbait = any(w in payload.title.lower() for w in clickbait_words)
    clickbait_risk = "High" if has_clickbait else "Medium" if "stop" in payload.title.lower() else "Low"

    return TitleScoreResponse(
        title=result["title"],
        score=result["score"],
        grade=result["grade"],
        clickbait_risk=clickbait_risk,
        strengths=result["strengths"],
        improvements=result["improvements"],
        suggested_variations=result["suggested_variations"]
    )

@router.get("/hook-diagnostics", response_model=List[DropoffHookDiagnostic])
def get_hook_diagnostics():
    videos = youtube_service.get_recent_videos()
    diagnostics = []
    for v in videos:
        retention = round((1 - v["retention_hook_drop"]) * 100, 1)
        diagnostics.append(DropoffHookDiagnostic(
            video_id=v["video_id"],
            video_title=v["title"],
            hook_retention_pct=retention,
            industry_benchmark_pct=65.0,
            diagnosis=v["drop_reason"],
            actionable_fix="Show working code/demo in the first 8 seconds before explaining." if retention < 65 else "Hook pacing was effective."
        ))
    return diagnostics
