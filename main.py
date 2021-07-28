from fastapi import FastAPI
from app import models
from app.database import engine
from app.router import item

app = FastAPI()

models.Base.metadata.create_all(engine) 

app.include_router(item.router)