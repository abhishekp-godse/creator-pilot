from fastapi import APIRouter
from backend.app.models.schemas import ChatRequest, ChatResponse
from backend.app.services.coach_service import coach_service

router = APIRouter(prefix="/api/coach", tags=["AI Conversational Coach"])

@router.post("/chat", response_model=ChatResponse)
def chat_with_coach(payload: ChatRequest):
    """
    Chat endpoint for the personal AI creator coach.
    Accepts user questions and returns channel-informed prescriptive advice with audio text.
    """
    history_dicts = [{"role": m.role, "content": m.content} for m in (payload.history or [])]
    result = coach_service.chat(user_message=payload.message, history=history_dicts)
    return ChatResponse(**result)
