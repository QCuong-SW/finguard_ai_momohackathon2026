"""
Cấu hình trung tâm cho FinGuard AI Engine (Gemini API + Read-Only Fixed Domain RAG).
"""
import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

# Nạp .env từ thư mục gốc repo hoặc thư mục ai_engine/
AI_ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = AI_ENGINE_DIR.parent

load_dotenv(REPO_ROOT / ".env")
load_dotenv(AI_ENGINE_DIR / ".env", override=True)

_PLACEHOLDER_KEYS = {"", "your_gemini_api_key_here", "CHANGE_ME", "none", "null"}


@dataclass(frozen=True)
class Settings:
    # Gemini API
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "").strip()
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
    gemini_temperature: float = float(os.getenv("GEMINI_TEMPERATURE", "0.2"))

    # Fixed Domain Knowledge Base & Vector Store (Read-Only ở runtime)
    knowledge_base_dir: Path = AI_ENGINE_DIR / "knowledge_base"
    scam_kb_dir: Path = AI_ENGINE_DIR / "knowledge_base" / "scam"
    finance_kb_dir: Path = AI_ENGINE_DIR / "knowledge_base" / "finance"
    vector_store_dir: Path = Path(
        os.getenv("CHROMA_PERSIST_DIR", str(AI_ENGINE_DIR / "vector_store"))
    )

    # ChromaDB Collections cố định
    scam_collection_name: str = "scam_domain_kb"
    finance_collection_name: str = "finance_rules_kb"

    # Retrieval defaults
    default_top_k: int = int(os.getenv("RAG_TOP_K", "4"))

    @property
    def is_gemini_configured(self) -> bool:
        return self.gemini_api_key.lower() not in _PLACEHOLDER_KEYS


settings = Settings()
