import re

class TextParser:
    """A utility class for extracting text from different file formats."""

    def clean_text(text: str) -> str:
        """
        Clean text by removing extra whitespace and non-alphanumeric characters.
        :param text: Input text.
        :return: Cleaned text.
        """
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()

    def extract_key_information(text: str) -> dict:
        """
        Extract key pieces of information from the text.
        Example: Extracting emails, phone numbers, and dates.
        :param text: Cleaned text.
        :return: Dictionary of extracted information.
        """
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        phone_pattern = r'\+?\d[\d -]{8,}\d'  # Simple phone number regex
        date_pattern = r'\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b'  # Date formats like 12/05/2023

        emails = re.findall(email_pattern, text)
        phones = re.findall(phone_pattern, text)
        dates = re.findall(date_pattern, text)

        return {
            "emails": emails,
            "phone_numbers": phones,
            "dates": dates,
            "text_snippet": text[:500]  # Limit preview to 500 characters
        }
    
    @staticmethod
    def extract_text_from_txt(file_path: str) -> str:
        """Extract text from a .txt file."""
        if not file_path.lower().endswith(".txt"):
            raise ValueError("Invalid file format. Expected .txt file.")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            raise RuntimeError(f"Error reading text file: {e}")

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from a .pdf file."""
        if not file_path.lower().endswith(".pdf"):
            raise ValueError("Invalid file format. Expected .pdf file.")

        try:
            reader = PdfReader(file_path)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            return text.strip()
        except Exception as e:
            raise RuntimeError(f"Error extracting text from PDF: {e}")

    #@staticmethod
    def extract_text_from_docx(file_path: str) -> str:
        """Extract text from a .docx file."""
        if not file_path.lower().endswith(".docx"):
            raise ValueError("Invalid file format. Expected .docx file.")

        try:
            doc = Document(file_path)
            text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
            return text.strip()
        except Exception as e:
            raise RuntimeError(f"Error extracting text from DOCX: {e}")

    @staticmethod
    def extract_text(file_path: str) -> str:
        """Determine file type and extract text accordingly."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        ext = file_path.lower().split(".")[-1]
        if ext == "txt":
            return TextParser.extract_text_from_txt(file_path)
        elif ext == "pdf":
            return TextParser.extract_text_from_pdf(file_path)
        elif ext == "docx":
            return TextParser.extract_text_from_docx(file_path)
        else:
            raise ValueError("Unsupported file format. Supported formats: .txt, .pdf, .docx")

# Expose methods outside the class for direct import
extract_text_from_txt = TextParser.extract_text_from_txt
extract_text_from_pdf = TextParser.extract_text_from_pdf
extract_text_from_docx = TextParser.extract_text_from_docx
extract_text = TextParser.extract_text_from_docx