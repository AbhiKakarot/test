from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from files import crud, models, schemas
from files.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.post("/post_location", response_model=schemas.Location)
def create_location(loc: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.add_location(db=db, loc=loc)

@app.get("/get_location/{latitude}/{longitude}")
def get_location(latitude: float, longitude: float, db: Session = Depends(get_db)):
    return crud.get_location_by_ll(db=db, latitude = latitude, longitude = longitude)