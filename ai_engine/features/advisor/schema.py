"""
Schema (Pydantic) cho Feature Persona Financial Decision Advisor.
Khớp 100% hợp đồng với NestJS AiBridgeService (`POST /api/v1/ai/advisor/recommend`).
"""
from typing import Any, Dict, List, Literal
from pydantic import BaseModel, Field


class AdvisorRequest(BaseModel):
    action: Dict[str, Any] = Field(..., description="Dự định chi tiêu/vay/đầu tư (proposed_action, amount, category, notes)")
    persona: Dict[str, Any] = Field(..., description="Hồ sơ User Persona (monthly_income, safe_spending_limit, risk_appetite...)")


class PersonalizedAnalysis(BaseModel):
    current_budget_status: str
    upcoming_obligations: str
    emergency_fund_impact: str


class ActionOption(BaseModel):
    option: str
    description: str


class AdvisorResponse(BaseModel):
    recommendation: Literal["PROCEED", "CAUTION_HOLD", "STRONGLY_DISCOURAGED"]
    headline: str
    personalized_analysis: PersonalizedAnalysis
    action_options: List[ActionOption] = Field(default_factory=list)
    rag_references: List[str] = Field(
        default_factory=list,
        description="Mã quy tắc tài chính cá nhân từ finance_rules_kb đã dùng để tư vấn",
    )
