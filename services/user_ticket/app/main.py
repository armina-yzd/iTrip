from fastapi import FastAPI
from app.core.db.database import in_db
from app.api.buy_ticket_api import router as buy_ticket
from app.api.ticket_info import router as ticket_info
from app.api.view_ticket import router as view_ticket

app = FastAPI()
in_db()
app.include_router(buy_ticket, prefix="/api")
app.include_router(ticket_info, prefix="/api")
app.include_router(view_ticket, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: Buying and Overseeing Tickets for Users!"}