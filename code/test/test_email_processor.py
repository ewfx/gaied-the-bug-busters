import pytest
from src.app.services.email_processor import process_email

def test_process_email():
    """Test the email processing logic."""
    email_body = "This is a test email"
    attachments = ["temp/test_file.txt"]  # Dummy attachment path
    
    result = process_email(email_body, attachments)
    
    assert result is not None
    assert "processed" in result  # Modify based on expected output
