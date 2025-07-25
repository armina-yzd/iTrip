from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.media import router as media_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS", "GET", "DELETE"],
    allow_headers=["*"],
)
app.include_router(media_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: media service!"}