from typing import Optional, List
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship


class Dftypes(SQLModel, table=True):
    DFTId: Optional[int] = Field(default=None, primary_key=True)
    DFTDesc: str


class Dstypes(SQLModel, table=True):
    DSTId: Optional[int] = Field(default=None, primary_key=True)
    DSTDesc: str


class Objects(SQLModel, table=True):
    ObjectId: Optional[int] = Field(default=None, primary_key=True)
    Name: str
    Description: str
    EasyAcces: bool
    FreeEntry: bool
    ImagePath: str
    FreeParking: Optional[bool] = None
    GMapLink: str
    OPMapLink: Optional[str] = None
    Longitude: float
    Latitude: float


class Disabledfacility(SQLModel, table=True):
    __tablename__ = 'disabledfacilities'

    DFId: Optional[int] = Field(default=None, primary_key=True)
    DFObjectId: int = Field(default=None, foreign_key="objects.ObjectId")
    DFType: int = Field(foreign_key='dftypes.DFTId')

    object:List[Objects] = Relationship(Objects)A
    dftype: List[Dftypes] = Relationship( Dftypes)


'''
class Discount(SQLModel):
    __tablename__ = 'discounts'

    DSId = Column(Integer, primary_key=True, unique=True)
    ObjectId = Column(ForeignKey('objects.ObjectId', ondelete='CASCADE'), nullable=False, index=True)
    DSType = Column(ForeignKey('dstypes.DSTId', ondelete='CASCADE'), nullable=False, index=True)

    dstype = relationship('Dstype')
    object = relationship('Object')
'''
