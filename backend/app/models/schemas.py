from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ChannelSummary(BaseModel):
    channel_id: str
    channel_name: str
    handle: str
    niche: str
    avatar_url: str
    subscriber_count: int
    total_views: int
    video_count: int
    watch_time_hours: float
    monetization_sub_target: int
    monetization_watch_target: int
    growth_health_score: int
    health_breakdown: Dict[str, int]
    current_streak_weeks: int
    last_upload_days_ago: int
    target_frequency_days: int

class NotificationAlert(BaseModel):
    id: str
    type: str # 'gap', 'best_time', 'streak', 'burnout'
    title: str
    message: str
    urgency: str # 'high', 'medium', 'info'
    timestamp: str

class VideoPerformanceItem(BaseModel):
    video_id: str
    title: str
    published_at: str
    views: int
    likes: int
    comments_count: int
    retention_hook_drop: float
    drop_reason: str
    sentiment_score: float
    thumbnail_url: str

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
    grade: str # A, B, C, D
    strengths: List[str]
    improvements: List[str]
    suggested_variations: List[str]

class ContentGapItem(BaseModel):
    topic: str
    sample_comment: str
    request_count: int
    urgency: str
    suggested_title: str

class TrendTopicItem(BaseModel):
    topic: str
    category: str
    fit_score: int
    search_volume_velocity: str
    expires_in_days: int
    urgency: str
    recommended_hook: str

class ChatMessage(BaseModel):
    role: str # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    reply: str
    action_nudges: List[str] = []
    audio_text: Optional[str] = None

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
