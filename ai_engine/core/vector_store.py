"""
Read-Only Fixed Domain Vector Store (ChromaDB).
- Chỉ quản lý 2 collection cố định: `scam_domain_kb` và `finance_rules_kb`.
- Tuyệt đối KHÔNG cung cấp API cho user ghi/chỉnh sửa dữ liệu ở runtime.
- Hỗ trợ cơ chế fallback nhẹ trong bộ nhớ (lexical + cosine) nếu môi trường dev
  chưa cài `chromadb`, giúp test pipeline mượt mà ngay cả khi chưa cài đủ dependency.
"""
import logging
import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional

from core.config import settings
from core.kb_loader import KBChunk, load_markdown_chunks

logger = logging.getLogger("ReadOnlyVectorStore")

_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


@dataclass(frozen=True)
class RetrievedChunk:
    chunk_id: str
    code: str
    title: str
    source_file: str
    content: str
    score: float


class FixedDomainVectorStore:
    """
    Kho Vector cố định, chỉ đọc ở runtime.
    Dữ liệu chỉ được nạp từ `knowledge_base/` thông qua `ingest_fixed_kb()`.
    """

    ALLOWED_COLLECTIONS = {
        settings.scam_collection_name: ("scam", settings.scam_kb_dir),
        settings.finance_collection_name: ("finance", settings.finance_kb_dir),
    }

    def __init__(self):
        self._chroma_client = None
        self._memory_cache: Dict[str, List[KBChunk]] = {}
        self._backend = "memory-fallback"

        try:
            import chromadb  # type: ignore

            settings.vector_store_dir.mkdir(parents=True, exist_ok=True)
            self._chroma_client = chromadb.PersistentClient(
                path=str(settings.vector_store_dir)
            )
            self._backend = "chromadb"
            logger.info(
                "Khởi tạo ChromaDB PersistentClient tại %s", settings.vector_store_dir
            )
        except ImportError:
            logger.warning(
                "Chưa cài `chromadb` — tạm dùng in-memory lexical fallback. "
                "Chạy `pip install -r requirements.txt` để bật ChromaDB thật."
            )
        except Exception as exc:
            logger.warning(
                "Không thể mở ChromaDB (%s) — tạm dùng in-memory lexical fallback.", exc
            )

    @property
    def backend(self) -> str:
        return self._backend

    def ingest_fixed_kb(self, reset: bool = True) -> Dict[str, int]:
        """
        Nạp cố định toàn bộ file Markdown từ `knowledge_base/` vào 2 collection.
        Chỉ gọi từ `scripts/ingest_kb.py` hoặc lúc khởi động server nếu DB chưa có dữ liệu.
        """
        stats: Dict[str, int] = {}

        for collection_name, (domain, kb_dir) in self.ALLOWED_COLLECTIONS.items():
            chunks = load_markdown_chunks(kb_dir, domain=domain)
            self._memory_cache[collection_name] = chunks
            stats[collection_name] = len(chunks)

            if self._chroma_client is not None:
                if reset:
                    try:
                        self._chroma_client.delete_collection(name=collection_name)
                    except Exception:
                        pass

                collection = self._chroma_client.get_or_create_collection(
                    name=collection_name,
                    metadata={"hnsw:space": "cosine", "domain": domain, "read_only": "true"},
                )
                if chunks:
                    collection.upsert(
                        ids=[c.chunk_id for c in chunks],
                        documents=[c.content for c in chunks],
                        metadatas=[c.to_metadata() for c in chunks],
                    )
                logger.info(
                    "Đã ingest %d chunks vào ChromaDB collection `%s`.",
                    len(chunks),
                    collection_name,
                )

        return stats

    def ensure_ready(self) -> None:
        """
        Đảm bảo 2 collection cố định đã sẵn sàng để đọc (Read-Only).
        Nếu chưa được ingest thì tự động nạp 1 lần từ `knowledge_base/`.
        """
        if self._chroma_client is not None:
            needs_ingest = False
            for collection_name in self.ALLOWED_COLLECTIONS:
                try:
                    col = self._chroma_client.get_collection(name=collection_name)
                    if col.count() == 0:
                        needs_ingest = True
                except Exception:
                    needs_ingest = True
            if needs_ingest:
                self.ingest_fixed_kb(reset=False)
        else:
            if not self._memory_cache:
                self.ingest_fixed_kb(reset=False)

    def search(
        self,
        collection_name: str,
        query: str,
        top_k: Optional[int] = None,
    ) -> List[RetrievedChunk]:
        """
        Truy vấn CHỈ ĐỌC (Read-Only) trên 1 trong 2 collection cố định.
        """
        if collection_name not in self.ALLOWED_COLLECTIONS:
            raise ValueError(
                f"Collection không hợp lệ: {collection_name}. "
                f"Chỉ cho phép: {list(self.ALLOWED_COLLECTIONS.keys())}"
            )

        self.ensure_ready()
        k = top_k or settings.default_top_k
        cleaned_query = (query or "").strip()
        if not cleaned_query:
            return []

        if self._chroma_client is not None:
            return self._search_chroma(collection_name, cleaned_query, k)
        return self._search_memory(collection_name, cleaned_query, k)

    def _search_chroma(
        self, collection_name: str, query: str, top_k: int
    ) -> List[RetrievedChunk]:
        collection = self._chroma_client.get_collection(name=collection_name)
        count = collection.count()
        if count == 0:
            return []

        result = collection.query(
            query_texts=[query],
            n_results=min(top_k, count),
            include=["documents", "metadatas", "distances"],
        )

        ids = result.get("ids", [[]])[0]
        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]

        retrieved: List[RetrievedChunk] = []
        for cid, doc, meta, dist in zip(ids, docs, metas, distances):
            # Chroma cosine distance nằm trong [0, 2]; chuyển sang similarity score [0, 1]
            score = max(0.0, round(1.0 - float(dist), 4))
            retrieved.append(
                RetrievedChunk(
                    chunk_id=cid,
                    code=meta.get("code", ""),
                    title=meta.get("title", ""),
                    source_file=meta.get("source_file", ""),
                    content=doc,
                    score=score,
                )
            )
        return retrieved

    def _search_memory(
        self, collection_name: str, query: str, top_k: int
    ) -> List[RetrievedChunk]:
        chunks = self._memory_cache.get(collection_name, [])
        if not chunks:
            return []

        q_tokens = Counter(_TOKEN_RE.findall(query.lower()))
        q_norm = math.sqrt(sum(v * v for v in q_tokens.values())) or 1.0

        scored: List[RetrievedChunk] = []
        for chunk in chunks:
            c_tokens = Counter(_TOKEN_RE.findall(chunk.content.lower()))
            c_norm = math.sqrt(sum(v * v for v in c_tokens.values())) or 1.0
            dot = sum(q_tokens[t] * c_tokens[t] for t in q_tokens if t in c_tokens)
            score = round(dot / (q_norm * c_norm), 4)
            if score > 0:
                scored.append(
                    RetrievedChunk(
                        chunk_id=chunk.chunk_id,
                        code=chunk.code,
                        title=chunk.title,
                        source_file=chunk.source_file,
                        content=chunk.content,
                        score=score,
                    )
                )

        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]


# Singleton Read-Only Vector Store dùng chung cho các feature repositories
vector_store = FixedDomainVectorStore()
