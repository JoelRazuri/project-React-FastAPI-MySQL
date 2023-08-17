from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config


engine = create_engine(config("URL_CONNECTION"))
local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


def get_db():
    db = local_session()
    try:
        yield db
    finally: 
        db.close()