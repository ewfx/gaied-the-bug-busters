import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_image(imagePath: str) -> str:
    """
    Extract text from an image using Tesseract OCR.
    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""
    
def extract_text_from_pdf(pdfPath: str) -> str:
    """
    Extract text from a PDF by converting it to images and applying OCR.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return ""