"""
Realistic pre-seeded dataset for CreatorPilot demonstration.
Enables full end-to-end functionality even without an active YouTube API quota.
"""

from datetime import datetime, timedelta

CHANNEL_INFO = {
    "channel_id": "UC_demo_codecraft_99",
    "channel_name": "CodeCraft Studio",
    "handle": "@codecraftstudio",
    "niche": "Web Development & AI Engineering",
    "avatar_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=150&auto=format&fit=crop&q=80",
    "subscriber_count": 28450,
    "total_views": 1845000,
    "video_count": 86,
    "watch_time_hours": 3480, # Monetization readiness: 3480 / 4000
    "monetization_sub_target": 1000,
    "monetization_watch_target": 4000,
    "current_streak_weeks": 4,
    "last_upload_days_ago": 6,
    "target_frequency_days": 5,
}

# 60 days of historical follower and view trajectory for Time-Series forecasting
def generate_historical_metrics():
    today = datetime.now()
    records = []
    base_subs = 21000
    base_views = 1350000
    
    for i in range(60, 0, -1):
        date_str = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        daily_sub_gain = 110 + (60 - i) * 2 + (i % 7) * 15
        daily_view_gain = 7800 + (60 - i) * 120 + (i % 5) * 600
        base_subs += daily_sub_gain
        base_views += daily_view_gain
        records.append({
            "date": date_str,
            "subscribers": base_subs,
            "views": base_views,
            "daily_subs": daily_sub_gain,
            "daily_views": daily_view_gain
        })
    return records

HISTORICAL_TRAJECTORY = generate_historical_metrics()

RECENT_VIDEOS = [
    {
        "video_id": "vid_101",
        "title": "Build a Full-Stack AI Chatbot with FastAPI and React in 30 Mins",
        "published_at": "6 days ago",
        "views": 18420,
        "likes": 1420,
        "comments_count": 184,
        "retention_hook_drop": 0.42, # 42% left in first 30 seconds
        "drop_reason": "Intro sequence was too long (45s) before showing demo.",
        "sentiment_score": 0.88,
        "thumbnail_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&auto=format&fit=crop&q=80"
    },
    {
        "video_id": "vid_102",
        "title": "Why You Should Stop Using Express.js in 2026 (Use This Instead)",
        "published_at": "12 days ago",
        "views": 34500,
        "likes": 2810,
        "comments_count": 420,
        "retention_hook_drop": 0.22, # Strong hook
        "drop_reason": "High retention at hook. Drop-off occurred at deep benchmark charts.",
        "sentiment_score": 0.74,
        "thumbnail_url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=400&auto=format&fit=crop&q=80"
    },
    {
        "video_id": "vid_103",
        "title": "Docker Containerization Crash Course for Complete Beginners",
        "published_at": "18 days ago",
        "views": 9800,
        "likes": 750,
        "comments_count": 92,
        "retention_hook_drop": 0.55, # Poor hook
        "drop_reason": "Title promised beginner friendly, but skipped installation steps.",
        "sentiment_score": 0.65,
        "thumbnail_url": "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=400&auto=format&fit=crop&q=80"
    },
    {
        "video_id": "vid_104",
        "title": "PostgreSQL vs MongoDB: Which Database Should You Choose?",
        "published_at": "25 days ago",
        "views": 22100,
        "likes": 1940,
        "comments_count": 210,
        "retention_hook_drop": 0.28,
        "drop_reason": "Good pacing, viewer retention remained steady until summary.",
        "sentiment_score": 0.82,
        "thumbnail_url": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=400&auto=format&fit=crop&q=80"
    }
]

# Viewer comments for NLP sentiment and Content Gap Finder
COMMENTS_DATASET = [
    {"author": "DevGamer", "text": "Loved the FastAPI breakdown! Can you please make a video on how to handle user authentication with JWT and refresh tokens?", "likes": 74},
    {"author": "SarahCodes", "text": "This was super clear. How do I deploy this stack to AWS or Render for free?", "likes": 52},
    {"author": "TechieBoi", "text": "Why did my CORS policy block the React frontend on localhost? Could you make a troubleshooting guide?", "likes": 39},
    {"author": "Alex_M", "text": "Great tutorial, but the audio was a bit quiet on the left channel.", "likes": 12},
    {"author": "Nitin_Web", "text": "Please make a full video on Next.js 15 Server Actions with Python backend!", "likes": 88},
    {"author": "CodeNewbie", "text": "Can you explain how to connect ChromaDB vector database with FastAPI for semantic search?", "likes": 64},
    {"author": "JordanDev", "text": "The pacing in the second half was fantastic, learned more in 15 mins than a 4-hour course.", "likes": 41},
    {"author": "ElenaR", "text": "Could you do a comparison between Celery vs APScheduler for background jobs?", "likes": 47},
    {"author": "Kevin99", "text": "I got stuck on the Docker networking step. How do containers communicate internally?", "likes": 31},
    {"author": "WebMasterDave", "text": "Amazing content as always! When is the tutorial on WebSockets coming?", "likes": 59}
]

# Trending topics in creator's niche with Trend-Fit score & expiry estimates
TRENDING_TOPICS = [
    {
        "topic": "Next.js 15 Server Actions & React 19",
        "category": "Frontend Frameworks",
        "fit_score": 94,
        "search_volume_velocity": "+140%",
        "expires_in_days": 14,
        "urgency": "High",
        "recommended_hook": "Why React 19 changes full-stack architecture forever"
    },
    {
        "topic": "Local LLMs with Ollama and LangChain",
        "category": "AI Engineering",
        "fit_score": 91,
        "search_volume_velocity": "+220%",
        "expires_in_days": 21,
        "urgency": "High",
        "recommended_hook": "Run deepseek locally without paying API bills"
    },
    {
        "topic": "FastAPI + Pydantic v2 Best Practices",
        "category": "Python Backend",
        "fit_score": 87,
        "search_volume_velocity": "+65%",
        "expires_in_days": 30,
        "urgency": "Medium",
        "recommended_hook": "5 mistakes backend devs make with Pydantic v2"
    },
    {
        "topic": "Supabase Vector vs Pinecone",
        "category": "Databases",
        "fit_score": 78,
        "search_volume_velocity": "+45%",
        "expires_in_days": 18,
        "urgency": "Medium",
        "recommended_hook": "Stop overpaying for vector databases"
    }
]
