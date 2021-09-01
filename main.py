import databases, sqlalchemy
from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/places")
def get_all_places(db: Session = Depends(get_db)):
    places = db.query(models.Object).all()
    return places


@app.get("/places/{id}", status_code=200)
def get_one_place(id: int, response: Response, db: Session = Depends(get_db)):
    place = db.query(models.Object).filter(models.Object.ObjectId == id).first()
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place
