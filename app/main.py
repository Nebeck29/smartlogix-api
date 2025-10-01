from fastapi import FastAPI
from .routes import router


app = FastAPI(title="SmartLogix API")
app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "service": "SmartLogix API"}