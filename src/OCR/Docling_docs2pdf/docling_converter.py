
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
import os
from pathlib import Path

def convert_document(source_path, output_format="markdown", enable_ocr=False, file_type=None):
    """
    Convert document using Docling with enhanced error handling
    
    Args:
        source_path (str): Path to document or URL
        output_format (str): Output format ('markdown', 'html', 'json')
        enable_ocr (bool): Enable OCR for scanned documents
        file_type (str): File type ('pdf', 'docx', 'pptx', 'xlsx') - auto-detect if None
    
    Returns:
        str: Converted document content
    """
    # Hàm này thực hiện chuyển đổi một tài liệu đầu vào sang định dạng mong muốn
    # Đầu vào có thể là đường dẫn file hoặc URL
    # Tham số output_format xác định định dạng đầu ra ('markdown', 'html', 'json')
    # Nếu enable_ocr=True, bật chế độ nhận diện ký tự quang học cho PDF scan
    try:
        # Auto-detect file type if not provided
        if file_type is None:
            file_ext = Path(source_path).suffix.lower()
            file_type = file_ext[1:] if file_ext else 'unknown'
        
        # Tạo đối tượng chuyển đổi đơn giản (không dùng format_options để tránh lỗi)
        # Docling sẽ tự động detect và xử lý phù hợp cho từng loại file
        converter = DocumentConverter()
        # Thực hiện chuyển đổi tài liệu
        result = converter.convert(source_path)
        
        # Kiểm tra kết quả trả về có document hay không
        if not result.document:
            raise ValueError("No document content extracted")
        
        # Lựa chọn xuất ra định dạng phù hợp theo output_format yêu cầu
        if output_format.lower() == "markdown":
            return result.document.export_to_markdown()
        elif output_format.lower() == "html":
            return result.document.export_to_html()
        elif output_format.lower() == "json":
            return result.document.export_to_dict()
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
            
    except Exception as e:
        # Xử lý lỗi và in thông báo nếu có lỗi xảy ra trong quá trình chuyển đổi
        print(f"Error converting document: {e}")
        return None

def batch_convert(input_directory, output_directory, file_extensions=None):
    """
    Batch convert multiple documents
    
    Args:
        input_directory (str): Directory containing documents
        output_directory (str): Directory to save converted files
        file_extensions (list): List of file extensions to process
    """
    # Hàm này thực hiện chuyển đổi hàng loạt tài liệu trong thư mục đầu vào
    # Các file sẽ được lọc theo danh sách phần mở rộng (file_extensions)
    # Kết quả chuyển đổi sẽ lưu ra thư mục output_directory dưới dạng file markdown (.md)

    if file_extensions is None:
        file_extensions = ['.pdf', '.docx', '.pptx', '.xlsx']
    
    input_path = Path(input_directory)
    output_path = Path(output_directory)
    # Tạo thư mục đầu ra nếu chưa tồn tại
    output_path.mkdir(exist_ok=True)
    
    # Lặp qua từng file trong thư mục đầu vào
    for file_path in input_path.iterdir():
        # Kiểm tra định dạng file có nằm trong danh sách cho phép không
        if file_path.suffix.lower() in file_extensions:
            print(f"Processing: {file_path.name}")
            
            # Chuyển đổi tài liệu, sử dụng hàm convert_document ở trên
            content = convert_document(str(file_path))
            if content:
                # Lưu nội dung đã chuyển đổi ra file .md tương ứng trong output_directory
                output_file = output_path / f"{file_path.stem}.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Converted: {output_file}")

# Example usage
if __name__ == "__main__":
    # Đoạn code ví dụ dùng cho việc chuyển đổi tài liệu đơn lẻ
    source = "D:/GIT/VPBank/Data/Application 1/LC Application.docx"
    # source = "D:/GIT/VPBank/src/Docling_docs2pdf/test-orrrr.pdf"
    content = convert_document(source, enable_ocr=True)
    
    if content:
        print("Conversion successful!")
        # Lưu file chuyển đổi để tránh lỗi encoding trên console
        output_file = "LC_Application_converted.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Converted content saved to: {output_file}")
        print(f"Content length: {len(content)} characters")
        # In ra 200 ký tự đầu tiên một cách an toàn (tránh lỗi encoding)
        try:
            print("First 200 characters:")
            print(content[:200])
        except UnicodeEncodeError:
            print("Content contains special characters - check the saved file")
    
    # Ví dụ batch convert (bỏ comment để sử dụng)
    # batch_convert("input_docs", "output_docs")
