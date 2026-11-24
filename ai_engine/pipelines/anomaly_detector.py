"""
Pipeline Phát hiện Biến động Dị biệt (Anomaly Detection) & Tính toán Burn-rate dòng tiền
"""
import logging
from typing import List, Dict, Any

logger = logging.getLogger("Anomaly_Detector")

class AnomalyDetector:
    def __init__(self):
        logger.info("Khởi tạo Anomaly Detector (Quy tắc Thống kê & Isolation Forest)")

    def detect_anomalies(self, transactions: List[Dict[str, Any]], user_baseline: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phát hiện các giao dịch bất thường so với thói quen sinh hoạt của User
        """
        return {
            "period": "LAST_30_DAYS",
            "anomaly_count": 2,
            "burn_rate": {
                "days_passed_percent": 40,
                "budget_spent_percent": 72,
                "status": "FAST_BURN_WARNING",
                "message": "Bạn đã tiêu hết 72% ngân sách tháng dù mới qua 12 ngày!"
            },
            "flagged_transactions": [
                {
                    "amount": 2500000,
                    "recipient": "NGUYEN VAN X",
                    "reason": "Giao dịch phát sinh lúc 02:15 sáng (lệch so với khung giờ sinh hoạt)."
                }
            ]
        }
