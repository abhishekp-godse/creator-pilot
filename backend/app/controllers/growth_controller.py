"""
CreatorPilot - Growth & Action Controller
Provides Content Gap Mining, Idea Vault, Collab Matcher, and Monetization Sprint endpoints.
"""

from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from backend.app.models.growth_model import (
    ContentGapItem,
    WeeklyGrowthPlanResponse,
    IdeaVaultItem,
    CollabCreator,
    MonetizationSprint,
    DayPlan
)
from backend.app.services.nlp_service import nlp_service
from backend.app.services.idea_vault_service import idea_vault_service
from backend.app.services.collab_service import collab_service
from backend.app.services.youtube_service import youtube_service

router = APIRouter(prefix="/api/growth", tags=["Growth & Action Controller"])

class AddIdeaRequest(BaseModel):
    title: str
    source: str = "user"
    effort: str = "Medium (3-5h)"

@router.get("/content-gaps", response_model=List[ContentGapItem])
def get_content_gaps():
    return [ContentGapItem(**g) for g in nlp_service.extract_content_gaps()]

@router.get("/idea-vault", response_model=List[IdeaVaultItem])
def get_idea_vault():
    return idea_vault_service.get_all_ideas()

@router.post("/idea-vault", response_model=IdeaVaultItem)
def add_idea_to_vault(payload: AddIdeaRequest):
    return idea_vault_service.add_idea(title=payload.title, source=payload.source, effort=payload.effort)

@router.get("/collab-matcher", response_model=List[CollabCreator])
def get_collab_creators():
    return collab_service.get_matched_creators()

@router.get("/monetization-sprint", response_model=MonetizationSprint)
def get_monetization_sprint():
    channel = youtube_service.get_channel_details()
    current_hours = channel["watch_time_hours"]
    target_hours = channel["monetization_watch_target"]
    remaining = max(0, target_hours - current_hours)
    
    # Calculate days based on daily velocity (~38 watch hours/day)
    estimated_days = max(1, int(remaining / 38))

    return MonetizationSprint(
        current_watch_hours=current_hours,
        target_watch_hours=target_hours,
        remaining_hours=remaining,
        estimated_days_to_reach=estimated_days,
        recommended_actions=[
            "Host a 1.5-hour Live Q&A Stream on FastAPI (Yields ~180 watch hours)",
            "Publish a 45-minute End-to-End Project Build tutorial",
            "Bundle your top 5 tutorials into an auto-playing YouTube Playlist"
        ]
    )

@router.get("/weekly-plan", response_model=WeeklyGrowthPlanResponse)
def get_weekly_plan():
    gaps = nlp_service.extract_content_gaps()
    top_title = gaps[0]["suggested_title"] if gaps else "FastAPI & React Fullstack Tutorial"

    daily_plan = [
        DayPlan(
            day="Monday",
            task_type="scripting",
            task_description=f"Script hook and outline for: '{top_title}'. Keep intro hook under 8 seconds.",
            recommended_time="10:00 AM",
            suggested_tags=["#webdev", "#coding", "#tutorial"]
        ),
        DayPlan(
            day="Tuesday",
            task_type="recording",
            task_description="Record code demo screen capture. Shoot 3 high-contrast expression thumbnails.",
            recommended_time="2:00 PM",
            suggested_tags=["#programming", "#learntocode"]
        ),
        DayPlan(
            day="Wednesday",
            task_type="editing",
            task_description="Edit video, add zoom cuts on crucial code lines, sound effects on terminal runs.",
            recommended_time="11:00 AM",
            suggested_tags=[]
        ),
        DayPlan(
            day="Thursday",
            task_type="publishing",
            task_description="Upload video with power curiosity title at peak audience window.",
            recommended_time="7:00 PM EST (Peak Audience)",
            suggested_tags=["#fastapi", "#react", "#python"]
        ),
        DayPlan(
            day="Friday",
            task_type="community",
            task_description="Post a YouTube Community tab poll: 'What is your biggest blocker with authentication?'",
            recommended_time="4:00 PM",
            suggested_tags=["#community"]
        ),
        DayPlan(
            day="Saturday",
            task_type="scripting",
            task_description="Create a 45-second YouTube Short / Reel demonstrating the fastest snippet from Thursday.",
            recommended_time="1:00 PM",
            suggested_tags=["#shorts", "#quicktips"]
        ),
        DayPlan(
            day="Sunday",
            task_type="community",
            task_description="Review comment questions and favorite high-engagement feedback for next week's gap mining.",
            recommended_time="6:00 PM",
            suggested_tags=[]
        )
    ]

    return WeeklyGrowthPlanResponse(
        week_focus="High-Demand Educational Content (Closing Audience Knowledge Gaps)",
        target_kpi="+450 Subscribers and +18,000 Views",
        daily_plan=daily_plan,
        projected_reach="~25,000 Impressions"
    )
