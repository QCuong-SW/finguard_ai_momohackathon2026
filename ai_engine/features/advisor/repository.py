"""
Repository (Read-Only RAG Retriever) cho Feature Persona Advisor.
Truy vấn đọc trên collection cố định `finance_rules_kb`.
"""
from typing import List, Tuple

from core.config import settings
from core.vector_store import RetrievedChunk, vector_store


class AdvisorRepository:
    def retrieve_finance_guidelines(
        self, query: str, top_k: int = 4
    ) -> Tuple[str, List[RetrievedChunk]]:
        chunks = vector_store.search(
            collection_name=settings.finance_collection_name,
            query=query,
            top_k=top_k,
        )
        if not chunks:
            return "Không tìm thấy quy tắc tài chính phù hợp.", []

        formatted = "\n\n---\n\n".join(
            f"[Nguồn: {c.source_file} | Mã: {c.code} | Điểm khớp: {c.score}]\n{c.content}"
            for c in chunks
        )
        return formatted, chunks
