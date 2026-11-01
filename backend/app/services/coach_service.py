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
        self.topic_counters = {
            "flop": 0,
            "ideas": 0,
            "monetization": 0,
            "sentiment": 0,
            "titles": 0,
            "cadence": 0,
            "scripting": 0,
            "algorithm": 0,
            "general": 0
        }
        self.last_topic = None

    def detect_topic(self, clean_msg: str) -> str:
        is_followup = any(w in clean_msg for w in ["another", "more", "else", "what about", "continue", "next", "further", "second reason", "third reason"])
        if is_followup and self.last_topic:
            return self.last_topic

        if any(w in clean_msg for w in ["last video", "flop", "underperform", "drop off", "retention", "why did", "views low", "bad video"]):
            return "flop"
        if any(w in clean_msg for w in ["what should i post", "post this week", "video idea", "next video", "recommend", "topic", "content gap"]):
            return "ideas"
        if any(w in clean_msg for w in ["monetiz", "watch time", "subscriber target", "ypp", "4000", "ad revenue"]):
            return "monetization"
        if any(w in clean_msg for w in ["sentiment", "comment", "feedback", "audience say", "critique", "positive", "negative"]):
            return "sentiment"
        if any(w in clean_msg for w in ["title", "ctr", "click", "thumbnail", "headline", "clickbait"]):
            return "titles"
        if any(w in clean_msg for w in ["consisten", "schedule", "streak", "burnout", "upload time", "best time"]):
            return "cadence"
        if any(w in clean_msg for w in ["script", "story", "intro", "hook", "structure", "pacing"]):
            return "scripting"
        if any(w in clean_msg for w in ["algorithm", "recommendation", "browse", "suggested", "seo"]):
            return "algorithm"
        return "general"

    def chat(self, user_message: str, history: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Process user query with full channel context awareness and non-repeating Gemini strategy.
        """
        clean_msg = user_message.lower().strip()
        last_video = RECENT_VIDEOS[0]
        gaps = nlp_service.extract_content_gaps()
        top_trend = TRENDING_TOPICS[0]
        health = ml_service.compute_growth_health_score()

        topic = self.detect_topic(clean_msg)
        count = self.topic_counters.get(topic, 0)
        self.topic_counters[topic] = count + 1
        self.last_topic = topic

        # 1. Underperformance / Flop Dimensions (5 unique non-repeating angles)
        if topic == "flop":
            dim = count % 5
            if dim == 0:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Dimension 1/5: Retention Hook & Intro Trimming\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Your latest video (_{last_video['title']}_) lost **{int(last_video['retention_hook_drop'] * 100)}% of viewers in the first 30 seconds** because your opening logo sequence and setup preamble lasted 45 seconds.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Benchmark 30s Retention: **65%** | Your Video: **{int((1 - last_video['retention_hook_drop']) * 100)}%**\n"
                    f"• Drop Trigger: {last_video['drop_reason']}\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Cut your animated intro sequence down to <4 seconds.\n"
                    f"2. Adopt the '8-Second Deliverable Rule': show the final working outcome in frame one.\n"
                    f"3. State viewer payoff immediately: _'By the end of this video, you will have built this exact live system...'_"
                )
                action_nudges = [
                    "What about the thumbnail expectation gap?",
                    "How to fix mid-video 3-minute drop?",
                    "Script a 10-second opening hook"
                ]
                audio = f"Alex, your latest video lost 42% of viewers in the first 30 seconds due to a 45-second intro. Cut the logo bumper and show the working result in the first 8 seconds."

            elif dim == 1:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Dimension 2/5: Thumbnail vs. First 60s Expectation Disconnect\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Building on our hook analysis: your video achieved a strong **8.1% Click-Through Rate**, but average view duration flattened sharply at 1:15. This points to an **Expectation Mismatch**.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• CTR: **8.1% (High)** vs 3-Min Retention: **48% (Steep Drop)**.\n"
                    f"• When viewers click on a bold visual promise that isn't visually corroborated in the first 60 seconds, YouTube registers an unsatisfied session.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Apply the 'Visual Continuity Rule': whatever hero asset appears on your thumbnail must be visible in your first 3 frames.\n"
                    f"2. Avoid spending the first 90 seconds explaining prerequisites; deliver an immediate micro-insight.\n"
                    f"3. Ensure your title and thumbnail complement each other rather than repeating the same words."
                )
                action_nudges = [
                    "Examine 3-minute retention valley",
                    "Audit audio comfort & mix",
                    "What should I post this week?"
                ]
                audio = f"Looking at dimension 2, your 8.1% click-through rate is strong, but viewers bounced early because the thumbnail promised something the first 60 seconds delayed. Show your thumbnail visual in frame one."

            elif dim == 2:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Dimension 3/5: The 3-Minute Cognitive Fatigue Slump\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Moving to mid-video retention: analytics show a secondary drop between **2:45 and 4:15**, where an additional 18% of the audience dropped off during the deep explanation section.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Pacing Diagnostic: **The Monotone Valley**—static camera framing for 110 consecutive seconds without graphics, sound cues, or pattern interrupts.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Adopt the 'Rule of 12': insert a visual pattern interrupt (zoom, diagram, code annotation, sound cue) every 10–14 seconds.\n"
                    f"2. Use dual-pane picture-in-picture when explaining complex architecture or multi-step concepts.\n"
                    f"3. Cut out microscopic breathing pauses and hesitation sounds in the middle third of your timeline."
                )
                action_nudges = [
                    "Audit audio mix & volume",
                    "Audience bucket expansion",
                    "Next high-retention video idea"
                ]
                audio = f"Your retention graph reveals a secondary drop between minutes 2 and 4. Insert a visual pattern interrupt like an on-screen diagram every 12 seconds to prevent viewer cognitive fatigue."

            elif dim == 3:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Dimension 4/5: Audio Engineering & Viewer Ear Fatigue\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"A subtle yet critical retention factor: audience comments explicitly noted **'audio was quiet on the left channel'** and uneven vocal levels.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Over **74% of your viewers** consume videos on mobile headphones. Unbalanced stereo panning or wide dynamic volume range triggers subconscious listener irritation, causing swift tab exits.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Sum your vocal commentary track to Centered Mono.\n"
                    f"2. Apply a 2.5:1 ratio compressor to tame loud laughter/shouts while boosting quiet explanations.\n"
                    f"3. Target -14.0 LUFS integrated loudness with a -1.0 dB True Peak ceiling for YouTube normalization."
                )
                action_nudges = [
                    "Audience bucket expansion",
                    "Generate weekly content plan",
                    "Check monetization progress"
                ]
                audio = f"Multiple comments flagged unbalanced sound. Mix your voice track in mono at minus 14 LUFS so mobile headphone listeners don't experience ear fatigue."

            else:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Dimension 5/5: Audience Bucket Expansion & Cold Traffic Bounces\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Dimension #5 reveals an algorithmic shift: after initial release, YouTube pushed impressions from core subscribers into broader **Browse & Suggested Feeds**.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Core Subscriber Retention: **72%** | Cold Browse Traffic Retention: **38%**.\n"
                    f"• Colder viewers bounced because the tutorial assumed deep prerequisite knowledge without context.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Add granular chapter markers with descriptive outcome labels.\n"
                    f"2. Pin a top comment containing downloadable starter code or recipe cheat sheets.\n"
                    f"3. Add an accessibility bracket tag in your title like `[Zero to Hero]` or `[Full Blueprint]`."
                )
                action_nudges = [
                    "What should I post this week?",
                    "How to score my next title?",
                    "Monetization watch hours check"
                ]
                audio = f"Finally, YouTube pushed your video to colder browse feeds where viewers lacked context. Adding chapter timestamps and a pinned starter kit will stabilize browse retention."

            return {"reply": reply, "action_nudges": action_nudges, "audio_text": audio}

        # 2. Video Ideas / Strategy Dimensions (5 unique non-repeating angles)
        elif topic == "ideas":
            dim = count % 5
            top_gap = gaps[0] if gaps else {"topic": "Full-Stack Tutorial", "suggested_title": "Build a SaaS App in 2026", "request_count": "89+"}
            if dim == 0:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Strategy Angle 1/5: #1 Audience-Demanded Content Gap\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"The highest probability video concept right now is **'{top_gap['topic']}'**. Over **{top_gap['request_count']} comments** were mined directly from your comment threads.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Suggested Title: **{top_gap['suggested_title']}**\n"
                    f"• Predicted CTR: **8.4%** | Trend-Fit Score: **88% Match**\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Structure the tutorial around the 3 most common stumbling blocks mentioned in comments.\n"
                    f"2. Pin a comment thanking the community: _'You asked for this in 89 comments—here is the complete breakdown!'_\n"
                    f"3. Publish on Thursday at 7:00 PM EST during peak subscriber activity."
                )
                action_nudges = [
                    "Give me a high-velocity trend idea",
                    "Suggest a controversial topic",
                    "Evergreen search compounder"
                ]
                audio = f"Alex, your top video opportunity is {top_gap['topic']}. Over {top_gap['request_count']} comments requested it, giving you an immediate built-in audience."

            elif dim == 1:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Strategy Angle 2/5: High-Velocity Search Spike (Riding Wave)\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"If you want rapid view velocity, ride the current search surge: **'{top_trend['topic']}'**. Search momentum is surging at **+{int(top_trend['search_velocity_growth'] * 100)}%**.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Niche Fit: **{int(top_trend['niche_fit_score'] * 100)}%** | Window of Opportunity: **Peak window expires in 14 days**.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Hook Formula: _'Why {top_trend['topic']} Changes Everything in 2026'_\n"
                    f"2. Focus on practical transition: why legacy workflows are becoming obsolete.\n"
                    f"3. Keep total runtime under 12 minutes to maximize algorithmic recommendation velocity."
                )
                action_nudges = [
                    "Suggest a controversial debate topic",
                    "Evergreen beginner compounder",
                    "Peer creator collaboration idea"
                ]
                audio = f"Looking for rapid view velocity? Cover {top_trend['topic']}. Search momentum is surging at 140% and the peak window lasts two weeks."

            elif dim == 2:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Strategy Angle 3/5: The Contrarian Myth-Buster (High Comment Velocity)\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Respectful controversy is the #1 trigger for algorithmic comment velocity. Pitch a contrarian concept: **'Why You Should Stop Using Express.js in 2026 (Use This Instead)'**.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Contrarian videos historically drive **3.2x higher comment-to-view ratios**.\n"
                    f"• YouTube's recommendation neural network uses comment velocity as a primary viral breakout indicator.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. State your provocative hypothesis in the first 5 seconds.\n"
                    f"2. Back up your stance with objective benchmarks, data tables, or side-by-side evidence.\n"
                    f"3. Invite audience debate: _'Do you agree with this benchmark, or are you sticking with your current stack?'_"
                )
                action_nudges = [
                    "Evergreen search compounder",
                    "Peer collaboration idea",
                    "How to script this concept"
                ]
                audio = f"Consider a contrarian debate video. Challenging conventional wisdom generates three times more comments, which triggers rapid algorithmic promotion."

            elif dim == 3:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Strategy Angle 4/5: The Evergreen Search Compounder (18-Month Passive Traffic)\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"While trends spike and fade, an evergreen foundational guide produces steady daily views and passive watch hours for 18+ months: **'Complete Full-Stack Architecture Roadmap for 2026'**.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Evergreen tutorials account for **44% of long-term watch hours** for channels in your niche, providing baseline stability toward monetization.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Design the video to be timeless: focus on core principles rather than fleeting library versions.\n"
                    f"2. Optimize metadata for search queries: 'How to', 'Step by Step', 'Complete Guide'.\n"
                    f"3. Create a downloadable reference sheet (GitHub repo or PDF) linked in the description."
                )
                action_nudges = [
                    "Peer creator collaboration pitch",
                    "Monetization watch hour sprint",
                    "Test title CTR potential"
                ]
                audio = f"Balance your trends with an evergreen beginner masterclass. Evergreen guides provide compounding watch hours every single day for years."

            else:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Strategy Angle 5/5: Cross-Audience Peer Collaboration (Synergy Multiplier)\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Accelerate subscriber acquisition by partnering with **Pythonic Dev** (31.2k Subs).\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• Synergy Match: **92% Match** | Joint Concept: **'FastAPI vs Express.js 2026 Benchmark Showdown'**\n"
                    f"• Expected Crossover: **+1,200 New Subscribers Potential**\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Split the topic into two parts: Part 1 on your channel, Part 2 on their channel.\n"
                    f"2. Include a pinned comment and end-screen card routing viewers to the partner video.\n"
                    f"3. Reach out via Twitter/Email with a ready-to-execute 3-bullet concept outline."
                )
                action_nudges = [
                    "Outline the joint video",
                    "Review top audience gap",
                    "Check monetization progress"
                ]
                audio = f"Partner with Pythonic Dev. A joint video comparing FastAPI and Express can cross-pollinate 1,200 new subscribers directly into your channel."

            return {"reply": reply, "action_nudges": action_nudges, "audio_text": audio}

        # 3. Monetization Dimensions
        elif topic == "monetization":
            dim = count % 4
            subs_needed = max(0, CHANNEL_INFO["monetization_sub_target"] - CHANNEL_INFO["subscriber_count"])
            hours_needed = max(0, CHANNEL_INFO["monetization_watch_target"] - CHANNEL_INFO["watch_time_hours"])
            daily_hours = round(hours_needed / 14, 1)

            if dim == 0:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Monetization Sprint 1/4: Mathematical Daily Quota Formula\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"You have **{CHANNEL_INFO['subscriber_count']:,} subscribers** (completed!) and **{CHANNEL_INFO['watch_time_hours']:,} of 4,000 watch hours** (87% completed). You only need **{int(hours_needed)} more hours**!\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• 14-Day Sprint Target: **{daily_hours} watch hours per day**.\n"
                    f"• At your current view velocity, you will reach full monetization in approximately **14 days**.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Publish 1 high-retention video (12–15 mins) every 5 days.\n"
                    f"2. Target 55% average view duration to capture ~7 minutes of watch time per viewer.\n"
                    f"3. Promote highest-retention older videos on your YouTube Community Tab."
                )
                action_nudges = [
                    "Session time playlist multiplier",
                    "Live stream watch hour sprint",
                    "Shorts vs long-form YPP rules"
                ]
                audio = f"You have passed the subscriber threshold! You only need {int(hours_needed)} more watch hours, requiring about {daily_hours} hours per day over the next two weeks."

            elif dim == 1:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Monetization Sprint 2/4: Session Time & Bingeable Playlist Multiplier\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"YouTube's recommendation algorithm places massive weighting on **Total Session Watch Time**—keeping viewers watching multiple videos in a single sitting.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• A viewer watching 3 consecutive videos generates **3.2x more watch hours** than 3 separate single-video viewers.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Group your top 3 complementary tutorials into a dedicated 'Mastery Playlist'.\n"
                    f"2. Set the end screen of Video 1 to auto-cue Video 2 in the final 10 seconds.\n"
                    f"3. Pin a comment in each video linking directly to the next installment."
                )
                action_nudges = [
                    "Live stream fast-track",
                    "Shorts vs long-form rules",
                    "What should I post this week?"
                ]
                audio = f"To speed up watch hours, focus on session time. Group your top 3 tutorials into an auto-playing playlist to double your watch time per viewer."

            elif dim == 2:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Monetization Sprint 3/4: The Live Stream Fast-Track (150 Hours in One Night)\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"The fastest shortcut to bank watch hours is an interactive live stream: a single **2-hour live broadcast with 75 concurrent viewers** generates **150 watch hours** in one evening.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• 75 viewers × 2 hours = 150 hours banked instantly. This covers **29% of your remaining 520-hour gap** in just 120 minutes.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Schedule a 'Live Q&A & Code Review' 48 hours in advance.\n"
                    f"2. Prepare 3 seed topics to prevent dead air.\n"
                    f"3. Leave replay public so offline viewers continue generating passive hours."
                )
                action_nudges = [
                    "Shorts vs long-form YPP warning",
                    "Review audience sentiment feedback",
                    "Why did my last video flop?"
                ]
                audio = f"Host a two-hour live stream with 75 viewers to bank 150 watch hours in one evening. That wipes out nearly a third of your remaining monetization gap."

            else:
                reply = (
                    f"### ✨ Gemini Growth Intelligence • Monetization Sprint 4/4: YouTube Shorts vs. Long-Form YPP Warning\n\n"
                    f"💡 **Executive Takeaway**:\n"
                    f"Critical rule: **YouTube Shorts watch hours do NOT count** toward the standard 4,000-hour YPP threshold. Shorts require 10 million views in 90 days.\n\n"
                    f"📊 **Telemetry Evidence**:\n"
                    f"• However, Shorts are exceptional for sub-acquisition and discovery. Use Shorts strictly as a teaser funnel into 12-minute long-form videos.\n\n"
                    f"⚡ **Tactical Action Blueprint**:\n"
                    f"1. Extract the most captivating 45-second moment from your long-form tutorial.\n"
                    f"2. Use YouTube's 'Related Video' feature to link the Short directly to full tutorial.\n"
                    f"3. Add on-screen callout: _'Full build linked below ⬇️'_"
                )
                action_nudges = [
                    "Precision daily sprint quota",
                    "Bingeable playlist multiplier",
                    "What should I post this week?"
                ]
                audio = f"Remember that YouTube Shorts watch time does not count toward the 4,000-hour threshold. Use Shorts strictly as teasers that route viewers to your long-form videos."

            return {"reply": reply, "action_nudges": action_nudges, "audio_text": audio}

        # 4. Default / General Strategy
        else:
            reply = (
                f"### ✨ Gemini Growth Intelligence • Comprehensive Channel Telemetry\n\n"
                f"💡 **Executive Takeaway**:\n"
                f"Your channel **{CHANNEL_INFO['channel_name']}** has an active Growth Health Score of **{health['overall_score']}/100** across all 10 platform modules.\n\n"
                f"📊 **Telemetry Evidence**:\n"
                f"• Subscribers: **{CHANNEL_INFO['subscriber_count']:,}** • Watch Hours: **{CHANNEL_INFO['watch_time_hours']:,} / 4,000** (87%)\n"
                f"• Upload Alert: Last posted {CHANNEL_INFO['last_upload_days_ago']} days ago. Target cadence is every 5 days.\n"
                f"• Comment Demand: {len(gaps)} uncovered questions waiting for dedicated tutorials.\n\n"
                f"⚡ **Tactical Action Blueprint**:\n"
                f"1. Post within the next 48 hours to preserve your {CHANNEL_INFO['current_streak_weeks']}-week streak multiplier.\n"
                f"2. Tap into your #1 comment gap to capture built-in audience demand.\n"
                f"3. Trim your intro bumper to <5s to boost first-30-second retention."
            )
            action_nudges = [
                "Why did my last video flop?",
                "What should I post this week?",
                "How close am I to monetization?",
                "Summarize viewer sentiment feedback"
            ]
            audio = f"Welcome back Alex! Your channel is in good shape with a health score of 82. What specific topic would you like to explore today?"
            return {"reply": reply, "action_nudges": action_nudges, "audio_text": audio}

coach_service = AICoachService()

