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


@user_router.get("(/{id:int}", response_model=UserId)
async def get_user(id:int, db: Session = Depends(get_db)):
    user_by_id = await UserService.get_user_by_id(db, id)
    
    if not user_by_id:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="El usuario no se encuentra.")    
    
    return user_by_id 


@user_router.post("/", response_model=UserId, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserData, db: Session = Depends(get_db)):
    check_name = await UserService.get_user_by_username(db, user.username)

    if check_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El nombre de usuario ya existe.")
    
    return await UserService.create_user(db, user)
    
