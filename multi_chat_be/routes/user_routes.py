from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from multi_chat_be.schemas.user_schema import UserCreate, UserLogin
from multi_chat_be.services.user_service import create_user, login_user
from multi_chat_be.database.db import get_db
router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)
 
@router.post("/login")
def login_user_endpoint(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)
