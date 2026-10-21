"""
CreatorPilot - Channel Controller (MVC Controller)
Orchestrates requests for channel profile, video metrics, and proactive notifications.
"""

from fastapi import APIRouter
from typing import List
from backend.app.models.channel_model import ChannelProfile, VideoMetric, NotificationAlert
from backend.app.services.youtube_service import youtube_service
from backend.app.services.ml_service import ml_service

router = APIRouter(prefix="/api/channel", tags=["Channel Controller"])

@router.get("/summary", response_model=ChannelProfile)
def get_channel_summary():
    data = youtube_service.get_channel_details()
    health = ml_service.compute_growth_health_score()
    
    return ChannelProfile(
        channel_id=data["channel_id"],
        channel_name=data["channel_name"],
        handle=data["handle"],
        niche=data["niche"],
        avatar_url=data["avatar_url"],
        subscriber_count=data["subscriber_count"],
        total_views=data["total_views"],
        video_count=data["video_count"],
        watch_time_hours=data["watch_time_hours"],
        monetization_sub_target=data["monetization_sub_target"],
        monetization_watch_target=data["monetization_watch_target"],
        growth_health_score=health["overall_score"],
        health_breakdown=health["breakdown"],
        current_streak_weeks=data["current_streak_weeks"],
        last_upload_days_ago=data["last_upload_days_ago"],
        target_frequency_days=data["target_frequency_days"]
    )

@router.get("/videos", response_model=List[VideoMetric])
def get_channel_videos():
    videos = youtube_service.get_recent_videos()
    return [VideoMetric(**v) for v in videos]

@router.get("/notifications", response_model=List[NotificationAlert])
def get_notifications():
    summary = youtube_service.get_channel_details()
    days_since = summary["last_upload_days_ago"]
    target = summary["target_frequency_days"]

    alerts = []
    if days_since >= target:
        alerts.append(NotificationAlert(
            id="alert_gap_1",
            type="gap",
            title="Upload Gap Alert",
            message=f"You haven't posted in {days_since} days. Your audience engagement historically drops after day 7.",
            urgency="high",
            timestamp="Just now"
        ))

    alerts.append(NotificationAlert(
        id="alert_time_2",
        type="best_time",
        title="Best-Time Alert",
        message="Your audience engagement peaks at 7:00 PM EST today. Scheduled uploads receive +28% more initial views.",
        urgency="medium",
        timestamp="Today, 2:30 PM"
    ))

    alerts.append(NotificationAlert(
        id="alert_streak_3",
        type="streak",
        title="Consistency Streak at Risk",
        message=f"You are on a {summary['current_streak_weeks']}-week streak! Upload within 48 hours to preserve your multiplier.",
        urgency="medium",
        timestamp="1 hour ago"
    ))

    alerts.append(NotificationAlert(
        id="alert_burnout_4",
        type="burnout",
        title="Burnout Prevention Check",
        message="Pacing is optimal. Batch record 2 videos this Friday to free up next weekend for rest.",
        urgency="info",
        timestamp="Yesterday"
    ))

    return alerts
