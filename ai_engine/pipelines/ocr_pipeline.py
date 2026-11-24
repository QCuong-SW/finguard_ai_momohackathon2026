"""
Pipeline trích xuất văn bản từ hình ảnh (Ảnh chụp màn hình chat Zalo/SMS/Telegram hoặc hợp đồng giấy)
"""
import logging

logger = logging.getLogger("OCR_Pipeline")

class OCRPipeline:
    def __init__(self):
        logger.info("Khởi tạo OCR Pipeline (Hỗ trợ tiếng Việt)")

    def extract_text(self, image_bytes: bytes) -> str:
        """
        Trích xuất text từ ảnh bằng EasyOCR / Tesseract hoặc Gemini Vision API
        """
        # Trả về text mẫu phục vụ cấu trúc kiến trúc
        return "Em là cán bộ CSGT thông báo anh có biên phạt nguội 5.000.000đ. Truy cập link http://tra-cuu-phat-nguoi-cand.online/pay để nộp ngay trong 24h!"
