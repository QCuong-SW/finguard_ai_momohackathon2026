"""
Repository (Read-Only RAG Retriever) cho Feature Contract RAG.
Chỉ truy vấn đọc trên collection cố định `finance_rules_kb`.
Tài liệu hợp đồng của người dùng KHÔNG BAO GIỜ được ghi vào Vector Store.
"""
from typing import List, Tuple

from core.config import settings
from core.vector_store import RetrievedChunk, vector_store


class ContractRagRepository:
    def retrieve_rules(
        self, query: str, top_k: int = 5
    ) -> Tuple[str, List[RetrievedChunk]]:
        chunks = vector_store.search(
            collection_name=settings.finance_collection_name,
            query=query,
            top_k=top_k,
        )
        if not chunks:
            return "Không tìm thấy quy chuẩn tài chính liên quan.", []

        formatted = "\n\n---\n\n".join(
            f"[Nguồn: {c.source_file} | Mã: {c.code} | Điểm khớp: {c.score}]\n{c.content}"
            for c in chunks
        )
        return formatted, chunks
