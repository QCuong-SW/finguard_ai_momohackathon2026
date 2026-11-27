"""
Controller (FastAPI Router) cho Feature Scam Intelligence.
"""
from fastapi import APIRouter

from features.scam.schema import ScamAnalyzeRequest, ScamAnalyzeResponse
from features.scam.service import ScamService

router = APIRouter(prefix="/api/v1/ai/scam", tags=["Scam Intelligence"])
_service = ScamService()


@router.post("/analyze", response_model=ScamAnalyzeResponse)
def analyze_scam(req: ScamAnalyzeRequest) -> ScamAnalyzeResponse:
    return _service.analyze(req)
