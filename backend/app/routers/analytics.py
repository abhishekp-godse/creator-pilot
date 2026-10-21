from fastapi import APIRouter
from typing import List
from backend.app.models.schemas import ChannelSummary, VideoPerformanceItem, NotificationAlert
from backend.app.services.youtube_service import youtube_service
from backend.app.services.ml_service import ml_service

router = APIRouter(prefix="/api/channel", tags=["Analytics & Channel"])

@router.get("/summary", response_model=ChannelSummary)
def get_channel_summary():
    """Retrieve full channel summary, monetization progress, and health score."""
    data = youtube_service.get_channel_details()
    health = ml_service.compute_growth_health_score()
    
    return ChannelSummary(
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

@router.get("/videos", response_model=List[VideoPerformanceItem])
def get_channel_videos():
    """Retrieve recent videos and their drop-off hook analysis."""
    videos = youtube_service.get_recent_videos()
    return [VideoPerformanceItem(**v) for v in videos]

@router.get("/notifications", response_model=List[NotificationAlert])
def get_proactive_notifications():
    """Retrieve proactive nudges, upload gap warnings, streak alerts, and best times."""
    summary = youtube_service.get_channel_details()
    days_since = summary["last_upload_days_ago"]
    target = summary["target_frequency_days"]

    alerts = []
    
    # 1. Upload Gap Alert
    if days_since >= target:
        alerts.append(NotificationAlert(
            id="alert_gap_1",
            type="gap",
            title="Upload Gap Alert",
            message=f"You haven't posted in {days_since} days. Your audience engagement historically drops after day 7.",
            urgency="high",
            timestamp="Just now"
        ))

    # 2. Best-Time Alert
    alerts.append(NotificationAlert(
        id="alert_time_2",
        type="best_time",
        title="Best-Time Alert",
        message="Your audience engagement peaks at 7:00 PM EST today. Scheduled uploads receive +28% more initial views.",
        urgency="medium",
        timestamp="Today, 2:30 PM"
    ))

    # 3. Streak Tracker
    alerts.append(NotificationAlert(
        id="alert_streak_3",
        type="streak",
        title="Consistency Streak at Risk",
        message=f"You are on a {summary['current_streak_weeks']}-week streak! Upload within the next 48 hours to extend your streak.",
        urgency="medium",
        timestamp="1 hour ago"
    ))

    # 4. Burnout Detector
    alerts.append(NotificationAlert(
        id="alert_burnout_4",
        type="burnout",
        title="Burnout Prevention Check",
        message="Pacing is stable. Consider recording 2 videos in batch this Friday to free up next weekend.",
        urgency="info",
        timestamp="Yesterday"
    ))

    return alerts
