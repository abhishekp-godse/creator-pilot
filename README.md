# CreatorPilot 🚀
### AI Growth Coach & Decision Engine for Content Creators

CreatorPilot is an agentic AI assistant designed to monitor upload activity, forecast growth, uncover audience content gaps, analyze trending topics, and proactively coach creators to grow their audience.

---

## 📁 Project Structure

```
creator-pilot/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI App entrypoint
│   │   ├── config.py              # Environment & App Settings
│   │   ├── models/                # Data schemas (Pydantic / DB)
│   │   │   ├── __init__.py
│   │   │   └── schemas.py
│   │   ├── services/              # Core Intelligence & Ingestion
│   │   │   ├── __init__.py
│   │   │   ├── youtube_service.py # YouTube Data API v3 integration
│   │   │   ├── ml_service.py      # Growth Forecast (Prophet) & Title Scorer
│   │   │   ├── nlp_service.py     # Sentiment Analysis & Content Gap Finder
│   │   │   └── coach_service.py   # AI Conversational Coach (LLM + Context)
│   │   └── routers/               # API Endpoints
│   │       ├── __init__.py
│   │       ├── analytics.py       # Channel metrics & Health Score
│   │       ├── ml.py              # Predictions & Forecasts
│   │       ├── trends.py          # Trend Intelligence
│   │       ├── coach.py           # Chat & Voice Assistant
│   │       └── growth_plan.py     # Content Gap & Weekly Plan
│   ├── requirements.txt           # Python dependencies
│   ├── demo_data.py               # Pre-populated live demo dataset
│   └── .env.example               # Environment variables template
│
└── frontend/                      # Web Client Dashboard & Voice Interface
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    ├── postcss.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css
        └── components/
            ├── Navbar.jsx
            ├── MetricsOverview.jsx
            ├── GrowthForecastChart.jsx
            ├── ContentGapFinder.jsx
            ├── TrendIntelligence.jsx
            ├── WeeklyGrowthPlan.jsx
            └── AICoachVoiceModal.jsx
```
