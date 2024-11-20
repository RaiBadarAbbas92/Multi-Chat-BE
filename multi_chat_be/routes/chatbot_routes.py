from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from multi_chat_be.database.db import get_db
from multi_chat_be.schemas.chatbot_schema import ChatbotCreate, ChatbotUpdate
from multi_chat_be.services.chatbot_service import create_chatbot, update_chatbot, get_chatbots, test_chatbot

router = APIRouter()

@router.post("/")
def create_new_chatbot(chatbot: ChatbotCreate, db: Session = Depends(get_db)):
    return create_chatbot(chatbot, db)

@router.put("/{chatbot_id}")
def update_existing_chatbot(chatbot_id: int, chatbot: ChatbotUpdate, db: Session = Depends(get_db)):
    return update_chatbot(chatbot_id, chatbot, db)

@router.get("/")
def list_all_chatbots(db: Session = Depends(get_db)):
    return get_chatbots(db)

@router.post("/{chatbot_id}/test")
def test_chatbot_response(chatbot_id: int, query: str, db: Session = Depends(get_db)):
    return test_chatbot(chatbot_id, query, db)
