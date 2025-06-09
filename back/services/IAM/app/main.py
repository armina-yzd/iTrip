from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db.database import in_db
from app.api.users_api import router as users_router
from app.api.admin_api import router as admins_router
from app.api.company_api import router as company_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS", "GET", "DELETE"],
    allow_headers=["*"],
)
in_db()
app.include_router(users_router, prefix="/api")
app.include_router(admins_router, prefix="/api")
app.include_router(company_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: iam service!"}