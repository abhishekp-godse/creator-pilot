"""
CreatorPilot - Conversational Coach Controller
"""

from fastapi import APIRouter
from backend.app.models.chat_model import ChatRequest, ChatResponse
from backend.app.services.coach_service import coach_service

router = APIRouter(prefix="/api/coach", tags=["AI Coach Controller"])

@router.post("/chat", response_model=ChatResponse)
def chat_with_coach(payload: ChatRequest):
    history_dicts = [{"role": m.role, "content": m.content} for m in (payload.history or [])]
    result = coach_service.chat(user_message=payload.message, history=history_dicts)
    
    return ChatResponse(
        reply=result["reply"],
        action_nudges=result.get("action_nudges", []),
        audio_text=result.get("audio_text"),
        suggested_quick_replies=[
            "Why did my last video flop?",
            "What should I post this week?",
            "How do I hit monetization this month?"
        ]
    )
