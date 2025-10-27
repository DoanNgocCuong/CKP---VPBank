# RegCheck Agent - Tự động hóa tuân thủ ngân hàng

## Mục tiêu:

Phát triển hệ thống RegCheck Agent dựa trên công nghệ GenAI/Agentic AI để kiểm tra tính tuân thủ của đơn đăng ký LC với luật pháp và các quy định/quy tắc quốc tế.

**Đầu vào:** Tài liệu đơn đăng ký của công ty

**Đầu ra:** Kiểm tra xem tài liệu có tuân thủ quy định hay không; Xác định các điểm không tuân thủ và giải thích lý do không tuân thủ

## 2. Dữ liệu

Có 3 đơn đăng ký LC được bao gồm trong dữ liệu được cung cấp:

**Đơn đăng ký 1, 2:** mỗi đơn đăng ký bao gồm 3 tệp:

- **Sale Contract.pdf:** tệp hợp đồng giữa người mua và người bán
- **LC Application.docx:** tệp đơn đăng ký do công ty nộp
- **LC Application_Legal Check Result.docx:** hiển thị kết quả kiểm tra tuân thủ (kết quả được ghi chú trong các bình luận tương ứng)

Chúng ta sẽ sử dụng thông tin trong tệp **Sale Contract.pdf** để kiểm tra tính tuân thủ của **LC Application.docx** đối với bốn tệp quy định trong thư mục **International Regulations** (Incoterms 2020, ISBP 821, ISBP 745, UCP 600). Tệp **LC Application_Legal Check Result.docx** có thể được sử dụng để hiểu rõ hơn về các yêu cầu và kết quả mong đợi.

**Đơn đăng ký 3:**

Chỉ bao gồm **Sale Contract.pdf** và **LC Application.docx**. Giải pháp cần tạo ra kết quả tương tự như trong **LC Application_Legal Check Result.docx** của Đơn đăng ký 1 và 2, và kết quả này sẽ được gửi lại để xác minh độ chính xác của LC Advisor.

## Cấu trúc dữ liệu

### Thư mục Data/
- **Application 1/**
  - Sale Contract.pdf
  - LC Application.docx  
  - LC Application_Legal Check Result.docx
- **Application 2/**
  - Sale Contract.pdf
  - LC Application.docx
  - LC Application_Legal Check Result.docx
- **Application 3/**
  - Sale Contract.pdf
  - LC Application.docx
- **International Regulations/**
  - Incoterms2020.pdf
  - ISBP 821.pdf
  - ISBP745.PDF
  - UCP600_English.pdf

## Quy trình hoạt động

1. **Thu thập dữ liệu đầu vào:** Đọc và phân tích các tài liệu đơn đăng ký LC
2. **Kiểm tra tuân thủ:** So sánh với các quy định quốc tế (Incoterms, ISBP, UCP)
3. **Xác định vi phạm:** Tìm ra các điểm không tuân thủ
4. **Báo cáo kết quả:** Tạo báo cáo chi tiết với lý do vi phạm và khuyến nghị

## Công nghệ sử dụng

- **GenAI/Agentic AI:** Công nghệ trí tuệ nhân tạo thế hệ mới
- **Multi-Agent System:** Hệ thống đa tác nhân để xử lý các tác vụ phức tạp
- **Document Processing:** Xử lý tài liệu tự động
- **Compliance Checking:** Kiểm tra tuân thủ tự động

## Lợi ích

- **Tự động hóa:** Giảm thời gian kiểm tra thủ công
- **Độ chính xác cao:** Phát hiện lỗi và vi phạm một cách chính xác
- **Tiết kiệm chi phí:** Giảm nhân lực cần thiết cho việc kiểm tra
- **Tuân thủ quốc tế:** Đảm bảo tuân thủ các quy định quốc tế

