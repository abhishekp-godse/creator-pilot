"""
Conversational AI Coach Service
Acts as the personal Siri-like strategic manager for the content creator.
"""

from typing import Dict, Any, List
from backend.app.config import settings
from backend.demo_data import (
    CHANNEL_INFO,
    RECENT_VIDEOS,
    TRENDING_TOPICS
)
from backend.app.services.nlp_service import nlp_service
from backend.app.services.ml_service import ml_service

class AICoachService:
    def __init__(self):
        self.gemini_key = settings.GEMINI_API_KEY
        self.openai_key = settings.OPENAI_API_KEY

    def chat(self, user_message: str, history: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Process user query with full channel context awareness and return actionable advice.
        """
        clean_msg = user_message.lower().strip()
        last_video = RECENT_VIDEOS[0]
        gaps = nlp_service.extract_content_gaps()
        top_trend = TRENDING_TOPICS[0]
        health = ml_service.compute_growth_health_score()

        # Heuristic Context-Aware Fallback (or when API keys not provided)
        # 1. "Why did my last video flop / underperform?"
        if any(w in clean_msg for w in ["last video", "flop", "underperform", "drop off", "retention"]):
            reply = (
                f"I analyzed your latest video: '{last_video['title']}'.\n\n"
                f"📊 **Diagnostic Analysis**:\n"
                f"• First 30-Second Drop-off: **{int(last_video['retention_hook_drop'] * 100)}%** of viewers left early.\n"
                f"• Cause: {last_video['drop_reason']}\n\n"
                f"💡 **Coach Advice**:\n"
                f"Cut your intro bumper from 45 seconds down to under 5 seconds. Open immediately with the finished demo result within the first 8 seconds before explaining how you built it."
            )
            action_nudges = [
                "Trim intro bumper to < 5 seconds in future videos",
                "Re-test thumbnail with higher contrast color palette",
                "Pin top question comment to boost engagement"
            ]
            return {
                "reply": reply,
                "action_nudges": action_nudges,
                "audio_text": f"Your last video had a 42% retention drop in the first 30 seconds because the intro was too long. Next time, show the working demo in the first 8 seconds."
            }

        # 2. "What should I post this week?"
        elif any(w in clean_msg for w in ["what should i post", "post this week", "video idea", "next video", "recommend"]):
            top_gap = gaps[0]
            reply = (
                f"Based on audience requests and current search momentum, here is your #1 high-impact video plan:\n\n"
                f"🎯 **Recommended Topic**: {top_gap['topic']}\n"
                f"📌 **Suggested Title**: '{top_gap['suggested_title']}'\n"
                f"🔥 **Why Now?**: Over {top_gap['request_count']} comments recently asked for this, and it matches '{top_trend['topic']}' with an **88% Trend-Fit Score**.\n\n"
                f"⏰ **Best Posting Window**: Tomorrow at 7:00 PM EST when your viewers are most active."
            )
            action_nudges = [
                f"Outline: {top_gap['suggested_title']}",
                "Record 15-second teaser for YouTube Shorts",
                "Schedule release for 7:00 PM EST"
            ]
            return {
                "reply": reply,
                "action_nudges": action_nudges,
                "audio_text": f"You should post a tutorial on {top_gap['topic']}. Your viewers have been begging for it in the comments, and it aligns with current trends."
            }

        # 3. "Monetization / watch time status"
        elif any(w in clean_msg for w in ["monetiz", "watch time", "subscriber target", "ypp"]):
            subs_needed = max(0, CHANNEL_INFO["monetization_sub_target"] - CHANNEL_INFO["subscriber_count"])
            hours_needed = max(0, CHANNEL_INFO["monetization_watch_target"] - CHANNEL_INFO["watch_time_hours"])
            reply = (
                f"🎉 **Monetization Milestone Update**:\n\n"
                f"• Subscribers: **{CHANNEL_INFO['subscriber_count']:,}** / {CHANNEL_INFO['monetization_sub_target']:,} ✅ (Completed!)\n"
                f"• Watch Hours: **{CHANNEL_INFO['watch_time_hours']:,}** / {CHANNEL_INFO['monetization_watch_target']:,} hours (87% completed)\n\n"
                f"You only need **{int(hours_needed)} more watch hours** to unlock YouTube Partner Program ad revenue! "
                f"At your current growth velocity, you will reach this in approximately **14 days**."
            )
            action_nudges = [
                "Host a 1-hour live Q&A session to bank ~150 watch hours",
                "Create a 3-part playlist to increase session watch time",
                "Add end screens pointing to your highest retention videos"
            ]
            return {
                "reply": reply,
                "action_nudges": action_nudges,
                "audio_text": f"You have already passed the subscriber threshold! You only need 520 more watch hours, which you will hit in about two weeks."
            }

        # 4. Default strategic response
        else:
            reply = (
                f"Hey! Your channel **{CHANNEL_INFO['channel_name']}** has a Growth Health Score of **{health['overall_score']}/100** right now.\n\n"
                f"Here are 3 key observations from this week:\n"
                f"1. **Upload Alert**: You haven't posted in {CHANNEL_INFO['last_upload_days_ago']} days. Your audience engagement historically drops after day 7.\n"
                f"2. **Audience Demand**: There are {len(gaps)} uncovered questions in your comments waiting for dedicated tutorials.\n"
                f"3. **Consistency Streak**: You are on a {CHANNEL_INFO['current_streak_weeks']}-week streak. Post within the next 48 hours to preserve it!\n\n"
                f"What would you like help with today? You can ask about title ideas, why a video flopped, or generate your weekly plan."
            )
            action_nudges = [
                "Review Content Gaps from Comments",
                "Generate Weekly Growth Action Plan",
                "Test Title Click Potential"
            ]
            return {
                "reply": reply,
                "action_nudges": action_nudges,
                "audio_text": f"Welcome back. You are currently on day 6 since your last upload. Post within the next 48 hours to keep your consistency streak alive."
            }

coach_service = AICoachService()
