Tôi sẽ kiểm tra nội dung thư mục Data để xem có những gì bên trong.

[1 tool called]

Dựa trên cấu trúc thư mục Data, đây là những gì có trong thư mục:

## 📁 **Cấu trúc thư mục Data**

### **1. Application 1** (Đơn đăng ký 1)

- `Sale Contract.pdf` - Hợp đồng mua bán
- `LC Application.docx` - Đơn đăng ký LC
- `LC Application_Legal Check Result.docx` - Kết quả kiểm tra tuân thủ (có sẵn)
- `~$LES_CONTRACT_TV250702_.docx` - File tạm của Word

### **2. Application 2** (Đơn đăng ký 2)

- `Sale Contract.pdf` - Hợp đồng mua bán
- `LC Application.docx` - Đơn đăng ký LC
- `LC Application_Legal Check Result.docx` - Kết quả kiểm tra tuân thủ (có sẵn)

### **3. Application 3** (Đơn đăng ký 3)

- `Sale Contract.pdf` - Hợp đồng mua bán
- `LC Application.docx` - Đơn đăng ký LC
- **Không có** `LC Application_Legal Check Result.docx` (đây là test case)

### **4. International Regulations** (Quy định quốc tế)

- `Incoterms2020.pdf` - Quy tắc thương mại quốc tế 2020
- `ISBP 821.pdf` - Quy tắc thực hành ngân hàng 821
- `ISBP745.PDF` - Quy tắc thực hành bổ sung 745
- `UCP600_English.pdf` - Quy tắc thống nhất về tín dụng chứng từ 600

## 🎯 **Mục đích sử dụng**

### **Application 1 & 2:**

- **Dữ liệu huấn luyện**: Có sẵn kết quả kiểm tra để AI học
- **So sánh**: Để đánh giá độ chính xác của hệ thống
- **Validation**: Kiểm tra xem AI có đưa ra kết quả tương tự không

### **Application 3:**

- **Test case**: Không có kết quả sẵn
- **Mục tiêu**: Hệ thống phải tự tạo ra kết quả kiểm tra
- **Đánh giá**: So sánh với kết quả thực tế để đánh giá độ chính xác

## 🔄 **Quy trình sử dụng dữ liệu**

1. **Đọc Sale Contract** → Hiểu nội dung giao dịch
2. **Đọc LC Application** → Kiểm tra đơn đăng ký
3. **Tham khảo International Regulations** → So sánh với quy định
4. **Tạo kết quả kiểm tra** → Tương tự như `LC Application_Legal Check Result.docx`
5. **So sánh với kết quả mẫu** (Application 1, 2) để đánh giá độ chính xác

Đây là một bộ dữ liệu hoàn chỉnh để phát triển và test hệ thống RegCheck Agent!
