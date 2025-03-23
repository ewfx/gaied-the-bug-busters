import pytest
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_health_check():
    """Test a dummy API to check if the app is running."""
    response = client.get("/health")  # Assuming you added a dummy API at /health
    assert response.status_code == 200
    assert response.json() == {"message": "App is running!", "status": "ok"}

def test_process_email():
    """Test the email processing API with dummy data."""
    files = {"files": ("test.txt", b"dummy file content")}
    response = client.post(
        "/process-email", 
        data={"email_body": "Test email body"}, 
        files=files
    )
    
    assert response.status_code == 200
    assert "processed" in response.json()  # Assuming your API returns processed data