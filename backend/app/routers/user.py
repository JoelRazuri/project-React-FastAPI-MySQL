from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user_schema import UserData, UserId
from app.services.user_service import UserService
from app.database.db_conn import engine, Base, get_db
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

user_router = APIRouter()


@user_router.get("/", response_model=list[UserId])
async def get_users(db: Session = Depends(get_db)):
    return await UserService.get_users(db)



