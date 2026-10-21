from fastapi import APIRouter
from typing import List
from backend.app.models.schemas import TrendTopicItem
from backend.demo_data import TRENDING_TOPICS

router = APIRouter(prefix="/api/trends", tags=["Trend Intelligence"])

@router.get("/niche", response_model=List[TrendTopicItem])
def get_niche_trends():
    """Retrieve trending topics matching creator niche, fit score, and expiration countdown."""
    return [TrendTopicItem(**t) for t in TRENDING_TOPICS]
