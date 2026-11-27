"""
CLI Script: Nạp cố định toàn bộ Knowledge Base (`knowledge_base/`) vào ChromaDB
và chạy kiểm thử truy xuất (smoke test) trên cả 2 collection.

Cách chạy:
    cd ai_engine
    python scripts/ingest_kb.py
"""
import logging
import sys
from pathlib import Path

# Đảm bảo import được `core.*` khi chạy trực tiếp từ thư mục `ai_engine/` hoặc gốc repo
AI_ENGINE_DIR = Path(__file__).resolve().parent.parent
if str(AI_ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(AI_ENGINE_DIR))

from core.config import settings
from core.vector_store import vector_store

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


def main() -> None:
    print(f"=== FinGuard AI Fixed KB Ingestion (backend={vector_store.backend}) ===")
    stats = vector_store.ingest_fixed_kb(reset=True)
    for col_name, count in stats.items():
        print(f"  - Collection `{col_name}`: {count} chunks")

    print("\n--- Smoke Test 1: scam_domain_kb ---")
    scam_query = "cán bộ CSGT thông báo phạt nguội 5 triệu bấm vào link .online nộp trong 24h"
    for item in vector_store.search(settings.scam_collection_name, scam_query, top_k=3):
        print(f"  [{item.score:.4f}] {item.code} - {item.title} ({item.source_file})")

    print("\n--- Smoke Test 2: finance_rules_kb ---")
    finance_query = "lãi suất ưu đãi 0.99% 3 tháng đầu sau đó thả nổi, phí phạt tất toán trước hạn 15%"
    for item in vector_store.search(settings.finance_collection_name, finance_query, top_k=3):
        print(f"  [{item.score:.4f}] {item.code} - {item.title} ({item.source_file})")


if __name__ == "__main__":
    main()
