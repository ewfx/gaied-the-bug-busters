from typing import List, Optional
from fastapi import APIRouter, Body, UploadFile, File, Body, Request
from app.services.email_processor import email_processor
from app.models.email_request import EmailRequest

router = APIRouter()

@router.post("/process-email")
async def process_email(
    request: EmailRequest,  # Use the model
    files: Optional[List[UploadFile]] = File(None),  # Allow multiple file uploads                 
):
    body = await request.model_dump_json()
    print("Received Request:", body)
    attachments = []
    for file in files:
        with open(f"temp/{file.filename}", "wb") as buffer:
            buffer.write(await file.read())
        attachments.append(f"temp/{file.filename}")

        result = email_processor.process_email(request.subject, request.email_body, attachments)
    return {"status": "success", "result": result}

@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "App is running!"}