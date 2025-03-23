from fastapi import APIRouter, UploadFile, File
from app.services.email_processor import email_processor

router = APIRouter()

@router.post("/process-email")
async def process_email(email_body: str, files: list[UploadFile] = File(None)):
    attachments = []
    for file in files:
        with open(f"temp/{file.filename}", "wb") as buffer:
            buffer.write(await file.read())
        attachments.append(f"temp/{file.filename}")

    result = email_processor.process_email(email_body, attachments)
    return result

@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "App is running!"}