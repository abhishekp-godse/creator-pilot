"""
CreatorPilot - Advanced Growth Domain Models:
Idea Vault, Collab Matcher, Content Gaps & Monetization Sprint.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class ContentGapItem(BaseModel):
    topic: str
    sample_comment: str
    request_count: int
    urgency: str
    suggested_title: str

class IdeaVaultItem(BaseModel):
    id: str
    title: str
    source: str # 'content_gap', 'trend', 'user'
    predicted_score: int # 0-100
    production_effort: str # 'Low (1-2h)', 'Medium (3-5h)', 'High (Deep Dive)'
    tags: List[str]
    status: str # 'vault', 'planned', 'published'

class CollabCreator(BaseModel):
    channel_name: str
    handle: str
    subscriber_count: int
    niche_overlap_pct: int
    common_topics: List[str]
    collab_video_concept: str
    reach_potential: str

class DayPlan(BaseModel):
    day: str
    task_type: str # 'scripting', 'recording', 'editing', 'publishing', 'community'
    task_description: str
    recommended_time: Optional[str] = None
    suggested_tags: List[str] = []

class WeeklyGrowthPlanResponse(BaseModel):
    week_focus: str
    target_kpi: str
    daily_plan: List[DayPlan]
    projected_reach: str

class MonetizationSprint(BaseModel):
    current_watch_hours: float
    target_watch_hours: float = 4000
    remaining_hours: float
    estimated_days_to_reach: int
    recommended_actions: List[str]
