"""
Schema (Pydantic) cho Feature Contract RAG (Bóc tách Bẫy chữ nhỏ & Q&A Hợp đồng).
Khớp 100% hợp đồng với NestJS AiBridgeService (`POST /api/v1/ai/rag/analyze-doc`)
và mở rộng thêm `POST /api/v1/ai/rag/chat` hoàn toàn Stateless (không ghi tài liệu user vào ChromaDB).
"""
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class RagAnalyzeRequest(BaseModel):
    doc_name: str = Field(..., min_length=1, description="Tên file tài liệu/hợp đồng")
    text: Optional[str] = Field(default="", description="Nội dung văn bản hợp đồng (xử lý tạm trong RAM)")


class HiddenTrap(BaseModel):
    category: str = Field(..., description="Nhóm bẫy (Lãi suất ngầm, Phí tất toán trước hạn, Quyền riêng tư...)")
    clause_snippet: str = Field(..., description="Đoạn trích chính xác từ hợp đồng người dùng")
    trap_warning: str = Field(..., description="Cảnh báo rủi ro và đối chiếu quy chuẩn/pháp luật VN")


class RagAnalyzeResponse(BaseModel):
    doc_name: str
    risk_rating: Literal["LOW_RISK", "MEDIUM_RISK", "HIGH_RISK"]
    summary: str
    hidden_traps: List[HiddenTrap] = Field(default_factory=list)
    suggested_questions: List[str] = Field(default_factory=list)
    rag_references: List[str] = Field(
        default_factory=list,
        description="Mã điều luật / danh mục bẫy từ finance_rules_kb đã dùng để đối chiếu",
    )


class RagChatRequest(BaseModel):
    doc_name: str = Field(..., min_length=1)
    document_text: str = Field(..., min_length=1, description="Nội dung hợp đồng (stateless từ RAM/Backend)")
    question: str = Field(..., min_length=1, description="Câu hỏi người dùng về hợp đồng")


class RagChatResponse(BaseModel):
    answer: str
    citations: List[str] = Field(
        default_factory=list,
        description="Các đoạn trích từ hợp đồng và quy chuẩn pháp lý làm căn cứ trả lời",
    )
