# CẨM NĂNG 24 HÌNH THỨC LỪA ĐẢO TRỰC TUYẾN TẠI VIỆT NAM (NCSC & BỘ CÔNG AN)

> **Collection:** `scam_domain_kb` | **Phục vụ:** API 1 (Scam Analyzer & XAI)
> **Cấu trúc:** Mỗi mục `##` là 1 đơn vị tri thức độc lập phục vụ chunking RAG.

---

## [SCAM-01] Giả danh Cơ quan Công an, CSGT, Viện kiểm sát, Tòa án
- **Nhóm chiêu thức:** Authority Impersonation (Mạo danh quyền lực), Fear Inducement (Tạo sợ hãi), False Urgency (Gấp gáp ảo).
- **Dấu hiệu nhận diện:** Tự xưng cán bộ Công an, CSGT, VKS; thông báo nạn nhân liên quan đường dây rửa tiền, ma túy hoặc có biên phạt nguội giao thông; gửi lệnh bắt/quyết định khởi tố giả qua Zalo; gửi đường link đuôi lạ (`.online`, `.xyz`, `.top`) hoặc yêu cầu chuyển tiền vào "tài khoản an toàn / tài khoản tạm giữ" để chứng minh vô tội trong 24h.
- **Ví dụ câu chữ:** "Em là cán bộ phòng CSGT, thông báo anh/chị có biên phạt nguội 5.000.000đ. Bấm vào link để nộp ngay trong 24h nếu không sẽ khóa tài khoản ngân hàng và khởi tố hình sự."
- **Hành động khuyến nghị:** TUYỆT ĐỐI KHÔNG bấm link lạ hoặc chuyển tiền. Cơ quan Công an KHÔNG làm việc, không thu tiền phạt nguội hay xác minh tài sản qua điện thoại/Zalo/SMS. Tra cứu phạt nguội duy nhất tại `csgt.vn`. Chặn và báo cáo số điện thoại.

## [SCAM-02] Giả mạo SMS Brandname Ngân hàng & Ví điện tử (Smishing / Trạm BTS giả)
- **Nhóm chiêu thức:** Brand Impersonation, False Urgency, Credential Phishing.
- **Dấu hiệu nhận diện:** Tin nhắn hiển thị tên thương hiệu Ngân hàng hoặc Ví điện tử (MoMo, VCB, TCB, MB...) chèn vào cùng luồng tin nhắn thật; thông báo tài khoản bị đăng nhập ở nước ngoài, sắp bị trừ phí thường niên, thẻ được nâng hạn mức hoặc điểm thưởng sắp hết hạn; kèm đường link yêu cầu đăng nhập và nhập mã OTP.
- **Ví dụ câu chữ:** "Thẻ tín dụng của quý khách đã được duyệt nâng hạn mức 50 triệu. Truy cập https://momo-support-upgrade.xyz để xác nhận trong 2 giờ."
- **Hành động khuyến nghị:** Không nhấn vào đường link trong SMS. Ngân hàng và Ví điện tử không bao giờ gửi link yêu cầu nhập mật khẩu hay mã OTP. Mở trực tiếp ứng dụng chính thức hoặc gọi tổng đài in sau thẻ để kiểm tra.

## [SCAM-03] Tuyển cộng tác viên làm nhiệm vụ sàn TMĐT (Job / Task Scam)
- **Nhóm chiêu thức:** Greed Lure (Mồi nhử lợi nhuận), Foot-in-the-door (Bẫy cam kết từng bước), Sunk Cost Fallacy (Tâm lý tiếc tiền).
- **Dấu hiệu nhận diện:** Mời làm CTV nghe nhạc, xem video TikTok, bấm thích sản phẩm Shopee/Lazada/Tiki hoặc đặt phòng khách sạn nhận hoa hồng 10–30%. Ban đầu trả hoa hồng thật cho 2–3 đơn nhỏ (vài trăm nghìn), sau đó dụ nạp số tiền lớn vào đơn hàng VIP rồi báo "lỗi cú pháp", "kẹt hệ thống", ép nạp thêm tiền để "giải cứu đơn hàng".
- **Ví dụ câu chữ:** "Việc nhẹ lương cao tại nhà, chỉ cần bấm đơn Shopee nhận 300k–1tr/ngày. Đơn của bạn bị lỗi hệ thống, cần nạp thêm 15 triệu để mở khóa rút toàn bộ gốc và lãi."
- **Hành động khuyến nghị:** Dừng nạp tiền ngay lập tức; tiền đã nạp vào hệ thống lừa đảo không thể "giải cứu" bằng cách nạp thêm. Các sàn TMĐT không tuyển CTV nạp tiền trước để làm nhiệm vụ. Lưu toàn bộ lịch sử chat và sao kê để trình báo công an.

## [SCAM-04] Giả danh nhân viên Viễn thông / Ngân hàng nâng cấp SIM 4G–5G & Sinh trắc học
- **Nhóm chiêu thức:** Authority/Tech Support Impersonation, False Urgency.
- **Dấu hiệu nhận diện:** Gọi điện hoặc nhắn tin dọa khóa SIM trong 2 giờ nếu không nâng cấp 4G/5G, hoặc hướng dẫn cập nhật sinh trắc học khuôn mặt/CCCD gắn chip qua đường link lạ hoặc file `.apk` cài ngoài kho ứng dụng. Mục đích là chiếm quyền nhận SMS OTP hoặc điều khiển điện thoại từ xa.
- **Ví dụ câu chữ:** "Tài khoản của anh/chị chưa cập nhật sinh trắc học sẽ bị khóa giao dịch sau 17h hôm nay. Tải app hỗ trợ qua link này để nhân viên xác thực giúp."
- **Hành động khuyến nghị:** Chỉ cập nhật sinh trắc học trực tiếp trên ứng dụng chính thức của Ngân hàng/Ví điện tử hoặc tại quầy giao dịch. Tuyệt đối không cài file `.apk` từ link lạ và không cấp quyền Trợ năng (Accessibility) cho app lạ.

## [SCAM-05] Giả mạo cài đặt ứng dụng Dịch vụ công / VNeID / Thuế (Malware `.apk`)
- **Nhóm chiêu thức:** Authority Impersonation, Technical Deception (Chiếm quyền thiết bị Android).
- **Dấu hiệu nhận diện:** Tự xưng công an khu vực hoặc cán bộ thuế yêu cầu cập nhật định danh mức 2, đóng thuế hộ kinh doanh hoặc sửa sai thông tin CCCD; gửi đường link giả mạo Cổng Dịch vụ công để tải file cài đặt `.apk` chứa mã độc chiếm quyền điều khiển điện thoại và đọc trộm OTP ngân hàng.
- **Ví dụ câu chữ:** "Anh/chị cần kích hoạt VNeID mức 2 gấp trong hôm nay, bấm vào link dichvucong-vneid.online tải bản cập nhật về cài đặt."
- **Hành động khuyến nghị:** Không tải ứng dụng qua đường link trên Zalo/SMS. Chỉ tải VNeID từ Google Play Store hoặc Apple App Store chính thức. Nếu lỡ cài `.apk` lạ, lập tức ngắt Wi-Fi/4G, gọi ngân hàng khóa tài khoản và khôi phục cài đặt gốc thiết bị.

## [SCAM-06] Lừa đảo tình cảm kết hợp đầu tư tài chính (Romance Scam / Pig Butchering)
- **Nhóm chiêu thức:** Emotional Manipulation (Thao túng tình cảm), Long-term Grooming (Nuôi lòng tin dài hạn), Fraudulent Investment.
- **Dấu hiệu nhận diện:** Kết bạn qua Facebook, Tinder, Zalo với hồ sơ hào nhoáng (doanh nhân, bác sĩ, Việt kiều, quân nhân nước ngoài); nhắn tin quan tâm dài ngày để tạo tình cảm sâu sắc; sau đó rủ đầu tư sàn vàng, Forex, tiền ảo (crypto) cam kết lợi nhuận 20–30%/tháng. Khi nạn nhân muốn rút tiền lãi, sàn đòi đóng "phí thuế thu nhập 10–20%", "phí xác minh rửa tiền".
- **Ví dụ câu chữ:** "Anh có chú làm trong quỹ nội bộ biết trước khung giờ vào lệnh thắng 100%, em thử nạp 5 triệu rút lãi ngay hôm nay xem."
- **Hành động khuyến nghị:** Không chuyển tiền hoặc đầu tư vào sàn giao dịch theo lời rủ rê của người quen qua mạng chưa từng gặp mặt. Mọi sàn đòi nạp thêm thuế/phí mới cho rút tiền đều là lừa đảo 100%.

## [SCAM-07] Deepfake gọi video giả danh người thân, bạn bè vay tiền khẩn cấp
- **Nhóm chiêu thức:** Identity Impersonation, Emergency/Fear Inducement, GenAI Deepfake.
- **Dấu hiệu nhận diện:** Hack tài khoản Facebook/Zalo của người quen rồi nhắn tin mượn tiền gấp (tai nạn, cấp cứu, kẹt hàng); gọi video call ngắn vài giây với hình ảnh mờ, giật lag, âm thanh ngắt quãng rồi tắt máy bảo "sóng yếu", sau đó gửi số tài khoản ngân hàng tên người lạ để nhận tiền.
- **Ví dụ câu chữ:** "Mình đang có việc gấp cần chuyển 10 triệu ngay, lát chiều mình gửi lại. Chuyển giúp vào STK bạn mình nhé, tài khoản mình đang lỗi."
- **Hành động khuyến nghị:** Luôn gọi lại trực tiếp bằng số điện thoại di động thông thường (không gọi qua app chat bị nghi hack) và hỏi câu hỏi riêng tư chỉ hai người biết trước khi chuyển tiền.

## [SCAM-08] Lừa đảo "Combo du lịch giá rẻ", đặt phòng khách sạn, vé máy bay giả
- **Nhóm chiêu thức:** Scarcity & Greed (Khan hiếm giả, giá rẻ bất thường).
- **Dấu hiệu nhận diện:** Fanpage giả mạo resort/khách sạn lớn (thậm chí có tích xanh thuê/mua) chào bán combo nghỉ dưỡng rẻ hơn thị trường 40–60%; thúc giục chuyển khoản cọc 50–100% để giữ suất khuyến mãi cuối cùng; sau khi nhận tiền thì chặn liên lạc hoặc báo "chuyển sai nội dung" để dụ chuyển tiếp.
- **Hành động khuyến nghị:** Kiểm tra tính minh bạch của Fanpage (mục Tính minh bạch của Trang – ngày đổi tên, lịch sử quản trị). Gọi trực tiếp số hotline công bố trên website chính thức của khách sạn/hãng bay để xác nhận trước khi đặt cọc.

## [SCAM-09] Lừa đảo App vay tiền online siêu tốc & Phí giải ngân trước (Advance Fee Fraud)
- **Nhóm chiêu thức:** Financial Desperation Exploitation, Advance Fee Trap.
- **Dấu hiệu nhận diện:** Quảng cáo vay online không cần thẩm định, duyệt trong 5 phút, lãi suất 0%. Khi nạn nhân nộp hồ sơ, đối tượng gửi hợp đồng giả báo "sai số tài khoản ngân hàng nên tiền bị đóng băng", yêu cầu chuyển 10–20% giá trị khoản vay làm "phí mở khóa / phí bảo hiểm giải ngân".
- **Ví dụ câu chữ:** "Hồ sơ vay 50 triệu đã duyệt nhưng anh nhập sai 1 số tài khoản, cần chuyển 5 triệu xác minh để hệ thống tự động giải ngân cả gốc và tiền xác minh."
- **Hành động khuyến nghị:** Không có ngân hàng hay tổ chức tín dụng hợp pháp nào yêu cầu người vay chuyển tiền trước để "mở khóa giải ngân". Dừng giao dịch ngay lập tức.

## [SCAM-10] Lừa đảo "Lấy lại tiền bị lừa" (Recovery Scam)
- **Nhóm chiêu thức:** Secondary Victimization (Tái trục lợi nạn nhân), Authority Impersonation.
- **Dấu hiệu nhận diện:** Quảng cáo trên Facebook/TikTok tự xưng là "luật sư an ninh mạng", "hacker mũ trắng", "đội hỗ trợ thu hồi vốn bị treo từ Cục An ninh mạng"; cam kết lấy lại 100% tiền đã bị lừa trước đó nhưng yêu cầu đóng "phí hồ sơ", "phí kích hoạt hệ thống" hoặc nạp tiền chạy lệnh hoàn tiền.
- **Hành động khuyến nghị:** Đây là bẫy lừa đảo nối tiếp (lừa chồng lừa). Chỉ cơ quan Công an chính thức mới có thẩm quyền điều tra và xử lý hoàn trả tài sản theo quy định pháp luật.

## [SCAM-11] Lừa đảo giả danh Shipper / Nhân viên giao hàng
- **Nhóm chiêu thức:** Routine Exploitation (Lợi dụng thói quen mua sắm), Impersonation.
- **Dấu hiệu nhận diện:** Gọi điện báo có đơn hàng gửi tới nhà khi nạn nhân đi vắng, thúc giục chuyển khoản thanh toán trước (COD); sau khi nạn nhân chuyển xong thì báo "gửi nhầm số tài khoản đăng ký hội viên giao hàng", gửi link lạ bảo bấm vào hủy gói cước nếu không sẽ bị trừ 3,5 triệu/tháng.
- **Hành động khuyến nghị:** Không chuyển khoản thanh toán cho đơn hàng chưa nhận tận tay hoặc chưa kiểm tra mã vận đơn trên app sàn TMĐT. Tuyệt đối không bấm vào link "hủy gói hội viên".

## [SCAM-12] Lừa đảo đầu tư chứng khoán quốc tế, tiền ảo (Crypto), quyền chọn nhị phân (BO)
- **Nhóm chiêu thức:** Greed Lure, Social Proof giả (Nhóm Zalo/Telegram toàn nick chim mồi), Ponzi Scheme.
- **Dấu hiệu nhận diện:** Kéo vào nhóm Zalo/Telegram có "chuyên gia đọc lệnh", hàng chục tài khoản ảo liên tục khoe ảnh lãi khủng mỗi ngày; dụ tải app giao dịch riêng không có trên kho ứng dụng chính thức; cho rút lãi nhỏ lần đầu rồi khóa rút tiền khi nạp lớn.
- **Hành động khuyến nghị:** Kiểm tra giấy phép hoạt động của sàn giao dịch tại Ủy ban Chứng khoán Nhà nước. Cảnh giác cao độ với các nhóm kín cam kết lợi nhuận cố định cao bất thường.

## [SCAM-13] Lừa đảo giả danh Giáo viên / Bệnh viện báo con bị tai nạn cấp cứu
- **Nhóm chiêu thức:** Extreme Fear & Panic Inducement (Gây hoảng loạn tột độ).
- **Dấu hiệu nhận diện:** Gọi điện báo con/người thân bị tai nạn chấn thương sọ não đang trong phòng mổ, cần chuyển gấp vài chục triệu viện phí để bác sĩ tiến hành phẫu thuật ngay lập tức.
- **Hành động khuyến nghị:** Giữ bình tĩnh, gọi ngay cho giáo viên chủ nhiệm, nhà trường hoặc người thân để xác minh trực tiếp trước khi chuyển bất kỳ khoản tiền nào.

## [SCAM-14] Lừa đảo chuyển nhầm tiền vào tài khoản rồi ép vay nặng lãi
- **Nhóm chiêu thức:** Reciprocity / Legal Intimidation (Lợi dụng tâm lý trả lại tiền & đe dọa nợ).
- **Dấu hiệu nhận diện:** Bất ngờ nhận một khoản tiền lạ chuyển vào tài khoản kèm nội dung giống giải ngân vay tiền; sau đó kẻ gian gọi điện bảo chuyển nhầm và đòi chuyển trả vào một số tài khoản KHÁC (không trùng tài khoản gửi), rồi sau đó tiếp tục đòi gốc + lãi cắt cổ.
- **Hành động khuyến nghị:** Không tự ý chuyển trả tiền lạ vào số tài khoản khác. Liên hệ trực tiếp ngân hàng để lập biên bản tra soát và hoàn trả đúng tài khoản nguồn theo quy trình ngân hàng.

## [SCAM-15] Lừa đảo dịch vụ Mở khóa tài khoản Facebook, Tăng tương tác, Xóa nợ xấu CIC
- **Nhóm chiêu thức:** Need Exploitation, Advance Fee Fraud.
- **Dấu hiệu nhận diện:** Quảng cáo "xóa nợ xấu CIC trong 24h", "lấy lại Facebook bị hack giá rẻ", yêu cầu chuyển tiền cọc và cung cấp ảnh CCCD hai mặt cùng mã OTP.
- **Hành động khuyến nghị:** Không cá nhân nào có thể tự ý xóa lịch sử tín dụng CIC (dữ liệu do Trung tâm Thông tin Tín dụng Quốc gia quản lý). Không gửi ảnh CCCD và OTP cho dịch vụ mạng không rõ danh tính.

## [SCAM-16] Lừa đảo Tuyển mẫu nhí, Cuộc thi ảnh online, Bình chọn trực tuyến
- **Nhóm chiêu thức:** Emotional/Parental Pride Exploitation + Task Scam / Phishing.
- **Dấu hiệu nhận diện:** Mời phụ huynh đăng ký cho con thi mẫu nhí hoặc gửi link nhờ bình chọn cuộc thi tài năng; dẫn dụ vào nhóm làm nhiệm vụ mua sản phẩm tài trợ để tăng điểm bình chọn, hoặc đánh cắp tài khoản Facebook/Zalo qua trang đăng nhập giả.
- **Hành động khuyến nghị:** Không đăng nhập tài khoản mạng xã hội vào các trang web bình chọn lạ và không nạp tiền để "tăng điểm bình chọn".

## [SCAM-17] Lừa đảo Giả danh Nhân viên Điện lực, Cấp nước, Bảo hiểm xã hội
- **Nhóm chiêu thức:** Authority Impersonation, False Urgency (Dọa cắt dịch vụ thiết yếu).
- **Dấu hiệu nhận diện:** Gọi điện báo chưa đóng tiền điện/nước tháng này và sẽ bị cắt điện sau 2 giờ, yêu cầu kết bạn Zalo gửi hóa đơn giả và cài app thanh toán hoặc chuyển khoản vào tài khoản cá nhân.
- **Hành động khuyến nghị:** Kiểm tra hóa đơn trực tiếp qua ứng dụng EVN/MoMo/Ngân hàng. Công ty điện lực/cấp nước không yêu cầu thanh toán vào tài khoản mang tên cá nhân.

## [SCAM-18] Lừa đảo Khóa thẻ tín dụng, Đáo hạn thẻ, Rút tiền mặt phí rẻ
- **Nhóm chiêu thức:** Financial Convenience Lure, Card Data Theft (Đánh cắp số thẻ & CVV).
- **Dấu hiệu nhận diện:** Mời chào rút tiền mặt/đáo hạn thẻ tín dụng phí thấp hoặc nâng hạn mức miễn phí; yêu cầu chụp ảnh hai mặt thẻ tín dụng (lộ số thẻ và mã CVV/CVC) và đọc mã OTP xác thực giao dịch.
- **Hành động khuyến nghị:** TUYỆT ĐỐI không chụp mặt sau thẻ (mã CVV) và không đọc mã OTP cho bất kỳ ai.

## [SCAM-19] Lừa đảo Tặng quà tri ân, Trúng thưởng từ thương hiệu lớn
- **Nhóm chiêu thức:** Greed & Reciprocity (Quà miễn phí).
- **Dấu hiệu nhận diện:** Thông báo trúng xe máy, iPhone hoặc nhận quà tri ân 0 đồng từ Điện Máy Xanh, Shopee, Viettel; yêu cầu đóng "phí vận chuyển", "phí xuất hóa đơn" hoặc làm nhiệm vụ tương tác nhận thưởng.
- **Hành động khuyến nghị:** Các chương trình trúng thưởng hợp pháp không yêu cầu người trúng chuyển tiền cọc hay nạp tiền làm nhiệm vụ trước khi nhận giải.

## [SCAM-20] Lừa đảo Kêu gọi từ thiện giả mạo sau thiên tai / hoàn cảnh thương tâm
- **Nhóm chiêu thức:** Empathy Exploitation (Lợi dụng lòng trắc ẩn), Fraudulent Crowdfunding.
- **Dấu hiệu nhận diện:** Tạo Fanpage mạo danh tổ chức thiện nguyện, lấy ảnh bệnh nhân/vùng bão lũ chỉnh sửa ghép số tài khoản cá nhân để kêu gọi quyên góp khẩn cấp.
- **Hành động khuyến nghị:** Chỉ quyên góp qua các tổ chức uy tín đã được xác minh chính thức (Mặt trận Tổ quốc, Hội Chữ thập đỏ, các quỹ thiện nguyện xác thực trên ví điện tử MoMo).

## [SCAM-21] Lừa đảo Xuất khẩu lao động, Xin việc làm nước ngoài lương cao
- **Nhóm chiêu thức:** Recruitment Fraud, Advance Fee Trap.
- **Dấu hiệu nhận diện:** Hứa hẹn đi làm việc tại nước ngoài hoặc khu vực biên giới với lương 25–40 triệu/tháng không cần bằng cấp/ngoại ngữ; yêu cầu đóng phí làm visa/cọc hồ sơ trước hoặc dụ sang nước ngoài bất hợp pháp.
- **Hành động khuyến nghị:** Chỉ kiểm tra doanh nghiệp xuất khẩu lao động được Bộ Lao động – Thương binh và Xã hội cấp phép chính thức.

## [SCAM-22] Lừa đảo Mua bán hàng hóa, Xe cộ, Thuê phòng trọ giá rẻ trên mạng xã hội
- **Nhóm chiêu thức:** Fraudulent E-commerce, Scarcity.
- **Dấu hiệu nhận diện:** Đăng bán hàng điện tử, xe máy cũ, phòng trọ đẹp giá rẻ bất thường; yêu cầu chuyển tiền cọc giữ chỗ/phí ship trước khi xem trực tiếp rồi chặn liên lạc.
- **Hành động khuyến nghị:** Không chuyển tiền đặt cọc cho người bán lạ trên mạng xã hội khi chưa kiểm tra thực tế hoặc không có cơ chế bảo vệ người mua qua sàn uy tín.

## [SCAM-23] Lừa đảo Cài mã QR giả dán đè tại điểm bán hàng (Quishing)
- **Nhóm chiêu thức:** Technical Spoofing (QR Phishing).
- **Dấu hiệu nhận diện:** Mã QR thanh toán tại quán ăn/cửa hàng bị dán đè bằng QR của kẻ gian, hoặc mã QR gửi qua tin nhắn dẫn tới trang web giả mạo ngân hàng đòi nhập mật khẩu/OTP.
- **Hành động khuyến nghị:** Luôn đối chiếu tên chủ tài khoản nhận tiền hiển thị trên app với tên cửa hàng trước khi bấm Xác nhận. Không quét QR lạ từ tờ rơi/tin nhắn không rõ nguồn gốc.

## [SCAM-24] Lừa đảo Chiếm đoạt tài khoản qua Link đăng nhập giả / Quét mã QR Zalo Web
- **Nhóm chiêu thức:** Account Takeover (ATO), Session Hijacking.
- **Dấu hiệu nhận diện:** Gửi đường link giả mạo giao diện đăng nhập Facebook/Zalo/MoMo hoặc dụ quét mã QR đăng nhập Zalo Web dưới vỏ bọc "nhận mã khuyến mãi", "xác nhận đơn hàng". Sau khi chiếm nick, kẻ gian nhắn tin vay tiền toàn bộ danh sách bạn bè.
- **Hành động khuyến nghị:** Không quét mã QR đăng nhập Zalo/ứng dụng từ người khác gửi. Bật xác thực 2 lớp (2FA) và kiểm tra mục "Thiết bị đã đăng nhập" để đăng xuất thiết bị lạ.
