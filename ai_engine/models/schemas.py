from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ScamAnalyzeRequest(BaseModel):
    type: str = Field(..., description="TEXT, IMAGE, hoặc URL")
    content: str = Field(..., description="Nội dung cần phân tích")
    context: Optional[str] = Field(None, description="Ngữ cảnh phụ (tin nhắn từ số lạ, group chat...)")

class ScamAnalyzeResponse(BaseModel):
    risk_score: int
    risk_level: str
    summary: str
    psychological_manipulation: List[Dict[str, str]]
    url_analysis: Optional[Dict[str, Any]] = None
    actionable_checklist: List[str]

class RagAnalyzeRequest(BaseModel):
    doc_name: str
    text: Optional[str] = ""

class RagAnalyzeResponse(BaseModel):
    doc_name: str
    risk_rating: str
    summary: str
    hidden_traps: List[Dict[str, str]]
    suggested_questions: List[str]

class AdvisorRequest(BaseModel):
    action: Dict[str, Any]
    persona: Dict[str, Any]

class AdvisorResponse(BaseModel):
    recommendation: str
    headline: str
    personalized_analysis: Dict[str, str]
    action_options: List[Dict[str, str]]
