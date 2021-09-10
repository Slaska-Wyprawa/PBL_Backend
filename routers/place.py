from typing import List

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select
from starlette import status

from database import models
from database.database import engine

router = APIRouter(prefix='/place',
                   tags=['Place'])


@router.get("/", response_model=List[models.BaseObject])
async def get_all_places(offset: int = 0, limit: int = Query(default=30, lte=100)):
    try:
        with Session(engine) as session:
            places = session.exec(select(models.Object).offset(offset).limit(limit)).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not places:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return places


@router.get("/{place_id}", response_model=models.Object)
async def get_one_place(place_id: int):
    try:
        with Session(engine) as session:
            place = session.exec(select(models.Object).where(models.Object.ObjectId == place_id)).first()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {place_id} is not available')
    return place
