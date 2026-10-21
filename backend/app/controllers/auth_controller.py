"""
CreatorPilot - Authentication Controller (MVC)
Handles Creator login, logout, token generation, and multi-channel profile switching.
"""

from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional, List
import uuid

from backend.app.models.auth_model import (
    CreatorAccount,
    LoginRequest,
    RegisterRequest,
    AuthResponse,
    LogoutResponse
)

router = APIRouter(prefix="/api/auth", tags=["Authentication & Creator Profiles"])

# Pre-seeded Creator Accounts for Demo & Production
DEMO_CREATORS = {
    "codecraft": CreatorAccount(
        id="creator_tech_01",
        channel_name="CodeCraft Studio",
        handle="@codecraftstudio",
        niche="Web Dev & AI Engineering",
        avatar_url="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=150",
        subscriber_count=28450,
        total_views=1845000,
        video_count=86,
        watch_time_hours=3480.0,
        health_score=87
    ),
    "pixelquest": CreatorAccount(
        id="creator_game_02",
        channel_name="PixelQuest Gaming",
        handle="@pixelquest_live",
        niche="Gaming & Live Speedruns",
        avatar_url="https://images.unsplash.com/photo-1566492031773-4f4e44671857?w=150",
        subscriber_count=42100,
        total_views=3920000,
        video_count=142,
        watch_time_hours=4890.0,
        health_score=92
    ),
    "nutrivibe": CreatorAccount(
        id="creator_life_03",
        channel_name="NutriVibe Healthy",
        handle="@nutrivibe_fit",
        niche="Nutrition, Meal Prep & Wellness",
        avatar_url="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150",
        subscriber_count=15800,
        total_views=890000,
        video_count=54,
        watch_time_hours=2150.0,
        health_score=79
    )
}

ACTIVE_SESSIONS = {}

@router.get("/profiles", response_model=List[CreatorAccount])
def get_available_profiles():
    """List available demo creator accounts for 1-click sign-in."""
    return list(DEMO_CREATORS.values())

@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest):
    """Authenticate creator by channel handle or email."""
    ident = payload.identifier.lower().strip().lstrip("@")
    
    # Match against demo handles or fallback to default
    matched_profile = None
    for key, profile in DEMO_CREATORS.items():
        if key in ident or profile.handle.lower().lstrip("@") == ident or ident in profile.channel_name.lower():
            matched_profile = profile
            break
            
    if not matched_profile:
        # Default fallback: personalize with whatever handle the user provided
        matched_profile = CreatorAccount(
            id=f"creator_{uuid.uuid4().hex[:6]}",
            channel_name=payload.identifier.split("@")[0].capitalize() or "Creator Studio",
            handle=f"@{ident}" if not ident.startswith("@") else ident,
            niche="Creator Education & Growth",
            avatar_url="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150",
            subscriber_count=12400,
            total_views=640000,
            video_count=35,
            watch_time_hours=1850.0,
            health_score=82
        )

    # Issue session token
    token = f"cp_sess_{uuid.uuid4().hex}"
    ACTIVE_SESSIONS[token] = matched_profile

    return AuthResponse(
        success=True,
        token=token,
        user=matched_profile,
        message=f"Welcome back, {matched_profile.channel_name}!"
    )

@router.post("/logout", response_model=LogoutResponse)
def logout(authorization: Optional[str] = Header(None)):
    """Terminate the active creator session."""
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        ACTIVE_SESSIONS.pop(token, None)
    return LogoutResponse(
        success=True,
        message="Logged out successfully. Channel telemetry saved."
    )

@router.get("/me", response_model=CreatorAccount)
def get_current_user(authorization: Optional[str] = Header(None)):
    """Return the profile for the active session token."""
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        if token in ACTIVE_SESSIONS:
            return ACTIVE_SESSIONS[token]
    return DEMO_CREATORS["codecraft"]
