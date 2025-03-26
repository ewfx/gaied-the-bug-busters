from pydantic import BaseModel
from typing import List, Optional

class EmailRequest(BaseModel):
    subject: str
    email_body: str
    filenames: Optional[List[str]] = []  # This is just metadata for attachments