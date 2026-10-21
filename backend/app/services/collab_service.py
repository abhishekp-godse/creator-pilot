"""
CreatorPilot - Collaboration Matcher Service
Discovers peer creators in identical niches with similar audience size for cross-promotion.
"""

from typing import List
from backend.app.models.growth_model import CollabCreator

class CollabMatcherService:
    def __init__(self):
        self._collab_database = [
            {
                "channel_name": "Pythonic Dev",
                "handle": "@pythonicdev",
                "subscriber_count": 31200,
                "niche_overlap_pct": 92,
                "common_topics": ["FastAPI", "Async Python", "Backend Engineering"],
                "collab_video_concept": "Building a Real-time Auction System: FastAPI Backend vs Node.js",
                "reach_potential": "+1,200 New Subscribers (Estimated 22k Shared Views)"
            },
            {
                "channel_name": "DevSimplified AI",
                "handle": "@devsimplifiedai",
                "subscriber_count": 26800,
                "niche_overlap_pct": 88,
                "common_topics": ["LangChain", "Vector DBs", "Open Source AI"],
                "collab_video_concept": "Building an Autonomous Coding Agent from Scratch",
                "reach_potential": "+950 New Subscribers (Estimated 18k Shared Views)"
            },
            {
                "channel_name": "Modern Frontend Lab",
                "handle": "@modernfrontend",
                "subscriber_count": 35400,
                "niche_overlap_pct": 84,
                "common_topics": ["Next.js 15", "Tailwind CSS", "React 19"],
                "collab_video_concept": "Fullstack Showdown: Python FastAPI Backend meets Next.js App Router",
                "reach_potential": "+1,500 New Subscribers (Estimated 30k Shared Views)"
            }
        ]

    def get_matched_creators(self) -> List[CollabCreator]:
        return [CollabCreator(**c) for c in self._collab_database]

collab_service = CollabMatcherService()
