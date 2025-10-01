from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartLogix API")
app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "service": "SmartLogix API"}
