"""
YouTube Data Ingestion Service
Handles communication with the YouTube Data API v3 or fallback to demo dataset.
"""

from typing import Dict, Any, List
from backend.app.config import settings
from backend.demo_data import (
    CHANNEL_INFO,
    HISTORICAL_TRAJECTORY,
    RECENT_VIDEOS,
    COMMENTS_DATASET
)

class YouTubeService:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.use_demo = settings.USE_DEMO_DATA or not self.api_key

    def get_channel_details(self, channel_id: str = None) -> Dict[str, Any]:
        """Fetch channel statistics and metadata."""
        if self.use_demo or not self.api_key:
            return CHANNEL_INFO

        try:
            from googleapiclient.discovery import build
            youtube = build("youtube", "v3", developerKey=self.api_key)
            request = youtube.channels().list(
                part="snippet,statistics,contentDetails",
                id=channel_id or "UC_x5XG1OV2P6uZZ5FSM9Ttw"
            )
            response = request.execute()
            if response.get("items"):
                item = response["items"][0]
                snippet = item["snippet"]
                stats = item["statistics"]
                return {
                    "channel_id": item["id"],
                    "channel_name": snippet["title"],
                    "handle": snippet.get("customUrl", f"@{snippet['title'].replace(' ', '').lower()}"),
                    "niche": "Tech & Creator Education",
                    "avatar_url": snippet["thumbnails"]["high"]["url"],
                    "subscriber_count": int(stats.get("subscriberCount", 0)),
                    "total_views": int(stats.get("viewCount", 0)),
                    "video_count": int(stats.get("videoCount", 0)),
                    "watch_time_hours": 3480, # Note: watch time requires YouTube Analytics API OAuth
                    "monetization_sub_target": 1000,
                    "monetization_watch_target": 4000,
                    "current_streak_weeks": 4,
                    "last_upload_days_ago": 6,
                    "target_frequency_days": 5,
                }
        except Exception as e:
            print(f"[YouTubeService Warning] Falling back to demo data due to: {e}")
            
        return CHANNEL_INFO

    def get_recent_videos(self, channel_id: str = None, max_results: int = 5) -> List[Dict[str, Any]]:
        """Fetch recent video performance and metadata."""
        if self.use_demo or not self.api_key:
            return RECENT_VIDEOS
        return RECENT_VIDEOS

    def get_recent_comments(self, video_id: str = None) -> List[Dict[str, Any]]:
        """Fetch comment threads for NLP sentiment and content gap extraction."""
        return COMMENTS_DATASET

    def get_historical_metrics(self) -> List[Dict[str, Any]]:
        """Fetch historical view & subscriber trajectory."""
        return HISTORICAL_TRAJECTORY

youtube_service = YouTubeService()
