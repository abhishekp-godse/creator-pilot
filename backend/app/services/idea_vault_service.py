"""
CreatorPilot - Idea Vault Service
Manages, ranks, and prioritizes content concepts by predicted performance and effort.
"""

from typing import List, Dict, Any
from backend.app.models.growth_model import IdeaVaultItem

class IdeaVaultService:
    def __init__(self):
        self._vault_store: List[Dict[str, Any]] = [
            {
                "id": "idea_1",
                "title": "FastAPI Authentication Masterclass: JWTs & Refresh Tokens",
                "source": "content_gap",
                "predicted_score": 94,
                "production_effort": "Medium (3-5h)",
                "tags": ["fastapi", "security", "jwt", "python"],
                "status": "planned"
            },
            {
                "id": "idea_2",
                "title": "Why React 19 Changes Fullstack Architecture Forever",
                "source": "trend",
                "predicted_score": 92,
                "production_effort": "Low (1-2h)",
                "tags": ["react19", "nextjs", "webdev"],
                "status": "vault"
            },
            {
                "id": "idea_3",
                "title": "Local LLM Agents with Ollama, LangChain & Python",
                "source": "trend",
                "predicted_score": 89,
                "production_effort": "High (Deep Dive)",
                "tags": ["ai", "ollama", "langchain"],
                "status": "vault"
            },
            {
                "id": "idea_4",
                "title": "Fixing CORS Policy in React and FastAPI in 5 Minutes",
                "source": "content_gap",
                "predicted_score": 85,
                "production_effort": "Low (1-2h)",
                "tags": ["cors", "troubleshooting", "quicktip"],
                "status": "vault"
            }
        ]

    def get_all_ideas(self) -> List[IdeaVaultItem]:
        # Sort by predicted impact score
        sorted_ideas = sorted(self._vault_store, key=lambda x: x["predicted_score"], reverse=True)
        return [IdeaVaultItem(**item) for item in sorted_ideas]

    def add_idea(self, title: str, source: str = "user", effort: str = "Medium (3-5h)") -> IdeaVaultItem:
        # Heuristic scoring based on title strength
        score = 75
        if any(w in title.lower() for w in ["how to", "why", "stop", "masterclass", "vs", "crash course"]):
            score += 15
        if len(title) > 35:
            score += 5
        score = min(98, score)

        new_item = {
            "id": f"idea_{len(self._vault_store) + 1}",
            "title": title,
            "source": source,
            "predicted_score": score,
            "production_effort": effort,
            "tags": ["custom"],
            "status": "vault"
        }
        self._vault_store.append(new_item)
        return IdeaVaultItem(**new_item)

idea_vault_service = IdeaVaultService()
