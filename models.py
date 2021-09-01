from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.dialects.mysql import TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from database import Base


class Dftype(Base):
    __tablename__ = 'dftypes'

    DFTId = Column(Integer, primary_key=True, unique=True)
    DFTDesc = Column(Text, nullable=False)


class Dstype(Base):
    __tablename__ = 'dstypes'


    DSTId = Column(Integer, primary_key=True, unique=True)
    DSTDesc = Column(TINYTEXT, nullable=False)


class Object(Base):
    __tablename__ = 'objects'

    ObjectId = Column(Integer, primary_key=True, unique=True)
    Name = Column(TINYTEXT, nullable=False)
    Description = Column(Text)
    EasyAcces = Column(TINYINT(1))
    FreeEntry = Column(TINYINT(1))
    ImagePath = Column(Text)
    FreeParking = Column(TINYINT(1))
    GMapLink = Column(Text)
    OPMapLink = Column(Text)
    Longitude = Column(Float)
    Latitude = Column(Float)


class Disabledfacility(Base):
    __tablename__ = 'disabledfacilities'

    DFId = Column(Integer, primary_key=True, unique=True)
    DFObjectId = Column(ForeignKey('objects.ObjectId', ondelete='CASCADE'), nullable=False, index=True)
    DFType = Column(ForeignKey('dftypes.DFTId', ondelete='CASCADE'), nullable=False, index=True)

    object = relationship('Object')
    dftype = relationship('Dftype')


class Discount(Base):
    __tablename__ = 'discounts'

    DSId = Column(Integer, primary_key=True, unique=True)
    ObjectId = Column(ForeignKey('objects.ObjectId', ondelete='CASCADE'), nullable=False, index=True)
    DSType = Column(ForeignKey('dstypes.DSTId', ondelete='CASCADE'), nullable=False, index=True)

    dstype = relationship('Dstype')
    object = relationship('Object')
