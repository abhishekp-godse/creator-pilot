from fastapi import APIRouter
from backend.app.models.schemas import GrowthForecastResponse, TitleScoreRequest, TitleScoreResponse
from backend.app.services.ml_service import ml_service

router = APIRouter(prefix="/api/ml", tags=["Machine Learning Predictions"])

@router.get("/growth-forecast", response_model=GrowthForecastResponse)
def get_growth_forecast(days: int = 30):
    """Generates 30-day subscriber and view trajectory with confidence intervals."""
    forecast = ml_service.forecast_growth(days_ahead=days)
    return GrowthForecastResponse(**forecast)

@router.post("/score-title", response_model=TitleScoreResponse)
def score_proposed_title(payload: TitleScoreRequest):
    """Evaluates click potential, emotional hooks, and provides title variations."""
    result = ml_service.score_title(payload.title)
    return TitleScoreResponse(**result)
