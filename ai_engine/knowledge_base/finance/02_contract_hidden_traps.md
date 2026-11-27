# DANH MỤC 12 "BẪY CHỮ NHỎ" (HIDDEN TRAPS) TRONG HỢP ĐỒNG TÀI CHÍNH

> **Collection:** `finance_rules_kb` | **Phục vụ:** API 2 (`RAGEngine.analyze_document_traps`)
> **Mục đích:** Làm chuẩn đối chiếu khi đọc hợp đồng vay tiêu dùng, điều khoản thẻ tín dụng, hợp đồng bảo hiểm/đầu tư do người dùng gửi lên.

---

## [TRAP-01] Bẫy Lãi suất Thả nổi không ghi rõ biên độ / trần
- **Hạng mục:** Lãi suất ngầm
- **Dấu hiệu trong hợp đồng:** "Lãi suất ưu đãi 0.99%/tháng (hoặc 6–8%/năm) cho 3–6 tháng đầu, sau đó áp dụng lãi suất điều chỉnh theo chính sách từng thời kỳ của Bên cho vay."
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Không có công thức tham chiếu rõ ràng và không có mức trần. Sau kỳ ưu đãi, lãi suất thực tế tại các công ty tài chính có thể vọt lên 40%–60%/năm.
- **Câu hỏi cần làm rõ:** Sau thời gian ưu đãi, công thức tính lãi suất cụ thể là gì (Lãi suất cơ sở nào + biên độ bao nhiêu %)? Mức trần tối đa là bao nhiêu?

## [TRAP-02] Bẫy Lãi suất phẳng (Tính trên dư nợ gốc ban đầu thay vì dư nợ giảm dần)
- **Hạng mục:** Lãi suất ngầm
- **Dấu hiệu trong hợp đồng:** Ghi lãi suất "chỉ 1.5%/tháng tính trên số tiền vay ban đầu" (Flat rate).
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Lãi suất tính trên dư nợ gốc ban đầu thực chất tương đương gấp **~1,8 đến 1,9 lần** lãi suất tính trên dư nợ giảm dần (1.5%/tháng phẳng ≈ 32%–34%/năm thực tế).
- **Câu hỏi cần làm rõ:** Lãi suất trong hợp đồng tính theo dư nợ giảm dần hay dư nợ gốc ban đầu? Tổng số tiền gốc + lãi phải trả cuối kỳ là bao nhiêu?

## [TRAP-03] Phí phạt tất toán trước hạn quá cao
- **Hạng mục:** Phí tất toán trước hạn
- **Dấu hiệu trong hợp đồng:** "Thanh toán trước hạn chịu phí vi phạm hợp đồng 10%–15% trên dư nợ còn lại" hoặc "phải trả toàn bộ phần lãi còn lại của hợp đồng nếu trả sớm".
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Thông lệ thị trường tại ngân hàng thương mại Việt Nam chỉ từ **1%–5%** (và thường giảm về 0% sau 2–3 năm). Mức 10%–15% cao gấp 3 lần thông lệ, nhốt người vay trong khoản nợ lãi cao.
- **Câu hỏi cần làm rõ:** Nếu tôi muốn tất toán trước hạn sau 6 tháng, tổng số tiền phạt cụ thể là bao nhiêu?

## [TRAP-04] Phí ẩn & Bảo hiểm khoản vay bị gộp ngầm vào gốc vay
- **Hạng mục:** Phí ẩn & Bảo hiểm bắt buộc trá hình
- **Dấu hiệu trong hợp đồng:** Điều khoản ghi "Bên vay đồng ý tham gia Bảo hiểm dư nợ tín dụng / Phí quản lý hồ sơ / Phí tư vấn 5%–10% cộng trực tiếp vào số tiền giải ngân".
- **Mức độ rủi ro:** MEDIUM_HIGH
- **Cảnh báo:** Người vay không nhận đủ tiền mặt nhưng vẫn phải trả lãi trên cả phần phí bảo hiểm bị cộng gộp vào gốc. Theo quy định, bảo hiểm khoản vay là tự nguyện, không được ép mua kèm.
- **Câu hỏi cần làm rõ:** Khoản vay có bắt buộc mua bảo hiểm hay trả phí quản lý hồ sơ không? Số tiền thực nhận về tay là bao nhiêu?

## [TRAP-05] Điều khoản Ủy quyền truy cập danh bạ & Liên hệ người thân
- **Hạng mục:** Xâm phạm quyền riêng tư
- **Dấu hiệu trong hợp đồng:** "Bên vay ủy quyền cho Bên cho vay truy cập danh bạ, mạng xã hội và liên hệ với người thân, đồng nghiệp, cơ quan công tác để xác minh hoặc nhắc nợ."
- **Mức độ rủi ro:** CRITICAL
- **Cảnh báo:** Vi phạm quyền bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP) và quy định thu hồi nợ tiêu dùng (TT 43/2016/TT-NHNN); thường bị các app tín dụng đen lợi dụng để bôi nhọ danh dự khi trễ hạn.
- **Câu hỏi cần làm rõ:** Hợp đồng có cho phép bên cho vay gọi điện hoặc gửi thông tin khoản nợ cho người thân, đồng nghiệp của tôi không?

## [TRAP-06] Phí phạt chậm trả & Lãi phạt kép (Lãi chồng lãi)
- **Hạng mục:** Phạt vi phạm hợp đồng
- **Dấu hiệu trong hợp đồng:** "Chậm thanh toán quá 1 ngày chịu phạt cố định 500.000đ/lần cộng thêm lãi suất phạt 150%–200% trên toàn bộ dư nợ gốc còn lại."
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Mức phạt tính trên toàn bộ dư nợ thay vì chỉ trên phần nợ quá hạn, cộng thêm phí nhắc nợ lặp lại hàng ngày khiến khoản nợ phình to mất kiểm soát.
- **Câu hỏi cần làm rõ:** Nếu tôi chậm trả 3 ngày thì tổng phí phạt và lãi quá hạn được tính trên phần kỳ hạn trễ hay toàn bộ dư nợ?

## [TRAP-07] Tự động gia hạn hợp đồng & Trừ phí ngầm (Auto-Renewal)
- **Hạng mục:** Tự động gia hạn
- **Dấu hiệu trong hợp đồng:** "Hợp đồng/gói hội viên tự động gia hạn chu kỳ tiếp theo và tự động trích nợ từ thẻ/tài khoản nếu khách hàng không gửi văn bản hủy trước 30 ngày."
- **Mức độ rủi ro:** MEDIUM_HIGH
- **Cảnh báo:** Bẫy phổ biến trong thẻ tín dụng, bảo hiểm liên kết và gói dịch vụ trả phí, khiến khách hàng bị trừ tiền định kỳ ngoài ý muốn.
- **Câu hỏi cần làm rõ:** Tôi cần thực hiện thủ tục hủy trước bao nhiêu ngày và qua kênh nào để không bị tự động gia hạn?

## [TRAP-08] Trả góp "0% lãi suất" nhưng ẩn phí chuyển đổi cao
- **Hạng mục:** Phí chuyển đổi trả góp
- **Dấu hiệu trong hợp đồng:** "Ưu đãi trả góp 0% lãi suất, áp dụng phí chuyển đổi 1%/tháng (hoặc 6%–9%/năm) và phí quản lý giao dịch."
- **Mức độ rủi ro:** MEDIUM
- **Cảnh báo:** Dù quảng cáo 0% lãi suất, tổng phí chuyển đổi 6%–9% trên giá trị gốc ban đầu tương đương mức lãi suất thực tế 12%–18%/năm theo dư nợ giảm dần.
- **Câu hỏi cần làm rõ:** Ngoài 0% lãi suất, tổng phí chuyển đổi trả góp và các phí đi kèm cho toàn kỳ hạn là bao nhiêu tiền?

## [TRAP-09] Điều khoản Đơn phương thay đổi biểu phí / điều khoản
- **Hạng mục:** Bất cân xứng quyền lợi
- **Dấu hiệu trong hợp đồng:** "Bên cung cấp có toàn quyền điều chỉnh biểu phí, lãi suất hoặc điều khoản bất kỳ lúc nào mà không cần sự đồng ý trước của khách hàng."
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Đặt toàn bộ rủi ro tăng chi phí về phía người dùng mà không có cơ chế từ chối hoặc chấm dứt hợp đồng không mất phí.

## [TRAP-10] Bẫy "Cam kết lợi nhuận cố định" trong Hợp đồng Hợp tác đầu tư / Trái phiếu
- **Hạng mục:** Rủi ro lừa đảo đầu tư / Ponzi
- **Dấu hiệu trong hợp đồng:** "Cam kết lợi nhuận cố định 24%–36%/năm không phụ thuộc kết quả kinh doanh", không có tài sản bảo đảm, không có tổ chức kiểm toán độc lập hoặc doanh nghiệp phát hành mới thành lập.
- **Mức độ rủi ro:** CRITICAL
- **Cảnh báo:** Lãi suất cam kết cao gấp 4–6 lần lãi suất tiết kiệm ngân hàng là dấu hiệu điển hình của mô hình huy động vốn đa cấp/Ponzi hoặc rủi ro mất trắng vốn.

## [TRAP-11] Miễn trừ trách nhiệm một chiều & Trọng tài bất lợi
- **Hạng mục:** Pháp lý bất lợi
- **Dấu hiệu trong hợp đồng:** "Bên cung cấp được miễn trừ mọi trách nhiệm đối với thiệt hại phát sinh từ sự cố kỹ thuật hoặc hành vi của bên thứ ba; mọi tranh chấp chỉ được giải quyết tại trung tâm trọng tài do Bên cung cấp chỉ định."
- **Mức độ rủi ro:** MEDIUM_HIGH
- **Cảnh báo:** Hạn chế quyền khởi kiện và đòi bồi thường hợp pháp của người dùng khi xảy ra sự cố lộ lọt dữ liệu hoặc mất tiền oan.

## [TRAP-12] Bẫy Lãi suất Thẻ tín dụng khi chỉ thanh toán "Dư nợ tối thiểu"
- **Hạng mục:** Điều khoản thẻ tín dụng
- **Dấu hiệu trong hợp đồng:** Cho phép thanh toán tối thiểu 5% dư nợ cuối kỳ; tuy nhiên nếu không thanh toán đủ 100% dư nợ sao kê, ngân hàng sẽ tính lãi 25%–38%/năm trên **toàn bộ giao dịch kể từ ngày quẹt thẻ** (mất hoàn toàn ưu đãi miễn lãi 45 ngày).
- **Mức độ rủi ro:** HIGH_RISK
- **Cảnh báo:** Chỉ cần trả thiếu 1 đồng so với dư nợ sao kê, toàn bộ kỳ giao dịch sẽ bị truy thu lãi suất rất cao ngay lập tức.
