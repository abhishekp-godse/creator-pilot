"""
CreatorPilot - Prediction & ML Domain Models
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ForecastPoint(BaseModel):
    date: str
    predicted_subs: int
    lower_bound: int
    upper_bound: int
    predicted_views: int

class GrowthForecastResponse(BaseModel):
    current_subs: int
    forecast_30d_subs: int
    predicted_sub_gain: int
    growth_rate_pct: float
    daily_points: List[ForecastPoint]
    model_used: str

class TitleScoreRequest(BaseModel):
    title: str

class TitleScoreResponse(BaseModel):
    title: str
    score: int # 0-100
    grade: str # A+, A, B, C, D
    clickbait_risk: str # Low, Medium, High
    strengths: List[str]
    improvements: List[str]
    suggested_variations: List[str]

class DropoffHookDiagnostic(BaseModel):
    video_id: str
    video_title: str
    hook_retention_pct: float
    industry_benchmark_pct: float
    diagnosis: str
    actionable_fix: str
