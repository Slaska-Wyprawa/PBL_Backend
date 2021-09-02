from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas
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
    try:
        places = db.query(models.Object).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    if not places:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no places were found")
    return places


@app.get("/places/{id}", response_model=schemas.PlaceSchema)
def get_one_place(id: int, response: Response, db: Session = Depends(get_db)):
    place = db.query(models.Object).filter(models.Object.ObjectId == id).first()
    if not place:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'place with id {id} is not avilable')
    return place
