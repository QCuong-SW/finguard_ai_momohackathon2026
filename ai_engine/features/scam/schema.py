"""
Schema (Pydantic) cho Feature Scam Intelligence & XAI.
Khớp 100% hợp đồng với NestJS AiBridgeService (`POST /api/v1/ai/scam/analyze`).
"""
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class ScamAnalyzeRequest(BaseModel):
    type: str = Field(default="TEXT", description="TEXT, IMAGE, IMAGE_OCR, hoặc URL")
    content: str = Field(..., min_length=1, description="Nội dung tin nhắn, OCR text hoặc URL cần quét")
    context: Optional[str] = Field(None, description="Ngữ cảnh phụ (Zalo lạ, SMS Brandname, group chat...)")


class ManipulationTactic(BaseModel):
    tactic: str = Field(..., description="Tên chiêu thức thao túng tâm lý")
    evidence: str = Field(..., description="Đoạn trích nguyên văn từ nội dung người dùng")
    explanation: str = Field(..., description="Giải thích XAI lý do đoạn này nguy hiểm")


class UrlAnalysis(BaseModel):
    url: Optional[str] = Field(None, description="Đường link được phát hiện trong nội dung")
    is_phishing: bool = Field(..., description="Có dấu hiệu giả mạo/phishing hay không")
    domain_age_days: Optional[int] = Field(None, description="Tuổi tên miền nếu có")
    warning: str = Field(..., description="Cảnh báo chi tiết về tên miền/URL")


class ScamAnalyzeResponse(BaseModel):
    risk_score: int = Field(..., ge=0, le=100)
    risk_level: Literal["SAFE", "SUSPICIOUS", "CRITICAL"]
    summary: str
    psychological_manipulation: List[ManipulationTactic] = Field(default_factory=list)
    url_analysis: Optional[UrlAnalysis] = None
    actionable_checklist: List[str] = Field(default_factory=list)
    rag_references: List[str] = Field(
        default_factory=list,
        description="Mã tri thức cố định từ scam_domain_kb đã được dùng để đối chiếu",
    )
