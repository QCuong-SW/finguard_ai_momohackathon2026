# QUY CHUẨN KIỂM TRA URL, TÊN MIỀN & KÊNH LIÊN LẠC CHÍNH THỨC TẠI VIỆT NAM

> **Collection:** `scam_domain_kb` | **Phục vụ:** API 1 (`url_analysis` & Heuristics + LLM XAI)

---

## [URL-01] Quy chuẩn tên miền Cơ quan Nhà nước Việt Nam
- **Quy tắc bắt buộc:** Cổng thông tin điện tử chính thức của cơ quan nhà nước, Bộ Công an, Cục Thuế, Dịch vụ công Quốc gia tại Việt Nam sử dụng tên miền cấp cao `.gov.vn` (hoặc tên miền định danh chính thức đã công bố rộng rãi như `csgt.vn`).
- **Dấu hiệu giả mạo chắc chắn (CRITICAL):**
  - Tên miền chứa từ khóa cơ quan nhà nước (`cand`, `congan`, `csgt`, `phatnguoi`, `vneid`, `dichvucong`, `thue`, `bhxh`) nhưng lại đi kèm đuôi thương mại/giá rẻ như `.online`, `.xyz`, `.top`, `.vip`, `.cc`, `.site`, `.info`, `.club`, `.com`, `.net`.
  - Ví dụ giả mạo: `http://tra-cuu-phat-nguoi-cand.online/pay`, `dichvucong-vneid.xyz`.

## [URL-02] Quy chuẩn tên miền Ngân hàng & Ví điện tử phổ biến tại Việt Nam
- **Tên miền chính thức tham chiếu:**
  - Ví MoMo: `momo.vn`
  - Vietcombank: `vietcombank.com.vn`
  - Techcombank: `techcombank.com` / `techcombank.com.vn`
  - MB Bank: `mbbank.com.vn`
  - BIDV: `bidv.com.vn`
  - VietinBank: `vietinbank.vn`
  - VPBank: `vpbank.com.vn`
  - ACB: `acb.com.vn`
  - Agribank: `agribank.com.vn`
  - TPBank: `tpb.vn`
- **Dấu hiệu giả mạo thương hiệu (Brand Spoofing / Typosquatting):**
  - Chèn thêm từ khóa hành động vào tên miền chính: `momo-support-upgrade.xyz`, `vcb-xacthuc.online`, `mbbank-nanghanmuc.com`.
  - Thay đổi ký tự giống nhau về mặt thị giác: `m0mo.vn`, `vietc0mbank.com`, `mbbank-vn.net`.
  - Dùng subdomain đánh lừa: `momo.vn.xacthuc-taikhoan.top` (tên miền thật nằm ngay trước `.top`, không phải `momo.vn`).

## [URL-03] Chỉ báo kỹ thuật của Phishing URL
- **Đuôi tên miền rủi ro cao (High-Risk TLDs):** `.online`, `.xyz`, `.top`, `.vip`, `.cc`, `.icu`, `.buzz`, `.click`, `.loan`, `.work`, `.tk`, `.ml`.
- **Tuổi tên miền (Domain Age):** Tên miền mới đăng ký dưới 30 ngày (đặc biệt 1–7 ngày) nhưng lại mạo danh tổ chức lâu năm có xác suất lừa đảo cực cao.
- **Giao thức & Đường dẫn:**
  - Dùng `http://` không mã hóa cho trang thanh toán/đăng nhập (lưu ý: có `https://` cũng KHÔNG đảm bảo an toàn vì kẻ gian dễ dàng dùng SSL miễn phí).
  - Link rút gọn (`bit.ly`, `tinyurl`, `t.co`, `bom.so`) đi kèm nội dung thúc giục chuyển tiền/đăng nhập nhằm che giấu đích đến thật.
  - Link dẫn thẳng tới file tải về đuôi `.apk` trên Android.
- **Kênh liên lạc bất thường:** Cơ quan nhà nước và ngân hàng không sử dụng tài khoản Zalo cá nhân, số di động 10 số thông thường hoặc email miễn phí (`@gmail.com`, `@yahoo.com`) để gửi quyết định pháp lý hay yêu cầu xác thực OTP.
