from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from multi_chat_be.services.chatbot_service import test_chatbot
from multi_chat_be.database.db import get_db

router = APIRouter()

@router.get("/{chatbot_id}/test")
def test_chatbot_response(chatbot_id: int, query: str, db: Session = Depends(get_db)):
    return test_chatbot(chatbot_id, query, db)
