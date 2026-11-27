"""
Repository (Read-Only RAG Retriever) cho Feature Scam Intelligence.
Chỉ truy vấn đọc trên collection cố định `scam_domain_kb`.
"""
from typing import List, Tuple

from core.config import settings
from core.vector_store import RetrievedChunk, vector_store


class ScamRepository:
    def retrieve_context(
        self, query: str, top_k: int = 4
    ) -> Tuple[str, List[RetrievedChunk]]:
        chunks = vector_store.search(
            collection_name=settings.scam_collection_name,
            query=query,
            top_k=top_k,
        )
        if not chunks:
            return "Không tìm thấy kịch bản tương đồng trong kho tri thức.", []

        formatted = "\n\n---\n\n".join(
            f"[Nguồn: {c.source_file} | Mã: {c.code} | Điểm khớp: {c.score}]\n{c.content}"
            for c in chunks
        )
        return formatted, chunks
