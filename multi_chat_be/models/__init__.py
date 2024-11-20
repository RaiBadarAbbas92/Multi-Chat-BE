from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session

# Database URL configuration would typically go here
DATABASE_URL = "sqlite:///./sql_app.db"

# Create SQLite engine instance
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialize the database by creating all tables"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session

