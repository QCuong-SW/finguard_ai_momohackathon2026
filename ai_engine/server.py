"""
FinGuard AI Engine - Internal FastAPI Microservice (Package-by-Feature + Read-Only Fixed RAG)
Được gọi từ NestJS Backend qua AiBridgeService.
"""
import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.llm_client import llm_client
from core.vector_store import vector_store
from features.advisor.controller import router as advisor_router
from features.contract_rag.controller import router as contract_rag_router
from features.scam.controller import router as scam_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("FinGuardAIEngine")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Đảm bảo kho tri thức cố định (Read-Only KB) sẵn sàng trước khi nhận request."""
    vector_store.ensure_ready()
    logger.info(
        "FinGuard AI Engine ready | rag_backend=%s | gemini_ready=%s | model=%s",
        vector_store.backend,
        llm_client.is_ready,
        llm_client.model,
    )
    yield


app = FastAPI(
    title="FinGuard AI Engine",
    description=(
        "Microservice xử lý AI (Gemini API, Read-Only Fixed Domain RAG, XAI) "
        "theo kiến trúc Package-by-Feature cho FinGuard AI"
    ),
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount các Feature Routers (tuyệt đối không expose endpoint ghi/xóa KB ra ngoài)
app.include_router(scam_router)
app.include_router(contract_rag_router)
app.include_router(advisor_router)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "FinGuard AI Engine",
        "ready": True,
        "rag_mode": "read-only-fixed-kb",
        "rag_backend": vector_store.backend,
        "gemini_ready": llm_client.is_ready,
        "gemini_model": llm_client.model,
    }


if __name__ == "__main__":
    port = int(os.getenv("AI_ENGINE_PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
