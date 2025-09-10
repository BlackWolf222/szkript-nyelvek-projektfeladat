import fitz

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self) -> str:
        try:
            with fitz.open(self.file_path) as pdf:
                text = ""
                for page in pdf:
                    text += page.get_text()
                    print(text)
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return ""
