import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from app.utils.text_parser import extract_text_from_docx
from app.models.classifier import email_classifier
from app.models.extractor import email_extractor

class EmailProcessor:
    def process_email(self, email_body: str, attachments: list):
        # 1. Classify Email
        classification = email_classifier.classify(email_body)

        # 2. Extract the key fields
        extracted_data = email_extractor.extract_fields(email_body)

        #3. Process attachments (OCR for PDFs and images)
        for attachment in attachments:
            if attachment.endswith(".pdf"):
                with pdfplumber.open(attachment) as pdf:
                    for page in pdf.pages:
                        extracted_data.update(email_extractor.extract_fields(page.extract_text))
            elif attachment.endswith(".jpg") or attachment.endswith(".png"):
                image = convert_from_path(attachment)
                extracted_text = pytesseract.image_to_string(image)
                extracted_data.update(email_extractor.extract_fields(extracted_text))

        return {"classification": classification, "extracted_data": extracted_data}
    
email_processor = EmailProcessor()