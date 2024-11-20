from pydantic import BaseModel

class DocumentUpload(BaseModel):
    file_name: str
    file_size: int
    file_type: str
