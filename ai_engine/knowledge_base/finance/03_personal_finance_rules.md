# NGUYÊN TẮC QUẢN LÝ TÀI CHÍNH CÁ NHÂN & NGƯỠNG AN TOÀN CHI TIÊU

> **Collection:** `finance_rules_kb` | **Phục vụ:** API 3 (`PersonaAdvisor`) & API 4 (Anomaly / Burn-rate Context)

---

## [FIN-01] Quy tắc phân bổ ngân sách 50 / 30 / 20
- **50% Nhu cầu thiết yếu:** Tiền thuê nhà, điện nước, ăn uống cơ bản, đi lại, bảo hiểm y tế, chi phí gia đình cố định.
- **30% Mong muốn cá nhân:** Mua sắm không thiết yếu (đồ điện tử, thời trang), giải trí, du lịch, ăn ngoài.
- **20% Tiết kiệm & Đầu tư:** Quỹ dự phòng khẩn cấp, trả nợ sớm, đầu tư dài hạn.
- **Ngưỡng cảnh báo cho Advisor:** Nếu một khoản chi thuộc nhóm Mong muốn (30%) làm vượt quá hạn mức ngân sách còn lại của tháng > 100%, khuyến nghị `CAUTION_HOLD` hoặc `STRONGLY_DISCOURAGED` tùy mức ảnh hưởng đến hóa đơn cố định sắp tới.

## [FIN-02] Quy tắc Quỹ dự phòng khẩn cấp (Emergency Fund)
- **Chuẩn an toàn tối thiểu:** Duy trì quỹ tiền mặt thanh khoản cao đủ trang trải **3 đến 6 tháng chi phí sinh hoạt thiết yếu** (mức báo động đỏ: dưới 1 tháng hoặc dưới 15 ngày sinh hoạt).
- **Nguyên tắc ra quyết định:** TUYỆT ĐỐI không rút quỹ dự phòng khẩn cấp để phục vụ mua sắm tiêu dùng, giải trí hoặc đầu tư rủi ro cao. Nếu khoản chi khiến quỹ dự phòng tụt xuống dưới 30 ngày sinh hoạt $\rightarrow$ bắt buộc cảnh báo đỏ.

## [FIN-03] Tỷ lệ Nợ trên Thu nhập (DTI – Debt-to-Income Ratio)
- **Công thức:** `DTI = (Tổng tiền trả góp + trả nợ gốc lãi hàng tháng) / Thu nhập ròng hàng tháng`.
- **Ngưỡng đánh giá:**
  - `DTI <= 20%`: Rất an toàn.
  - `20% < DTI <= 35%`: Mức chấp nhận được, cần thận trọng nếu phát sinh thêm khoản trả góp mới.
  - `DTI > 35%`: Vùng rủi ro cao — dễ mất khả năng thanh toán khi có biến cố thu nhập. Khuyến nghị trì hoãn vay/trả góp mới hoặc chia nhỏ kỳ hạn 0% (không phí chuyển đổi) để giữ nghĩa vụ trả nợ hàng tháng dưới 35%.

## [FIN-04] Đánh giá Tốc độ đốt ngân sách (Burn-rate) & Nghĩa vụ cố định chu kỳ
- **Công thức Burn-rate:** So sánh `budget_spent_percent` (% ngân sách đã tiêu) với `days_passed_percent` (% số ngày đã qua trong tháng).
  - Nếu `budget_spent_percent - days_passed_percent >= 20%`: Trạng thái `FAST_BURN_WARNING` (tiêu nhanh bất thường).
- **Ưu tiên nghĩa vụ cố định (Upcoming Obligations):** Trước khi duyệt khoản chi mới, luôn trừ trước các khoản chi cố định sắp đến hạn trong tháng (tiền nhà, điện nước, học phí, kỳ trả góp thẻ tín dụng).

## [FIN-05] Phân loại Khẩu vị Rủi ro (Risk Appetite) theo User Persona
- **LOW (Thận trọng):** Ưu tiên bảo toàn vốn và dòng tiền ổn định; tránh vay tiêu dùng lãi thả nổi và tránh khoản chi lớn trước ngày nhận lương.
- **MODERATE (Cân bằng):** Có thể chấp nhận trả góp 0% kỳ hạn hợp lý nếu tổng DTI <= 30% và không chạm quỹ dự phòng.
- **HIGH (Ưa rủi ro):** Sẵn sàng đầu tư tăng trưởng nhưng vẫn bắt buộc tuân thủ quy tắc không dùng tiền vay nóng/quỹ khẩn cấp và cảnh giác với cam kết lợi nhuận bất thường (> 20%/năm).
