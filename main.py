from fastapi import FastAPI, Depends, status, Response, HTTPException, Query
import schemas
from database import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
import models
from typing import List, Optional

app = FastAPI()


@app.get("/place", response_model=List[models.BaseObject])
def get_all_places(offset: int = 0, limit: int = Query(default=30, lte=100)):
    try:
        with Session(engine) as session:
            places = session.exec(
                select(models.Object.ObjectId, models.Object.Name, models.Object.Longitude, models.Object.Latitude,
                       models.Object.Description, models.Object.ImagePath).offset(offset).limit(limit)).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not places:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return places


@app.get("/place/{id}", response_model=models.Object)
def get_one_place(id: int):
    try:
        with Session(engine) as session:
            place = session.exec(select(models.Object).where(models.Object.ObjectId == id)).first()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place


@app.get("/discount/{place_id}", response_model=models.DisabilitiesSchema)
def get_one_place(place_id: int):
    try:
        with Session(engine) as session:
            discounts = session.exec(
                select(models.Object.ObjectId, models.Dstype.DSTDesc).select_from(models.Object).join(
                    models.Discount).join(models.Dstype).where(models.Discount.ObjectId == place_id)).all()
            discounts_list = {
                'ObjectId': place_id,
                'DiscountList': [discounts[x][1] for x in range(len(discounts))]
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not discounts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no discounts for place with id {place_id}')
    return discounts_list


