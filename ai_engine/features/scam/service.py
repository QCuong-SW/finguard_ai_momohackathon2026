"""
Service nghiệp vụ cho Feature Scam Intelligence:
1. Trích xuất & kiểm tra URL Heuristics (TLD rủi ro, giả mạo .gov.vn / thương hiệu).
2. Truy xuất tri thức cố định từ `scam_domain_kb` qua ScamRepository.
3. Gọi Gemini LLM với Structured Output (Pydantic); tự động fallback có căn cứ RAG khi chưa có API key.
"""
import logging
import re
from typing import Optional
from urllib.parse import urlparse

from core.llm_client import llm_client
from features.scam.prompt import SCAM_SYSTEM_PROMPT, build_scam_user_prompt
from features.scam.repository import ScamRepository
from features.scam.schema import (
    ManipulationTactic,
    ScamAnalyzeRequest,
    ScamAnalyzeResponse,
    UrlAnalysis,
)

logger = logging.getLogger("ScamService")

_URL_RE = re.compile(r"(https?://[^\s<>\"']+|www\.[^\s<>\"']+)", re.IGNORECASE)
_RISKY_TLDS = (".online", ".xyz", ".top", ".vip", ".cc", ".icu", ".click", ".loan", ".tk", ".ml")
_GOV_KEYWORDS = ("cand", "congan", "csgt", "phatnguoi", "vneid", "dichvucong", "thue", "bhxh")
_BRAND_KEYWORDS = ("momo", "vietcombank", "vcb", "techcombank", "mbbank", "bidv", "vpbank", "acb")
_OFFICIAL_DOMAINS = (
    "csgt.vn",
    "momo.vn",
    "vietcombank.com.vn",
    "techcombank.com",
    "techcombank.com.vn",
    "mbbank.com.vn",
    "bidv.com.vn",
    "vietinbank.vn",
    "vpbank.com.vn",
    "acb.com.vn",
    "agribank.com.vn",
    "tpb.vn",
)


class ScamService:
    def __init__(self, repository: Optional[ScamRepository] = None):
        self.repository = repository or ScamRepository()

    def analyze(self, req: ScamAnalyzeRequest) -> ScamAnalyzeResponse:
        # 1. URL Heuristics
        url_result = self._inspect_url(req.content)
        url_hint = (
            f"Phát hiện URL: {url_result.url} | Phishing: {url_result.is_phishing} | Cảnh báo: {url_result.warning}"
            if url_result
            else "Không phát hiện đường link (URL) trong nội dung."
        )

        # 2. Retrieve cố định từ scam_domain_kb
        query_text = f"{req.content} {req.context or ''}".strip()
        kb_context, chunks = self.repository.retrieve_context(query_text, top_k=4)
        rag_refs = [f"{c.code}: {c.title}" for c in chunks]

        # 3. Gọi Gemini Structured Output nếu đã cấu hình GEMINI_API_KEY
        if llm_client.is_ready:
            user_prompt = build_scam_user_prompt(
                content=req.content,
                input_type=req.type,
                context=req.context,
                kb_context=kb_context,
                url_hint=url_hint,
            )
            llm_result = llm_client.generate_structured(
                system_prompt=SCAM_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                response_schema=ScamAnalyzeResponse,
            )
            if llm_result is not None:
                if not llm_result.rag_references:
                    llm_result.rag_references = rag_refs
                if llm_result.url_analysis is None and url_result is not None:
                    llm_result.url_analysis = url_result
                return llm_result

        # 4. RAG-backed fallback khi chưa điền GEMINI_API_KEY trong .env
        return self._fallback_analyze(req.content, url_result, rag_refs)

    def _inspect_url(self, content: str) -> Optional[UrlAnalysis]:
        match = _URL_RE.search(content)
        if not match:
            return None

        raw_url = match.group(0).rstrip(".,);!")
        parsed = urlparse(raw_url if raw_url.startswith("http") else f"http://{raw_url}")
        host = (parsed.hostname or "").lower()
        if not host:
            return None

        is_official = host.endswith(".gov.vn") or any(
            host == d or host.endswith(f".{d}") for d in _OFFICIAL_DOMAINS
        )
        if is_official:
            return UrlAnalysis(
                url=raw_url,
                is_phishing=False,
                warning="Tên miền thuộc hệ thống chính thức đã xác minh.",
            )

        warnings = []
        is_phishing = False
        if any(host.endswith(tld) for tld in _RISKY_TLDS):
            is_phishing = True
            warnings.append("Tên miền sử dụng đuôi giá rẻ thường bị lạm dụng cho phishing.")
        if any(k in host for k in _GOV_KEYWORDS) and not host.endswith(".gov.vn"):
            is_phishing = True
            warnings.append("Giả mạo cơ quan nhà nước (tên miền chính thức phải có đuôi .gov.vn hoặc csgt.vn).")
        if any(k in host for k in _BRAND_KEYWORDS):
            is_phishing = True
            warnings.append("Có dấu hiệu giả mạo thương hiệu ngân hàng/ví điện tử (Brand Spoofing).")
        if raw_url.lower().endswith(".apk"):
            is_phishing = True
            warnings.append("Đường link dẫn tới file cài đặt .apk ngoài kho ứng dụng chính thức.")

        return UrlAnalysis(
            url=raw_url,
            is_phishing=is_phishing,
            warning=" ".join(warnings) if warnings else "Đường link chưa xác minh nguồn gốc, cần kiểm tra kỹ trước khi truy cập.",
        )

    def _fallback_analyze(
        self,
        content: str,
        url_result: Optional[UrlAnalysis],
        rag_refs: list[str],
    ) -> ScamAnalyzeResponse:
        lower = content.lower()
        tactics: list[ManipulationTactic] = []
        score = 15

        if any(k in lower for k in ("công an", "csgt", "viện kiểm sát", "tòa án", "phạt nguội", "cán bộ")):
            score += 45
            tactics.append(
                ManipulationTactic(
                    tactic="Authority Impersonation (Mạo danh quyền lực)",
                    evidence=content[:80],
                    explanation="Tự xưng cơ quan thực thi pháp luật nhằm gây áp lực buộc nạn nhân phục tùng.",
                )
            )
        if any(k in lower for k in ("24h", "khóa tài khoản", "khởi tố", "ngay lập tức", "trong 2 giờ", "bắt giam")):
            score += 30
            tactics.append(
                ManipulationTactic(
                    tactic="Fear Inducement & False Urgency (Tạo sợ hãi & Gấp gáp ảo)",
                    evidence=content[:80],
                    explanation="Đe dọa pháp lý hoặc thúc ép mốc thời gian ngắn khiến nạn nhân không kịp kiểm chứng.",
                )
            )
        if any(k in lower for k in ("otp", "nâng hạn mức", "hoa hồng", "nhiệm vụ", "giải cứu đơn", "lãi suất 30%")):
            score += 35
            tactics.append(
                ManipulationTactic(
                    tactic="Greed Lure / Credential Phishing (Mồi nhử lợi nhuận hoặc đánh cắp OTP)",
                    evidence=content[:80],
                    explanation="Dẫn dụ lợi ích bất thường hoặc yêu cầu cung cấp mã OTP/thông tin đăng nhập.",
                )
            )
        if url_result and url_result.is_phishing:
            score += 25

        score = min(score, 98)
        if score >= 71:
            level = "CRITICAL"
            summary = "Phát hiện kịch bản lừa đảo mức độ nghiêm trọng dựa trên đối chiếu bộ quy tắc NCSC & URL Heuristics."
            checklist = [
                "TUYỆT ĐỐI KHÔNG bấm vào đường link lạ, không chuyển tiền và không cung cấp mã OTP.",
                "Cơ quan Công an và Ngân hàng không làm việc hay thu phạt qua tin nhắn Zalo/SMS.",
                "Kiểm tra thông tin trực tiếp trên cổng chính thức (csgt.vn hoặc ứng dụng ngân hàng/MoMo).",
                "Chặn, báo cáo số điện thoại qua đầu số 156 hoặc cổng canhbao.ncsc.gov.vn.",
            ]
        elif score >= 31:
            level = "SUSPICIOUS"
            summary = "Nội dung có dấu hiệu đáng ngờ cần xác minh độc lập trước khi thực hiện giao dịch."
            checklist = [
                "Không vội chuyển tiền hoặc cung cấp thông tin cá nhân.",
                "Gọi trực tiếp tổng đài chính thức của tổ chức liên quan để kiểm chứng.",
            ]
        else:
            level = "SAFE"
            summary = "Chưa phát hiện dấu hiệu thao túng tâm lý hoặc kịch bản lừa đảo rõ rệt."
            checklist = [
                "Tiếp tục duy trì thói quen kiểm tra kỹ tên chủ tài khoản nhận trước khi chuyển tiền."
            ]

        return ScamAnalyzeResponse(
            risk_score=score,
            risk_level=level,
            summary=summary,
            psychological_manipulation=tactics,
            url_analysis=url_result,
            actionable_checklist=checklist,
            rag_references=rag_refs,
        )
