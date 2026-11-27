"""
Service nghiệp vụ cho Feature Contract RAG (Stateless Hidden Traps & Legal Q&A).
- Xử lý văn bản hợp đồng hoàn toàn trong RAM, KHÔNG lưu vào ChromaDB.
- Đối chiếu với `finance_rules_kb` cố định thông qua ContractRagRepository.
"""
import logging
from typing import Optional

from core.llm_client import llm_client
from features.contract_rag.prompt import (
    CONTRACT_CHAT_SYSTEM_PROMPT,
    CONTRACT_TRAP_SYSTEM_PROMPT,
    build_contract_chat_prompt,
    build_contract_trap_prompt,
)
from features.contract_rag.repository import ContractRagRepository
from features.contract_rag.schema import (
    HiddenTrap,
    RagAnalyzeRequest,
    RagAnalyzeResponse,
    RagChatRequest,
    RagChatResponse,
)

logger = logging.getLogger("ContractRagService")


class ContractRagService:
    def __init__(self, repository: Optional[ContractRagRepository] = None):
        self.repository = repository or ContractRagRepository()

    def analyze_document(self, req: RagAnalyzeRequest) -> RagAnalyzeResponse:
        doc_text = (req.text or "").strip()
        query = doc_text[:1500] if doc_text else f"{req.doc_name} lãi suất thả nổi phí phạt tất toán"

        kb_context, chunks = self.repository.retrieve_rules(query, top_k=5)
        rag_refs = [f"{c.code}: {c.title}" for c in chunks]

        if llm_client.is_ready and doc_text:
            user_prompt = build_contract_trap_prompt(
                doc_name=req.doc_name,
                document_text=doc_text,
                kb_context=kb_context,
            )
            llm_result = llm_client.generate_structured(
                system_prompt=CONTRACT_TRAP_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                response_schema=RagAnalyzeResponse,
            )
            if llm_result is not None:
                llm_result.doc_name = req.doc_name
                if not llm_result.rag_references:
                    llm_result.rag_references = rag_refs
                return llm_result

        return self._fallback_analyze(req.doc_name, doc_text, rag_refs)

    def chat_with_document(self, req: RagChatRequest) -> RagChatResponse:
        query = f"{req.question} {req.document_text[:500]}"
        kb_context, chunks = self.repository.retrieve_rules(query, top_k=4)
        citations = [f"{c.code} ({c.source_file}): {c.title}" for c in chunks]

        if llm_client.is_ready:
            user_prompt = build_contract_chat_prompt(
                doc_name=req.doc_name,
                document_text=req.document_text,
                question=req.question,
                kb_context=kb_context,
            )
            llm_result = llm_client.generate_structured(
                system_prompt=CONTRACT_CHAT_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                response_schema=RagChatResponse,
            )
            if llm_result is not None:
                if not llm_result.citations:
                    llm_result.citations = citations
                return llm_result

        return RagChatResponse(
            answer=(
                f"[Chế độ RAG Fallback — chưa cấu hình GEMINI_API_KEY] "
                f"Hệ thống đã đối chiếu câu hỏi '{req.question}' với {len(chunks)} quy chuẩn pháp lý "
                f"trong kho tri thức cố định. Vui lòng thêm GEMINI_API_KEY vào .env để nhận câu trả lời chi tiết."
            ),
            citations=citations,
        )

    def _fallback_analyze(
        self, doc_name: str, doc_text: str, rag_refs: list[str]
    ) -> RagAnalyzeResponse:
        lower = doc_text.lower()
        traps: list[HiddenTrap] = []

        if any(k in lower for k in ("thả nổi", "từng thời kỳ", "điều chỉnh lãi suất", "ưu đãi")):
            traps.append(
                HiddenTrap(
                    category="Lãi suất ngầm",
                    clause_snippet="Điều khoản đề cập lãi suất ưu đãi ban đầu sau đó thả nổi/điều chỉnh theo chính sách từng thời kỳ.",
                    trap_warning="BẪY LÃI THẢ NỔI (TRAP-01 / TT 39/2016/TT-NHNN): Không nêu rõ công thức tham chiếu và mức trần, lãi suất thực tế có thể tăng vọt 40%–60%/năm.",
                )
            )
        if any(k in lower for k in ("tất toán", "trước hạn", "phạt", "vi phạm hợp đồng")):
            traps.append(
                HiddenTrap(
                    category="Phí tất toán trước hạn",
                    clause_snippet="Điều khoản quy định mức phí phạt khi thanh toán/tất toán trước hạn.",
                    trap_warning="PHÍ PHẠT CAO (TRAP-03): Cần đối chiếu xem mức phạt có vượt thông lệ 1%–5% của ngân hàng thương mại hay không.",
                )
            )
        if any(k in lower for k in ("danh bạ", "người thân", "đồng nghiệp", "chia sẻ dữ liệu")):
            traps.append(
                HiddenTrap(
                    category="Xâm phạm quyền riêng tư",
                    clause_snippet="Điều khoản cho phép truy cập danh bạ hoặc liên hệ người thân, đồng nghiệp.",
                    trap_warning="RỦI RO PHÁP LÝ (TRAP-05 / Nghị định 13/2023/NĐ-CP & TT 43/2016/TT-NHNN): Nghiêm cấm nhắc nợ/bôi nhọ người không có nghĩa vụ trả nợ.",
                )
            )
        if any(k in lower for k in ("bảo hiểm khoản vay", "phí quản lý", "phí chuyển đổi", "tự động gia hạn")):
            traps.append(
                HiddenTrap(
                    category="Phí ẩn / Tự động gia hạn",
                    clause_snippet="Điều khoản có đề cập phí bảo hiểm, phí chuyển đổi hoặc cơ chế tự động gia hạn.",
                    trap_warning="PHÍ ẨN (TRAP-04 / TRAP-07 / TRAP-08): Cần làm rõ số tiền thực nhận về tay và điều kiện hủy gia hạn.",
                )
            )

        if not traps and not doc_text:
            traps.append(
                HiddenTrap(
                    category="Cần bổ sung nội dung hợp đồng",
                    clause_snippet="(Văn bản đầu vào đang trống)",
                    trap_warning="Vui lòng gửi kèm nội dung text của hợp đồng để FinGuard AI đối chiếu với 12 quy chuẩn bẫy chữ nhỏ.",
                )
            )

        risk_rating = "HIGH_RISK" if len(traps) >= 2 else ("MEDIUM_RISK" if len(traps) == 1 else "LOW_RISK")
        summary = (
            f"Phát hiện {len(traps)} nhóm điều khoản cần lưu ý trong tài liệu `{doc_name}` khi đối chiếu bộ quy chuẩn pháp lý VN."
            if traps
            else f"Chưa phát hiện từ khóa bẫy chữ nhỏ rõ rệt trong `{doc_name}` (bật GEMINI_API_KEY để phân tích ngữ nghĩa sâu hơn)."
        )

        return RagAnalyzeResponse(
            doc_name=doc_name,
            risk_rating=risk_rating,
            summary=summary,
            hidden_traps=traps,
            suggested_questions=[
                "Sau thời gian ưu đãi, công thức tính lãi suất cụ thể (% theo năm) và mức trần tối đa là bao nhiêu?",
                "Nếu tất toán trước hạn hoặc chậm trả 3 ngày, tổng phí phạt được tính cụ thể thế nào?",
                "Hợp đồng có yêu cầu mua bảo hiểm khoản vay bắt buộc hay cho phép gọi điện cho người thân không?",
            ],
            rag_references=rag_refs,
        )
