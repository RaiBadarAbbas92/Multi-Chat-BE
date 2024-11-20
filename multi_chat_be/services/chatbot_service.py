from fastapi import HTTPException
from sqlalchemy.orm import Session
from multi_chat_be.models.chatbot import Chatbot
from multi_chat_be.schemas.chatbot_schema import ChatbotCreate, ChatbotUpdate
from multi_chat_be.utils.langchain_utils import get_gemanai_response, similarity_search


def create_chatbot(chatbot: ChatbotCreate, db: Session):
    """
    Create a new chatbot entry in the database.
    """
    db_chatbot = Chatbot(
        name=chatbot.name,
        description=chatbot.description,
        personality=chatbot.personality,
    )
    db.add(db_chatbot)
    db.commit()
    db.refresh(db_chatbot)
    return {"message": "Chatbot created successfully", "chatbot": db_chatbot}


def update_chatbot(chatbot_id: int, chatbot: ChatbotUpdate, db: Session):
    """
    Update an existing chatbot's information.
    """
    db_chatbot = db.query(Chatbot).filter(Chatbot.id == chatbot_id).first()
    if not db_chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found.")

    db_chatbot.name = chatbot.name
    db_chatbot.description = chatbot.description
    db_chatbot.personality = chatbot.personality
    db.commit()
    db.refresh(db_chatbot)
    return {"message": "Chatbot updated successfully", "chatbot": db_chatbot}


def get_chatbots(db: Session):
    """
    Retrieve all chatbots from the database.
    """
    return db.query(Chatbot).all()


def test_chatbot(chatbot_id: int, query: str, db: Session):
    """
    Test the chatbot by querying similar documents or generating a response.
    """
    db_chatbot = db.query(Chatbot).filter(Chatbot.id == chatbot_id).first()
    if not db_chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found.")

    # Search for similar documents
    document_response = similarity_search(query)
    if document_response != "No similar documents found.":
        return {"response": document_response}

    # Generate response from GemanAI
    response = get_gemanai_response(query)
    return {"response": response}
