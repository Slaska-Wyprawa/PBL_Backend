from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from starlette import status

from database import models
from database.database import engine

router = APIRouter(tags=['More informations'])


@router.get("/discount/{place_id}", response_model=models.DiscountSchema)
def get_discounts(place_id: int):
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


@router.get("/disabilities/{place_id}", response_model=models.DisabilitiesSchema)
def get_disabilities(place_id: int):
    try:
        with Session(engine) as session:
            disabilities = session.exec(
                select(models.Object.ObjectId, models.Dftype.DFTDesc).select_from(models.Object).join(
                    models.Disabledfacilitie).join(models.Dftype).where(
                    models.Disabledfacilitie.DFObjectId == place_id)).all()
            disabilities_list = {
                'ObjectId': place_id,
                'DisabilitiesList': [disabilities[x][1] for x in range(len(disabilities))]
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not disabilities:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'no disabilities for place with id {place_id}')
    return disabilities_list
