from fastapi import APIRouter
from typing import List
from backend.app.models.schemas import ContentGapItem, WeeklyGrowthPlanResponse, DayPlan
from backend.app.services.nlp_service import nlp_service

router = APIRouter(prefix="/api/gaps", tags=["Content Gaps & Growth Planning"])

@router.get("/content-gaps", response_model=List[ContentGapItem])
def get_audience_content_gaps():
    """Mines viewer comments to find topics audience is asking for that haven't been made yet."""
    gaps = nlp_service.extract_content_gaps()
    return [ContentGapItem(**g) for g in gaps]

@router.get("/weekly-plan", response_model=WeeklyGrowthPlanResponse)
def get_weekly_growth_plan():
    """Generates an automated 7-day action plan combining trends and audience content gaps."""
    gaps = nlp_service.extract_content_gaps()
    top_gap = gaps[0]["suggested_title"] if gaps else "FastAPI & React Fullstack Tutorial"

    daily_plan = [
        DayPlan(
            day="Monday",
            task_type="scripting",
            task_description=f"Script hook and outline for: '{top_gap}'. Keep intro under 10 seconds.",
            recommended_time="10:00 AM",
            suggested_tags=["#webdev", "#coding", "#tutorial"]
        ),
        DayPlan(
            day="Tuesday",
            task_type="recording",
            task_description="Record video code walkthrough and screen recording. Capture 3 high-contrast thumbnail frames.",
            recommended_time="2:00 PM",
            suggested_tags=["#devvlog", "#learntocode"]
        ),
        DayPlan(
            day="Wednesday",
            task_type="editing",
            task_description="Edit video, add zoom cuts on key code blocks, add sound design on terminal transitions.",
            recommended_time="11:00 AM",
            suggested_tags=[]
        ),
        DayPlan(
            day="Thursday",
            task_type="publishing",
            task_description="Upload video with optimized power title and pin top viewer comment to start discussion.",
            recommended_time="7:00 PM EST (Peak Audience)",
            suggested_tags=["#fastapi", "#react", "#programming"]
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
            task_description="Create a 45-second YouTube Shorts / Instagram Reel highlighting the best code snippet from Thursday's video.",
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
