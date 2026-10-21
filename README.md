# CreatorPilot 🚀
### Autonomous AI Growth Coach & Decision Engine for Content Creators

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Time--Series%20Forecasting-FF6F00?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-Comment%20Mining-4B8BBE?style=flat&logo=python&logoColor=white)](https://www.nltk.org/)
[![Web Speech API](https://img.shields.io/badge/Voice-Web%20Speech%20API-7952B3?style=flat&logo=googlechrome&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
[![Architecture](https://img.shields.io/badge/Architecture-MVC%20Enterprise-blueviolet?style=flat)]()

---

## 📌 1. Project Overview & The Industry Problem

Existing creator analytics platforms (**Social Blade, VidIQ, TubeBuddy, YouTube Studio**) suffer from a major design flaw: **they are passive dashboards**. They present overwhelming graphs, leaving creators paralyzed with questions like:
- *"Why did my last video flop?"*
- *"What specific tutorial is my audience asking for?"*
- *"When will I finally reach 4,000 watch hours to monetize?"*

**CreatorPilot** transforms creator tooling from a passive observer into an **active, proactive AI coach** (a Siri-like personal manager). It analyzes historical upload cadences, flags retention drop-offs, mines comment threads for untapped video ideas, predicts 30-day subscriber growth, and speaks actionable advice directly to the creator.

---

## 🏛️ 2. Enterprise Model-View-Controller (MVC) Architecture

The application strictly separates data models, business logic controllers, and interactive presentation views:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        VIEW LAYER (React / HTML5)                      │
│   Analytics Dash | Growth Chart | Idea Vault | Collab Matcher | Voice  │
└───────────────────▲────────────────────────────────┬───────────────────┘
                    │ JSON Contracts                 │ User Actions / Voice
                    │                                ▼
┌───────────────────┴────────────────────────────────────────────────────┐
│                    CONTROLLER LAYER (FastAPI / Hooks)                  │
│   ChannelController | MLController | GrowthController | CoachController│
└───────────────────▲────────────────────────────────┬───────────────────┘
                    │ Service Calls                  │ ORM / Persistence
                    │                                ▼
┌───────────────────┴────────────────────────────────────────────────────┐
│                        MODEL LAYER (Pydantic / DB)                     │
│   ChannelProfile | VideoMetric | ForecastResponse | IdeaVaultItem     │
└────────────────────────────────────────────────────────────────────────┘
```

### MVC Responsibilities:
1. **Model Layer (`backend/app/models/`)**:
   - `channel_model.py`: Domain entities for channel statistics, retention hooks, and notification alerts.
   - `prediction_model.py`: Schemas for Prophet time-series forecasts and title click-potential scores.
   - `growth_model.py`: Data contracts for the Idea Vault, Collab Matcher, and Content Gap items.
   - `chat_model.py`: Conversational memory schemas and voice synthesis payloads.

2. **Controller Layer (`backend/app/controllers/`)**:
   - `channel_controller.py`: Computes composite Health Scores and fires proactive upload gap / burnout alerts.
   - `ml_controller.py`: Fits regression models to forecast 30-day subscriber trajectories and analyzes CTR potential.
   - `growth_controller.py`: Orchestrates audience comment mining, Idea Vault prioritization, and peer collab matching.
   - `coach_controller.py`: Manages the contextual LLM agent, channel memory injection, and speech responses.

3. **View Layer (`frontend/src/components/`)**:
   - Decoupled from direct API calls using the `useCreatorPilot` controller hook (`frontend/src/controllers/useCreatorPilot.js`).
   - Renders responsive analytics, Recharts area curves, interactive modals, and real-time audio visualizers.

---

## 🌟 3. Real-World Features & Problem Solutions

| Feature | The Real Creator Problem | How CreatorPilot Solves It |
| :--- | :--- | :--- |
| **🎙️ Voice AI Coach (Siri for Creators)** | Analytics dashboards don't talk, requiring manual interpretation. | Zero-latency speech recognition (`STT`) and browser speech synthesis (`TTS`) that answers *"Why did my last video flop?"* with real diagnostic data. |
| **💡 Idea Vault & AI Prioritizer** | Creators write ideas in scattered notes and struggle to pick what to film. | Ranks ideas by **`0–100 Predicted Score`** and tags them by **`Production Effort`** *(Low: 1-2h vs. High: Deep Dive)*. |
| **🤝 Peer Collab Matcher** | Channels hit growth plateaus when confined to their own audience. | Scans for creators in the same niche with **similar subscriber counts (15k–45k)** and generates custom cross-promotional video pitches. |
| **📉 Drop-Off Hook Diagnosis** | High early drop-offs (40%+) destroy YouTube recommendation velocity. | Benchmarks early viewer retention against the **65% industry standard** and prescribes actionable intro edits. |
| **🔍 Audience Content Gap Finder** | Creators run out of video ideas despite viewers constantly asking questions. | NLP regex & semantic clustering scans comment threads for unanswered questions that have never been covered in published videos. |
| **⏰ Trend Decay Timer** | Creators jump on trends too late, after search momentum has died down. | Tracks search volume velocity ($dV/dt$) and provides an expiration countdown *(e.g. "Peak fading in 14 days")*. |
| **🎯 Monetization Readiness Tracker** | Unclear milestone tracking toward the 4,000 watch hours YPP requirement. | Calculates exact daily watch hour deficits and prescribes targeted high-yield live streams and playlist bundles. |
| **📊 Pre-Publish Title Scorer** | Guessing video titles results in poor initial Click-Through Rate (CTR). | Evaluates character length (optimal 45-65 chars), power words, emotional curiosity hooks, and clickbait risk. |

---

## 📂 4. Project Directory Tree

```
creator-pilot/
├── backend/                             # Python / FastAPI MVC Backend
│   ├── app/
│   │   ├── models/                      # [M] Pydantic Domain Models
│   │   │   ├── channel_model.py
│   │   │   ├── prediction_model.py
│   │   │   ├── growth_model.py
│   │   │   └── chat_model.py
│   │   ├── controllers/                 # [C] API Routers & Controllers
│   │   │   ├── channel_controller.py
│   │   │   ├── ml_controller.py
│   │   │   ├── growth_controller.py
│   │   │   └── coach_controller.py
│   │   ├── services/                    # Core Analytical & ML Engines
│   │   │   ├── youtube_service.py       # API client & mock dataset fallback
│   │   │   ├── ml_service.py            # Time-Series Regressor & Title Scorer
│   │   │   ├── nlp_service.py           # Comment question miner & Sentiment
│   │   │   ├── idea_vault_service.py    # Idea prioritizer by effort/score
│   │   │   ├── collab_service.py        # Cosine similarity niche matcher
│   │   │   └── coach_service.py         # LLM agent with context memory
│   │   ├── config.py                    # Environment settings
│   │   └── main.py                      # FastAPI entrypoint with CORS
│   ├── demo_data.py                     # Realistic offline dataset for viva demo
│   ├── requirements.txt                 # Backend dependencies
│   ├── .env                             # Active environment configuration
│   └── .env.example
│
├── frontend/                            # React / Vite / Tailwind MVC Client
│   ├── src/
│   │   ├── controllers/                 # [C] Frontend Controller Hooks
│   │   │   └── useCreatorPilot.js       # State orchestration & API client
│   │   ├── components/                  # [V] Pure Presentation Views
│   │   │   ├── Navbar.jsx
│   │   │   ├── NotificationBanner.jsx
│   │   │   ├── MetricsOverview.jsx
│   │   │   ├── GrowthForecastChart.jsx
│   │   │   ├── IdeaVaultView.jsx        # 💡 Idea Vault Backlog
│   │   │   ├── CollabMatcherView.jsx    # 🤝 Peer Collab Matcher
│   │   │   ├── ContentGapFinder.jsx
│   │   │   ├── TrendIntelligence.jsx
│   │   │   ├── AICoachModal.jsx         # 🎙️ Voice & Chat Modal
│   │   │   ├── TitleScorerModal.jsx
│   │   │   └── WeeklyPlanModal.jsx
│   │   ├── App.jsx                      # Main View Coordinator
│   │   ├── main.jsx                     # Root React DOM entry
│   │   └── index.css                    # Tailwind design system
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── .vscode/
│   └── tasks.json                       # VS Code 1-click execution tasks
├── START_LOCALHOST.bat                  # 🚀 Master 1-Click Localhost Launcher (Port 8080)
├── start_server.ps1                     # Native Windows socket server (Zero external dependencies)
├── index.html                           # Unified localhost entrypoint
└── preview_dashboard.html               # Standalone direct-file preview
```

---

## ⚡ 5. Quick Start & Localhost Execution

### 🌟 Method 1: The Master Launcher (Recommended)
1. Open your File Explorer to `c:\creator pilot`.
2. Double-click **`START_LOCALHOST.bat`**.
3. It auto-detects Python, Node.js, or uses the native Windows server, and automatically launches your browser:
   👉 **`http://localhost:8080`**

---

### 💻 Method 2: VS Code 1-Click Task
1. Open `c:\creator pilot` in VS Code (`code "c:\creator pilot"`).
2. Press **`Ctrl + Shift + B`** *(or click **Terminal** → **Run Build Task...**)*.
3. Select **`1. Run Localhost (Port 8080 - Auto Fallback)`**.

---

### 🛠️ Method 3: Manual Client-Server Execution

#### Terminal 1 — Start the Python FastAPI Backend:
```powershell
cd "c:\creator pilot\backend"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
> **Backend Docs:** 👉 `http://localhost:8000/docs`

#### Terminal 2 — Start the React Frontend:
```powershell
cd "c:\creator pilot\frontend"
npm install
npm run dev
```
> **Frontend App:** 👉 `http://localhost:5173`

---

## 📐 6. Mathematical & Algorithmic Formulations

### 1. Growth Health Score (0–100)
$$\text{Health Score} = 0.40 \times C_{\text{consistency}} + 0.35 \times E_{\text{engagement}} + 0.25 \times T_{\text{trend\_alignment}}$$
* Where $C_{\text{consistency}}$ is penalized when $(t_{\text{now}} - t_{\text{last\_upload}}) > \text{Target Interval}$.
* Where $E_{\text{engagement}} = \frac{\text{Average Views}}{\text{Total Subscribers}} \times 100$.

### 2. Niche Trend-Fit Score
$$\text{Fit Score} = \left( \frac{\vec{E}_{\text{niche}} \cdot \vec{E}_{\text{trend}}}{\|\vec{E}_{\text{niche}}\| \|\vec{E}_{\text{trend}}\|} \right) \times 100$$
* Matches creator niche embeddings against trending Google search velocity.

### 3. Time-Series Predictive Extrapolation
$$\hat{y}(t) = \beta_0 + \beta_1 t + \epsilon_t, \quad \text{CI}_{95\%} = \hat{y}(t) \pm 1.96 \cdot \sigma \sqrt{t}$$
* Extrapolates future subscriber trajectory with an expanding confidence interval over a 30-day horizon.

---

## 📡 7. API Specification (Backend Routes)

| Method | Endpoint | Controller | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/channel/summary` | `ChannelController` | Real-time subscriber count, watch hours, and Health Score breakdown. |
| `GET` | `/api/channel/notifications` | `ChannelController` | Proactive alerts: Upload Gap warning, streak risk, peak posting hour. |
| `GET` | `/api/ml/growth-forecast` | `MLController` | 30-day forecast with 95% upper and lower confidence bounds. |
| `POST` | `/api/ml/score-title` | `MLController` | Predicts CTR rating (0-100), letter grade (A-D), and clickbait risk. |
| `GET` | `/api/ml/hook-diagnostics` | `MLController` | Analyzes first 30s viewer drop-off against the 65% retention baseline. |
| `GET` | `/api/growth/idea-vault` | `GrowthController` | Backlog of ranked video ideas categorized by production effort. |
| `POST` | `/api/growth/idea-vault` | `GrowthController` | Adds and auto-scores a new video concept. |
| `GET` | `/api/growth/collab-matcher`| `GrowthController` | Finds creators in the same niche (15k–45k subs) with collaboration pitches. |
| `GET` | `/api/growth/content-gaps` | `GrowthController` | Audience questions mined from comments not yet covered in catalog. |
| `GET` | `/api/growth/monetization-sprint`| `GrowthController`| 14-day watch hour sprint plan toward YPP ad approval. |
| `POST` | `/api/coach/chat` | `CoachController` | Siri-like strategic manager chat with memory and voice synthesis text. |


---

## ⚙️ 8. Configuration & Environment Variables

The backend supports configuration via `backend/.env`. A template is provided at `backend/.env.example`:

```ini
# Environment Mode
ENVIRONMENT=development

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True

# YouTube Data API v3 (Optional - falls back to demo_data.py if empty)
YOUTUBE_API_KEY=

# LLM Provider Key (Optional - falls back to internal rule-based coach if empty)
OPENAI_API_KEY=
GEMINI_API_KEY=

# Channel Defaults
DEFAULT_CHANNEL_ID=UC_creator_demo_01
MONETIZATION_HOURS_TARGET=4000
MONETIZATION_SUBS_TARGET=1000
```

---

## 🛠️ 9. Troubleshooting & Common Fixes

| Symptom / Error | Root Cause | Solution |
| :--- | :--- | :--- |
| **`ERR_CONNECTION_REFUSED`** on `localhost:8080` | No local background server is actively listening on port 8080. | Double-click **`START_LOCALHOST.bat`** or run VS Code Task **`1. Run Localhost`** (`Ctrl + Shift + B`). Keep the command window open. |
| **Microphone not working in Voice Coach** | Modern browsers restrict `webkitSpeechRecognition` on raw `file:///` URLs. | Access the app via **`http://localhost:8080`** rather than opening the file directly. When prompted, click **Allow** for microphone access. |
| **`Address already in use` (Port 8080)** | Another process (e.g. previous server instance) is holding port 8080. | Close existing terminal windows running the server, or run `netstat -ano | findstr 8080` in PowerShell and terminate the matching PID. |
| **FastAPI Backend missing modules** | Python packages not installed in virtual environment. | Run `cd backend; pip install -r requirements.txt`. |

---
