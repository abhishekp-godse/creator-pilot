"""
CreatorPilot - Authentication & User Profile Domain Models (MVC)
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class CreatorAccount(BaseModel):
    id: str
    channel_name: str
    handle: str
    niche: str
    avatar_url: str
    subscriber_count: int
    total_views: int
    video_count: int
    watch_time_hours: float
    health_score: int

class LoginRequest(BaseModel):
    identifier: str # Email or Channel Handle (e.g. @codecraftstudio)
    password: str
    remember_me: bool = True

class RegisterRequest(BaseModel):
    channel_name: str
    handle: str
    niche: str
    email: str
    password: str

class AuthResponse(BaseModel):
    success: bool
    token: str
    token_type: str = "Bearer"
    user: CreatorAccount
    message: str

class LogoutResponse(BaseModel):
    success: bool
    message: str
