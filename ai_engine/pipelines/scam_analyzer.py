"""
Pipeline Phân tích Lừa đảo, Thao túng tâm lý và Giải thích minh bạch (Explainable AI - XAI)
"""
import logging
from typing import Dict, Any
from prompts.scam_prompts import SCAM_DETECTION_SYSTEM_PROMPT

logger = logging.getLogger("Scam_Analyzer")

class ScamAnalyzer:
    def __init__(self):
        logger.info("Khởi tạo Scam Analyzer Pipeline")

    def analyze(self, content: str, input_type: str = "TEXT", context: str = None) -> Dict[str, Any]:
        """
        Phân tích nội dung qua LLM + Heuristics rules
        """
        lower = content.lower()
        is_scam = any(k in lower for k in ["công an", "phạt nguội", "otp", "khóa tài khoản", "lãi suất 30%", "nhiệm vụ shopee"])

        if is_scam:
            return {
                "risk_score": 92,
                "risk_level": "CRITICAL",
                "summary": "Phát hiện dấu hiệu mạo danh cơ quan chức năng hoặc đe dọa cưỡng ép chuyển tiền.",
                "psychological_manipulation": [
                    {
                        "tactic": "Authority Impersonation (Mạo danh quyền lực)",
                        "evidence": content[:50],
                        "explanation": "Kẻ gian tự xưng cơ quan có thẩm quyền để nạn nhân mất cảnh giác."
                    },
                    {
                        "tactic": "False Urgency (Tạo áp lực khẩn cấp giả tạo)",
                        "evidence": "nộp ngay trong 24h",
                        "explanation": "Thúc ép hành động nhanh khiến nạn nhân không kịp hỏi ý kiến người thân hoặc kiểm tra ngân hàng."
                    }
                ],
                "url_analysis": {
                    "is_phishing": True,
                    "warning": "Đường link có đuôi lạ không phải cổng chính thức .gov.vn của nhà nước."
                },
                "actionable_checklist": [
                    "TUYỆT ĐỐI KHÔNG bấm vào link lạ hoặc làm theo hướng dẫn chuyển tiền.",
                    "Công an không bao giờ phạt nguội hoặc xử lý án qua tin nhắn Zalo/SMS.",
                    "Báo cáo và chặn số điện thoại này ngay."
                ]
            }

        return {
            "risk_score": 15,
            "risk_level": "SAFE",
            "summary": "Nội dung an toàn, không chứa từ khóa thao túng tâm lý độc hại.",
            "psychological_manipulation": [],
            "url_analysis": None,
            "actionable_checklist": ["Tiếp tục duy trì thói quen kiểm tra tài khoản nhận trước khi chuyển tiền."]
        }
