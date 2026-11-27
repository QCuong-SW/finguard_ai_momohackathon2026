"""
End-to-End API Tests cho FinGuard AI Engine (Package-by-Feature + Read-Only Fixed RAG).
Chạy trực tiếp:
    python ai_engine/tests/test_rag_api.py
Hoặc với pytest:
    pytest ai_engine/tests/test_rag_api.py -v
"""
import sys
import unittest
from pathlib import Path

AI_ENGINE_DIR = Path(__file__).resolve().parent.parent
if str(AI_ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(AI_ENGINE_DIR))

from fastapi.testclient import TestClient

from core.vector_store import vector_store
from server import app


class TestFinGuardRagAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_01_health_check(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["rag_mode"], "read-only-fixed-kb")

    def test_02_scam_analyze_critical(self):
        payload = {
            "type": "TEXT",
            "content": (
                "Em là cán bộ phòng CSGT, thông báo anh/chị có biên phạt nguội 5.000.000đ. "
                "Bấm vào link http://tra-cuu-phat-nguoi-cand.online/pay để nộp ngay trong 24h, "
                "nếu không sẽ khóa tài khoản ngân hàng và khởi tố hình sự!"
            ),
            "context": "Tin nhắn từ số điện thoại lạ qua Zalo",
        }
        res = self.client.post("/api/v1/ai/scam/analyze", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["risk_level"], "CRITICAL")
        self.assertGreaterEqual(data["risk_score"], 71)
        self.assertTrue(data["url_analysis"]["is_phishing"])
        self.assertGreater(len(data["psychological_manipulation"]), 0)
        self.assertGreater(len(data["rag_references"]), 0)

    def test_03_scam_analyze_safe(self):
        payload = {
            "type": "TEXT",
            "content": "Chiều nay 6h gặp nhau ăn tối ở quán cũ nhé bạn ơi.",
        }
        res = self.client.post("/api/v1/ai/scam/analyze", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["risk_level"], "SAFE")
        self.assertLessEqual(data["risk_score"], 30)

    def test_04_contract_rag_analyze_doc(self):
        payload = {
            "doc_name": "Hop_Dong_Vay_Tieu_Dung_Nhanh.pdf",
            "text": (
                "Lãi suất ưu đãi 0.99%/tháng cho 3 tháng đầu, sau đó áp dụng biểu phí điều chỉnh "
                "theo chính sách từng thời kỳ. Bên vay nếu thanh toán trước hạn sẽ chịu phí vi phạm "
                "hợp đồng 15% trên dư nợ còn lại và ủy quyền liên hệ người thân khi chậm trả."
            ),
        }
        res = self.client.post("/api/v1/ai/rag/analyze-doc", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["doc_name"], payload["doc_name"])
        self.assertEqual(data["risk_rating"], "HIGH_RISK")
        self.assertGreaterEqual(len(data["hidden_traps"]), 2)
        self.assertGreater(len(data["suggested_questions"]), 0)
        self.assertGreater(len(data["rag_references"]), 0)

    def test_05_contract_rag_stateless_chat(self):
        payload = {
            "doc_name": "Hop_Dong_Vay_Tieu_Dung_Nhanh.pdf",
            "document_text": "Phí tất toán trước hạn là 15% trên dư nợ còn lại.",
            "question": "Mức phí tất toán trước hạn 15% có cao hơn thông lệ không?",
        }
        res = self.client.post("/api/v1/ai/rag/chat", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(len(data["answer"]) > 0)
        self.assertGreater(len(data["citations"]), 0)

    def test_06_advisor_recommend(self):
        payload = {
            "action": {
                "proposed_action": "SPENDING",
                "amount": 4200000,
                "category": "Mua sắm / Điện tử",
                "notes": "Mua tai nghe Bluetooth trả góp 3 tháng",
            },
            "persona": {
                "monthly_income": 15000000,
                "safe_spending_limit": 4000000,
                "risk_appetite": "LOW",
            },
        }
        res = self.client.post("/api/v1/ai/advisor/recommend", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn(data["recommendation"], ("CAUTION_HOLD", "STRONGLY_DISCOURAGED"))
        self.assertIn("current_budget_status", data["personalized_analysis"])
        self.assertGreater(len(data["action_options"]), 0)
        self.assertGreater(len(data["rag_references"]), 0)

    def test_07_read_only_collection_guard(self):
        with self.assertRaises(ValueError):
            vector_store.search("user_injected_collection", "hack")


if __name__ == "__main__":
    unittest.main(verbosity=2)
