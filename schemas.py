from typing import List, Optional
from pydantic import BaseModel




class PlaceSchema(BaseModel):
    ObjectId: int
    Name: str
    Description: str
    ImagePath: str
    Longitude: float
    Latitude: float
    OPMapLink: Optional[str] = None
    GMapLink: str
    EasyAcces: bool
    FreeParking: Optional[bool] = None
    FreeEntry: bool

    class Config:
        orm_mode = True
