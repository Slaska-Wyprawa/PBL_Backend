from typing import List, Optional
from pydantic import BaseModel


class PlaceBaseSchema(BaseModel):
    ObjectId: int
    Name: str
    Description: str
    ImagePath: str
    Longitude: float
    Latitude: float

    class Config:
        orm_mode = True

class PlaceSchema(PlaceBaseSchema):

    OPMapLink: Optional[str] = None
    GMapLink: str
    EasyAcces: bool
    FreeParking: Optional[bool] = None
    FreeEntry: bool

    class Config:
        orm_mode = True

class DisabilitiesSchema(BaseModel):
    ObjectId: int
    DiscountList: List[str]

    class Config:
        orm_mode = True