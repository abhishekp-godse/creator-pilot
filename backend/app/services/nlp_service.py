"""
NLP Service for Comment Sentiment & Content Gap Finder
Extracts actionable insights from viewer comments using linguistic patterns & sentiment heuristics.
"""

import re
from typing import List, Dict, Any
from backend.demo_data import COMMENTS_DATASET, RECENT_VIDEOS

class NLPService:
    def __init__(self):
        # Interrogative and request regex triggers
        self.question_patterns = [
            re.compile(r"can you (?:please )?(make|do|explain|cover|show)", re.IGNORECASE),
            re.compile(r"how (?:do|can|to|should) (?:i|we|you)", re.IGNORECASE),
            re.compile(r"could you (?:please )?(make|do|explain|cover|show)", re.IGNORECASE),
            re.compile(r"please (?:make|do|create|cover) a? (?:video|tutorial)", re.IGNORECASE),
            re.compile(r"when is the (.*) coming", re.IGNORECASE),
            re.compile(r"why (?:does|did|is|are)", re.IGNORECASE),
            re.compile(r"stuck on (.*)", re.IGNORECASE)
        ]

        # Sentiment lexicon
        self.positive_words = {
            "love", "loved", "great", "awesome", "fantastic", "clear", "helpful", "best",
            "amazing", "subscribed", "clean", "thanks", "thank you", "learned", "pacing"
        }
        self.negative_words = {
            "bad", "terrible", "flop", "quiet", "confusing", "skipped", "stuck", "error",
            "issue", "dislike", "boring", "long", "slow", "failed"
        }

    def analyze_sentiment(self, text: str) -> float:
        """
        Returns sentiment score between -1.0 (very negative) to +1.0 (very positive).
        Zero external dependency fallback for instantaneous reliable scoring.
        """
        words = re.findall(r"\b\w+\b", text.lower())
        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)
        total = pos_count + neg_count

        if total == 0:
            return 0.5 # Neutral baseline
        score = (pos_count - neg_count) / total
        return round(score, 2)

    def extract_content_gaps(self, comments: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Mines viewer comments for questions and topics that the creator hasn't published yet.
        """
        if comments is None:
            comments = COMMENTS_DATASET

        published_titles = [v["title"].lower() for v in RECENT_VIDEOS]
        gaps = []

        for c in comments:
            text = c["text"]
            is_question = any(p.search(text) for p in self.question_patterns) or "?" in text
            
            if is_question:
                # Extract clean topic suggestion
                clean_topic = text
                suggested_title = "Complete Guide: " + text.split("?")[0].strip()
                
                if "jwt" in text.lower() or "auth" in text.lower():
                    clean_topic = "FastAPI JWT & Refresh Token Authentication"
                    suggested_title = "FastAPI Authentication Masterclass: JWTs, Refresh Tokens & Security"
                elif "deploy" in text.lower() or "aws" in text.lower():
                    clean_topic = "Deploying FastAPI & React to AWS / Render for Free"
                    suggested_title = "How to Deploy Fullstack Web Apps for Free (Render, Vercel & AWS)"
                elif "cors" in text.lower():
                    clean_topic = "Fixing CORS Policy Errors in React & FastAPI"
                    suggested_title = "Fixing CORS in 5 Minutes (React, FastAPI & Express)"
                elif "next.js" in text.lower() or "server actions" in text.lower():
                    clean_topic = "Next.js 15 Server Actions with Python Backend"
                    suggested_title = "Connecting Next.js 15 Server Actions to a Python FastAPI Backend"
                elif "chromadb" in text.lower() or "vector" in text.lower():
                    clean_topic = "ChromaDB Vector Database with FastAPI Semantic Search"
                    suggested_title = "Build a Vector Search Engine with ChromaDB & FastAPI"
                elif "celery" in text.lower() or "apscheduler" in text.lower():
                    clean_topic = "Background Jobs: Celery vs APScheduler vs Redis Queue"
                    suggested_title = "Celery vs APScheduler: Which Background Task Queue to Pick?"
                elif "docker networking" in text.lower():
                    clean_topic = "Docker Container Networking & Multi-Container Apps"
                    suggested_title = "Docker Networking Explained Simply: Containers, Bridges & Compose"
                elif "websocket" in text.lower():
                    clean_topic = "Real-Time WebSockets in Python and React"
                    suggested_title = "Real-Time Chat & Notifications with WebSockets in FastAPI"

                # Check if published
                is_already_covered = any(clean_topic.lower() in t for t in published_titles)

                if not is_already_covered:
                    gaps.append({
                        "topic": clean_topic,
                        "sample_comment": text,
                        "request_count": c.get("likes", 10) + 15,
                        "urgency": "High" if c.get("likes", 0) > 50 else "Medium",
                        "suggested_title": suggested_title
                    })

        # Deduplicate by topic and sort by request popularity
        unique_gaps = {}
        for g in gaps:
            if g["topic"] not in unique_gaps:
                unique_gaps[g["topic"]] = g
            else:
                unique_gaps[g["topic"]]["request_count"] += g["request_count"]

        sorted_gaps = sorted(unique_gaps.values(), key=lambda x: x["request_count"], reverse=True)
        return sorted_gaps[:5]

nlp_service = NLPService()
