"""
Service nghiệp vụ cho Feature Persona Decision Advisor.
Kết hợp dữ liệu User Persona + Hành động dự kiến + Quy tắc tài chính cố định từ `finance_rules_kb`.
"""
from typing import Optional

from core.llm_client import llm_client
from features.advisor.prompt import ADVISOR_SYSTEM_PROMPT, build_advisor_user_prompt
from features.advisor.repository import AdvisorRepository
from features.advisor.schema import (
    ActionOption,
    AdvisorRequest,
    AdvisorResponse,
    PersonalizedAnalysis,
)


class AdvisorService:
    def __init__(self, repository: Optional[AdvisorRepository] = None):
        self.repository = repository or AdvisorRepository()

    def recommend(self, req: AdvisorRequest) -> AdvisorResponse:
        action = req.action
        persona = req.persona

        query = (
            f"tài chính cá nhân 50/30/20 DTI quỹ dự phòng "
            f"{action.get('proposed_action', '')} {action.get('category', '')} "
            f"{action.get('notes', '')} {persona.get('risk_appetite', '')}"
        )
        kb_context, chunks = self.repository.retrieve_finance_guidelines(query, top_k=4)
        rag_refs = [f"{c.code}: {c.title}" for c in chunks]

        if llm_client.is_ready:
            user_prompt = build_advisor_user_prompt(
                action=action,
                persona=persona,
                kb_context=kb_context,
            )
            llm_result = llm_client.generate_structured(
                system_prompt=ADVISOR_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                response_schema=AdvisorResponse,
            )
            if llm_result is not None:
                if not llm_result.rag_references:
                    llm_result.rag_references = rag_refs
                return llm_result

        return self._fallback_recommend(action, persona, rag_refs)

    def _fallback_recommend(
        self, action: dict, persona: dict, rag_refs: list[str]
    ) -> AdvisorResponse:
        amount = float(action.get("amount", 0) or 0)
        income = float(persona.get("monthly_income", 15_000_000) or 15_000_000)
        safe_limit = float(persona.get("safe_spending_limit", income * 0.3) or income * 0.3)
        ratio = (amount / safe_limit) if safe_limit > 0 else 1.0

        if ratio <= 0.5:
            rec = "PROCEED"
            headline = "Khoản chi nằm trong ngưỡng an toàn, bạn có thể tiến hành."
            budget_msg = f"Khoản chi {amount:,.0f}đ chỉ chiếm khoảng {ratio*100:.0f}% hạn mức chi tiêu an toàn ({safe_limit:,.0f}đ)."
            ef_msg = "Không làm ảnh hưởng tới quỹ dự phòng khẩn cấp 3–6 tháng sinh hoạt."
            options = [
                ActionOption(
                    option="Thanh toán trực tiếp",
                    description="Giữ lại phần dư để bổ sung vào mục tiêu tiết kiệm 20% hàng tháng.",
                )
            ]
        elif ratio <= 1.2:
            rec = "CAUTION_HOLD"
            headline = "Cân nhắc hoãn khoản chi này sang chu kỳ lương sau để tránh hụt ngân sách thiết yếu!"
            budget_msg = f"Khoản chi {amount:,.0f}đ chiếm tới {ratio*100:.0f}% hạn mức an toàn ({safe_limit:,.0f}đ) của tháng."
            ef_msg = "Nếu chi ngay, quỹ dự phòng khẩn cấp có nguy cơ giảm xuống dưới ngưỡng an toàn 3 tháng."
            options = [
                ActionOption(
                    option="Trì hoãn sau ngày nhận lương",
                    description="Chờ sang chu kỳ thu nhập mới để không ảnh hưởng tiền thuê nhà và hóa đơn cuối tháng.",
                ),
                ActionOption(
                    option="Chia nhỏ trả góp 0% (không phí chuyển đổi)",
                    description="Giữ tổng nghĩa vụ trả góp hàng tháng dưới ngưỡng an toàn DTI 35% thu nhập.",
                ),
            ]
        else:
            rec = "STRONGLY_DISCOURAGED"
            headline = "Khuyến cáo KHÔNG NÊN chi khoản này ngay lúc này — vượt xa ngưỡng an toàn tài chính!"
            budget_msg = f"Khoản chi {amount:,.0f}đ vượt mức hạn mức chi tiêu an toàn ({safe_limit:,.0f}đ) tới {ratio*100:.0f}%."
            ef_msg = "Có nguy cơ rút cạn quỹ dự phòng khẩn cấp và gây mất cân đối dòng tiền cuối tháng."
            options = [
                ActionOption(
                    option="Tạm dừng & tích lũy theo mục tiêu",
                    description="Trích 15–20% thu nhập mỗi tháng vào quỹ riêng cho đến khi đủ tiền mặt.",
                ),
                ActionOption(
                    option="Chọn phương án có chi phí thấp hơn",
                    description="Cân nhắc sản phẩm/dịch vụ phù hợp với ngân sách thực tế hiện tại.",
                ),
            ]

        return AdvisorResponse(
            recommendation=rec,
            headline=headline,
            personalized_analysis=PersonalizedAnalysis(
                current_budget_status=budget_msg,
                upcoming_obligations="Ưu tiên thanh toán các khoản cố định cuối tháng (tiền nhà, điện nước, hóa đơn định kỳ) trước khi chi mua sắm.",
                emergency_fund_impact=ef_msg,
            ),
            action_options=options,
            rag_references=rag_refs,
        )
