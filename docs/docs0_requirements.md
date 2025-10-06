```bash
Đề tài thì như hôm trước anh em mình trao đổi, anh sẽ chọn đề tài số 34: RegCheck Agent for Banking Compliance Automation
Hướng làm sẽ là xây dựng một hệ thống MAS, gồm nhiều Agent, mỗi Agent sẽ đảm nhiệm một bước (đối với Supporting Domain) hoặc một Domain (đối với các Core Domain). Mỗi một Agent sẽ kết nối tới một hoặc một vài MCP Server để lấy thông tin, tài liệu, skill, domain knowledge, quy trình xử lý (Prompt) ... dành cho nó. Prompt cứng đi kèm trong code sẽ khá ít
Ngoài phần back-end nói trên thì sẽ có môt phần Front-End dành cho người dùng đăng nhập, upload tài liệu cần check, xem report, yêu cầu DeepCheck lại từng câu hoặc đoạn của tài liệu, yêu cầu giải thích chi tiết ...
Em có bạn nào chuyên về Front-End thì giới thiệu nhé. Anh cũng chưa chốt vị trí cho phần này
LLMs thì có thể dùng AWS Bedrock với sonet 4.5 hoặc gpt-oss-20b, gpt-oss-120b
Ưu tiên sẽ là gpt-oss vì nó cũng đang là định hướng của anh Hùng - Head of AI bên đó
Trên giao diện, có thể cho người dùng tùy chọn sử dụng model
```


---
