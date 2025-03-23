import os
from reportlab.pdfgen import canvas

# Define paths
test_data_dir = os.path.join("test", "test_data")
pdf_path = os.path.join(test_data_dir, "sample.pdf")

# Ensure the directory exists
os.makedirs(test_data_dir, exist_ok=True)

def generate_sample_pdf():
    """Creates a sample PDF file inside test/test_data/"""
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Sample PDF for Testing")
    c.drawString(100, 730, "This is a generated PDF file for test purposes.")
    c.save()
    print(f"Sample PDF created at: {pdf_path}")

if __name__ == "__main__":
    generate_sample_pdf()