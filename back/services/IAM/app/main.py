from fastapi import FastAPI
from app.core.db.database import in_db
from app.api.users_api import router as users_router

app = FastAPI()
in_db()
app.include_router(users_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI SQLAlchemy Demo!"}