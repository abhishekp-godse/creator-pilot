"""
CreatorPilot - Conversational Coach & Memory Domain Models
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str # 'user' or 'assistant'
    content: str
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    reply: str
    action_nudges: List[str] = []
    audio_text: Optional[str] = None
    suggested_quick_replies: List[str] = []
