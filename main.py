from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas
from models import Object,
from database import SessionLocal
from typing import List, Optional

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/places", response_model=List[schemas.PlaceBaseSchema])
def get_all_places(db: Session = Depends(get_db)):
    try:
        places = db.query(Object.ObjectId,Object.Name, Object.Latitude, Object.Longitude, Object.Description).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not places:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no places were found")
    return places


@app.get("/places/{id}", response_model=schemas.PlaceSchema)
def get_one_place(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        place = db.query(models.Object).filter(models.Object.ObjectId == id).first()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place


@app.get("/discount/{id}" )
def get_one_place(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        place = db.query(models.Dstype.DSTDesc).select_from(models.Object).join(
            models.Discount).join(models.Dstype).filter(models.Discount.ObjectId == id).filter(
            models.Discount.DSType == models.Dstype.DSTId).all()

        '''place_response = {
            'ObjectId': id,
            'DiscountList': List[place]
        }'''
        print(type(place))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place
