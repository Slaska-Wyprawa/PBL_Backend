from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
USER = os.getenv('DATABASE_USERNAME')
PASSWORD = os.getenv('DATABASE_PASSWORD')
ADDRESS = os.getenv('DATABASE_ADDRESS')
PORT = os.getenv('DATABASE_PORT')
NAME = os.getenv('DATABASE_NAME')

#database_connenct_URL = F'mysql://{USER}:{PASSWORD}@157.158.40.129:3306/pblapk_live'
database_connenct_URL = 'mysql://APK:Cpia9qOehPC]-Y!r@157.158.40.129:3306/pblapk_live'
#database_connenct_URL = os.getenv('CONNECT_STRING')

print(database_connenct_URL)

engine = create_engine(database_connenct_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
metadata = Base.metadat

