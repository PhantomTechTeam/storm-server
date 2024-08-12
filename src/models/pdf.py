from pydantic import BaseModel


class PdfInput(BaseModel):
    content: str
    user_id: str
    topic: str
