from fastapi import FastAPI
from multi_chat_be.database.db import Base, engine
from multi_chat_be.routes.user_routes import router as user_router
from multi_chat_be.routes.chatbot_routes import router as chatbot_router
from multi_chat_be.routes.test_routes import router as test_router

# Initialize database tables
Base.metadata.create_all(bind=engine)
 
app = FastAPI()

# Register routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(chatbot_router, prefix="/chatbots", tags=["chatbots"])
app.include_router(test_router, prefix="/test", tags=["test"])
 
@app.get("/")
def read_root(): 
    return {"message": "Welcome to the Multi-Chatbot Platform!"}
 

def start():
    import uvicorn
    uvicorn.run("multi_chat_be.main:app", host="127.0.0.1", port=8080, reload=True)


  
