from fastapi import FastAPI
from app.core.db.database import in_db
from app.api.manage_services import router as manage_services

app = FastAPI()
in_db()
app.include_router(manage_services, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: Manage Services for Companies!"}