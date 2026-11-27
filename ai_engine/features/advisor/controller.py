"""
Controller (FastAPI Router) cho Feature Persona Financial Advisor.
"""
from fastapi import APIRouter

from features.advisor.schema import AdvisorRequest, AdvisorResponse
from features.advisor.service import AdvisorService

router = APIRouter(prefix="/api/v1/ai/advisor", tags=["Persona Financial Advisor"])
_service = AdvisorService()


@router.post("/recommend", response_model=AdvisorResponse)
def recommend_advice(req: AdvisorRequest) -> AdvisorResponse:
    return _service.recommend(req)
