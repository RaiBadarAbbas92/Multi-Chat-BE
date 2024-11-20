from pydantic import BaseModel

class ChatbotCreate(BaseModel):
    name: str
    description: str
    personality: str

class ChatbotUpdate(BaseModel):
    name: str
    description: str
    personality: str
