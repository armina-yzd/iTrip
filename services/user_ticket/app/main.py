from fastapi import FastAPI
from app.core.db.database import in_db
from app.api.buy_ticket_api import router as buy_ticket

app = FastAPI()
in_db()
app.include_router(buy_ticket, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: Buying and Overseeing Tickets for Users!"}