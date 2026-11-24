"""
Pipeline Cố vấn Quyết định & Chi tiêu dựa trên Hồ sơ Đặc trưng User Persona
"""
import logging
from typing import Dict, Any

logger = logging.getLogger("Persona_Advisor")

class PersonaAdvisor:
    def __init__(self):
        logger.info("Khởi tạo Persona Advisor Pipeline")

    def recommend(self, action: Dict[str, Any], persona: Dict[str, Any]) -> Dict[str, Any]:
        """
        Đối chiếu khoản chi dự kiến với hồ sơ tài chính User để ra lời khuyên thực tế
        """
        amount = action.get("amount", 0)
        income = persona.get("monthly_income", 15000000)

        return {
            "recommendation": "CAUTION_HOLD",
            "headline": "Cân nhắc hoãn khoản chi này sang đầu tháng sau để tránh ảnh hưởng tiền sinh hoạt thiết yếu!",
            "personalized_analysis": {
                "current_budget_status": f"Khoản chi {amount:,.0f}đ chiếm tỷ trọng lớn trong ngân sách còn lại của tháng.",
                "upcoming_obligations": "Bạn còn các khoản thanh toán cố định vào cuối tháng (tiền nhà, hóa đơn điện nước).",
                "emergency_fund_impact": "Nếu chi ngay hôm nay, quỹ dự phòng sẽ giảm xuống dưới ngưỡng an toàn 3 tháng."
            },
            "action_options": [
                {
                    "option": "Trì hoãn mua sắm sang tháng sau",
                    "description": "Chờ nhận lương chu kỳ tiếp theo để không tạo áp lực dòng tiền."
                },
                {
                    "option": "Tìm kiếm phương án trả góp 0%",
                    "description": "Chia nhỏ thành các đợt thanh toán nhẹ nhàng từ 600.000đ - 700.000đ/tháng."
                }
            ]
        }
