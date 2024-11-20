from multi_chat_be.models.user import User
from multi_chat_be.database.db import get_db
from multi_chat_be.schemas.user_schema import UserCreate, UserLogin
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: UserCreate, db: Session):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully"}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def login_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}
