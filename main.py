from fastapi import FastAPI
from database.database import engine
from database import models
from routers import conversation, message
from auth import authentication

app =FastAPI()
#app.include_router(authentication.router)
#app.include_router(user.router)
app.include_router(conversation.router)
app.include_router(message.router)



models.Base.metadata.create_all(engine)