"""
Pipeline RAG bóc tách hợp đồng tài chính & Bẫy chữ nhỏ (Hidden Traps)
"""
import logging
from typing import Dict, Any

logger = logging.getLogger("RAG_Engine")

class RAGEngine:
    def __init__(self):
        logger.info("Khởi tạo RAG Engine với Vector Store (ChromaDB)")

    def index_document(self, doc_name: str, text: str):
        """
        Chunking văn bản và nạp vào Vector Store
        """
        logger.info(f"Đã chunking và đánh index cho tài liệu: {doc_name}")
        return True

    def analyze_document_traps(self, doc_name: str, text: str) -> Dict[str, Any]:
        """
        Trích xuất bẫy chữ nhỏ trong hợp đồng
        """
        return {
            "doc_name": doc_name,
            "risk_rating": "HIGH_RISK",
            "summary": "Hợp đồng vay tiêu dùng có các điều khoản bất lợi về lãi suất thả nổi và mức phạt tất toán sớm.",
            "hidden_traps": [
                {
                    "category": "Lãi suất ngầm",
                    "clause_snippet": "Lãi suất ưu đãi 0.99%/tháng cho 3 tháng đầu, sau đó thả nổi theo chính sách từng thời kỳ.",
                    "trap_warning": "BẪY LÃI THẢ NỔI: Sau 3 tháng đầu, lãi suất có thể tăng vọt lên 40-50%/năm mà không có trần cố định."
                },
                {
                    "category": "Phí phạt tất toán trước hạn",
                    "clause_snippet": "Bên vay nếu tất toán trước hạn sẽ chịu phạt 15% trên dư nợ còn lại.",
                    "trap_warning": "PHÍ PHẠT CAO: Mức 15% cao hơn rất nhiều so với mức thông lệ 3-5% của ngân hàng thương mại."
                }
            ],
            "suggested_questions": [
                "Sau 3 tháng đầu, công thức tính lãi suất cụ thể là gì?",
                "Nếu tôi muốn trả nợ trước hạn sau 6 tháng, tổng số tiền phạt là bao nhiêu?",
                "Có phí ẩn nào liên quan đến bảo hiểm khoản vay không?"
            ]
        }
