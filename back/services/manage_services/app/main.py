from fastapi import FastAPI
from app.core.db.database import in_db
from app.api.test import router as test
from app.api.manage_services.add_services import router as add_services
from app.api.manage_services.get_services import router as get_services
from app.api.filter_services.filter_services import router as filter_services
from app.api.filter_services.service_info import router as service_info

app = FastAPI()
in_db()
app.include_router(test, prefix="/api")
app.include_router(add_services, prefix="/api")
app.include_router(get_services, prefix="/api")
app.include_router(filter_services, prefix="/api")
app.include_router(service_info, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "iTrip: Manage Services for Companies!"}