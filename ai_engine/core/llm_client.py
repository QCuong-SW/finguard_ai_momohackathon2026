"""
Gemini LLM Client chuẩn hóa với Structured JSON Output (Pydantic Schema)
và cơ chế tự động báo trạng thái khi chưa cấu hình GEMINI_API_KEY trong .env.
"""
import json
import logging
from typing import Optional, Type, TypeVar

from pydantic import BaseModel

from core.config import settings

logger = logging.getLogger("GeminiLLMClient")

T = TypeVar("T", bound=BaseModel)


class GeminiLLMClient:
    """
    Wrapper gọi Google Gemini API qua SDK chính thức `google-genai`.
    - Nếu GEMINI_API_KEY chưa được cấu hình: client ở chế độ offline (is_ready=False),
      để các feature service chủ động chạy fallback từ RAG context mà không crash app.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ):
        self.api_key = (api_key if api_key is not None else settings.gemini_api_key).strip()
        self.model = model or settings.gemini_model
        self.temperature = temperature if temperature is not None else settings.gemini_temperature
        self._client = None

        if self.is_ready:
            try:
                from google import genai  # type: ignore

                self._client = genai.Client(api_key=self.api_key)
                logger.info("Khởi tạo GeminiLLMClient thành công (model=%s)", self.model)
            except ImportError:
                logger.warning(
                    "Chưa cài thư viện `google-genai`. Chạy `pip install -r requirements.txt`."
                )
            except Exception as exc:
                logger.error("Lỗi khởi tạo Gemini client: %s", exc)
        else:
            logger.warning(
                "GEMINI_API_KEY chưa được thiết lập trong .env — hệ thống sẽ chạy ở chế độ RAG fallback."
            )

    @property
    def is_ready(self) -> bool:
        return self.api_key.lower() not in {"", "your_gemini_api_key_here", "change_me", "none", "null"}

    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_schema: Type[T],
    ) -> Optional[T]:
        """
        Gọi Gemini API và ép đầu ra JSON khớp 100% với Pydantic `response_schema`.
        Trả về None nếu chưa có API key hoặc gọi API thất bại (để service xử lý fallback).
        """
        if not self._client:
            return None

        try:
            from google.genai import types  # type: ignore

            response = self._client.models.generate_content(
                model=self.model,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=self.temperature,
                    response_mime_type="application/json",
                    response_schema=response_schema,
                ),
            )

            raw_text = (response.text or "").strip()
            if not raw_text:
                logger.warning("Gemini trả về nội dung rỗng.")
                return None

            data = json.loads(raw_text)
            return response_schema.model_validate(data)
        except Exception as exc:
            logger.error("Gemini structured generation failed: %s", exc)
            return None


# Singleton dùng chung cho toàn bộ feature services
llm_client = GeminiLLMClient()
