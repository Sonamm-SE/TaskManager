from fastapi import FastAPI
import models
from database import engine
from routes import user, task

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)