"""
Markdown Knowledge Base Loader & Section Chunker.
Tách các file .md cố định trong `knowledge_base/` theo từng heading `## [MÃ]`
để mỗi chunk giữ trọn vẹn 1 thủ đoạn lừa đảo hoặc 1 quy chuẩn tài chính.
"""
import re
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger("KBLoader")

_SECTION_SPLIT_RE = re.compile(r"(?m)^##\s+")
_CODE_HEADER_RE = re.compile(r"^\[([A-Z0-9_-]+)\]\s*(.+)$")


@dataclass(frozen=True)
class KBChunk:
    chunk_id: str
    domain: str
    source_file: str
    code: str
    title: str
    content: str

    def to_metadata(self) -> Dict[str, str]:
        return {
            "domain": self.domain,
            "source_file": self.source_file,
            "code": self.code,
            "title": self.title,
        }


def load_markdown_chunks(directory: Path, domain: str) -> List[KBChunk]:
    """
    Đọc toàn bộ file `.md` trong `directory` và tách thành danh sách KBChunk theo heading `##`.
    """
    if not directory.exists():
        logger.warning("Thư mục Knowledge Base không tồn tại: %s", directory)
        return []

    chunks: List[KBChunk] = []
    for md_file in sorted(directory.glob("*.md")):
        raw_text = md_file.read_text(encoding="utf-8").strip()
        if not raw_text:
            continue

        parts = _SECTION_SPLIT_RE.split(raw_text)
        # parts[0] là tiêu đề cấp # và phần mô tả đầu file; từ parts[1:] là các mục ##
        for idx, section in enumerate(parts[1:], start=1):
            lines = [line.rstrip() for line in section.strip().splitlines()]
            if not lines:
                continue

            header_line = lines[0].strip()
            body = "\n".join(lines[1:]).strip()
            if not body:
                continue

            match = _CODE_HEADER_RE.match(header_line)
            if match:
                code = match.group(1).strip()
                title = match.group(2).strip()
            else:
                code = f"{domain.upper()}-{idx:02d}"
                title = header_line

            chunk_id = f"{domain}::{md_file.stem}::{code}"
            full_content = f"[{code}] {title}\n{body}"
            chunks.append(
                KBChunk(
                    chunk_id=chunk_id,
                    domain=domain,
                    source_file=md_file.name,
                    code=code,
                    title=title,
                    content=full_content,
                )
            )

    logger.info("Đã nạp %d chunks từ %s (domain=%s)", len(chunks), directory, domain)
    return chunks
