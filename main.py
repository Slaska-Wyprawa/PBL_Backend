from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas
from database import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
import models
from typing import List, Optional

app = FastAPI()




@app.get("/places", response_model=List[models.Objects])
def get_all_places():
    try:
        with Session(engine) as session:
            places = session.exec(select(models.Objects)).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    if not places:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no places were found")
    return places

@app.get("/test")
def get_test_model():
    with Session(engine) as session:
        test = session.exec(select(models.Disabledfacility)).all()
    return  test

'''
@app.get("/places/{id}", response_model=schemas.PlaceSchema)
def get_one_place(id: int, response: Response, db: Session = Depends(get_db)):
    place = db.query(models.Object).filter(models.Object.ObjectId == id).first()
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place
@app.get("/discount")
def get_all_places(db: Session = Depends(get_db)):
    try:
        discout = db.query(models.Dstype).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    if not discout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no discout were found")
    return discout'''