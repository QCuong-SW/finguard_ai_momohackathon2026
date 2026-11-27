"""
Controller (FastAPI Router) cho Feature Contract RAG.
"""
from fastapi import APIRouter

from features.contract_rag.schema import (
    RagAnalyzeRequest,
    RagAnalyzeResponse,
    RagChatRequest,
    RagChatResponse,
)
from features.contract_rag.service import ContractRagService

router = APIRouter(prefix="/api/v1/ai/rag", tags=["Contract RAG (Read-Only KB)"])
_service = ContractRagService()


@router.post("/analyze-doc", response_model=RagAnalyzeResponse)
def analyze_document(req: RagAnalyzeRequest) -> RagAnalyzeResponse:
    return _service.analyze_document(req)


@router.post("/chat", response_model=RagChatResponse)
def chat_document(req: RagChatRequest) -> RagChatResponse:
    return _service.chat_with_document(req)
