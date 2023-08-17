from sqlalchemy import Column, String, Integer
from app.database.db_conn import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(30), index=True, unique=True)
    password = Column(String(30), index=True)

