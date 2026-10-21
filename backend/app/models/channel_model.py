"""
CreatorPilot - Model Layer (Domain Entities & Data Schemas)
Defines the core data structures for Channel Telemetry, Videos, Comments, and Health Metrics.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class VideoMetric(BaseModel):
    video_id: str
    title: str
    published_at: str
    views: int
    likes: int
    comments_count: int
    retention_hook_drop: float # e.g. 0.42 = 42% left in 30s
    drop_reason: str
    sentiment_score: float # -1.0 to 1.0
    thumbnail_url: str

class ChannelSnapshot(BaseModel):
    date: str
    subscribers: int
    views: int
    daily_subs: int
    daily_views: int

class ChannelProfile(BaseModel):
    channel_id: str
    channel_name: str
    handle: str
    niche: str
    avatar_url: str
    subscriber_count: int
    total_views: int
    video_count: int
    watch_time_hours: float
    monetization_sub_target: int = 1000
    monetization_watch_target: int = 4000
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
