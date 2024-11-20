from sqlalchemy import Column, Integer, String, Text
from multi_chat_be.database.db import Base

class Chatbot(Base):
    __tablename__ = "chatbots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    personality = Column(Text)
